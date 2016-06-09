#!/usr/bin/python
#-*- coding: UTF-8 -*-

import logging, re, time, bisect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from decimal import Decimal
from datetime import datetime, timedelta
from www.models import *
from www.codelist import Codes
from www.yahoo import YQL

def day0(day):
    ret = day - timedelta(hours=day.hour, minutes=day.minute)
    if ret.day != day.day: raise
    return ret

def month0(day):
    return datetime(day.year, day.month, 1)

def index(request):
    setattr(request.user, 'view', "index")
    if not request.user.is_authenticated():
        return render(request, 'www/html/index.html')
    return render(request, 'www/html/profile.html')


@login_required(login_url="/account/login/")
def stock_list(request):
    setattr(request.user, 'view', "stock_list")
    def Name(code):
        return Codes.get(code.strip(), code)
    try: stocks = eval(request.user.profile.stocks_raw)
    except: stocks = {}

    yql = YQL()
    current = []
    history = []
    for code,s in stocks.items():
        if code == '': continue
        if s['num'] > 0:
            s['worth'] = yql.stock(code) * s['num']
            s['earn'] = s['worth'] + s['money']
            current.append( (Name(code), s) )
        else:
            history.append( (Name(code), s) )
    history.sort( lambda x,y: cmp(y[1]['money'], x[1]['money']) )
    return render(request, 'www/html/stock/list.html', {'current': current, 'history': history})

def get_stock_worth(stocks):
    yql = YQL()
    active = dict( (c,s) for c,s in stocks.items() if s['num'] > 0 )
    prices = yql.stocks(active.keys())
    return sum( prices[c]*s['num'] for c,s in active.items() )

@login_required(login_url="/account/login/")
def analyse(request):
    setattr(request.user, 'view', "analyse")
    try: stocks = eval(request.user.profile.stocks_raw)
    except: stocks = {}
    request.user.profile.stocks_val = get_stock_worth(stocks)

    bills = request.user.bill_set.all()
    money = 0
    tax = 0
    fee1 = 0
    fee2 = 0
    fee3 = 0
    for b in bills:
        if b.date.year > 2012 and b.type == b.TYPES['BUY']:
            money -= b.stock_money
        tax += b.tax
        fee1 += b.fee1
        fee2 += b.fee2
        fee3 += b.fee3
    args = {
            'money': money,
            'tax': tax,
            'fee1': fee1,
            'fee2': fee2,
            'fee3': fee3,
        }
    return render(request, 'www/html/analyse.html', args)

def bisect_find(infos, code, day):
    '''有序查找day当天、或前一天的数据'''
    if code not in infos: return None
    hs = infos[code]
    i = bisect.bisect_left(hs, (day.date(), ))
    if i >= len(hs): i -= 1
    elif hs[i][0] != day.date(): i -= 1
    try: return hs[i][1]
    except: return None

def get_date(value):
    return datetime.strptime(value[0:8], "%Y%m%d")

def D(val):
    if val == u'---':
        return Decimal(0)
    return Decimal(val)

@login_required(login_url="/account/login/")
def chart_build(request):
    profile = request.user.profile
    request.user.node_set.all().delete()
    bills = request.user.bill_set.order_by('date').all()
    if bills.count() == 0:
        profile.is_outdate = 0
        profile.save()
        return HttpResponse("no bills?")

    # get stock history data
    querys = {}
    for b in bills:
        code = b.stock_code
        if code not in querys:
            querys[code] = [code, b.date, None]
        querys[code][2] = b.date
    yql = YQL()
    yql.infos = yql.stocks_history(querys.values())
    querys = None

    # build nodes
    first_day = day0(bills[0].date)
    day = first_day
    #today = bills[len(bills)-1].date
    today = timezone.now()
    oneday = timedelta(days=1)
    n = Node(type=Node.TYPES['DAY'], open=0, date=day, user=request.user)
    n.low = n.high = n.close = n.open

    stocks = {}
    base = 0
    free = 0
    balance = 0
    nodes = []

    # FIXME there are bugs
    idx = 0
    while day <= today:
        if idx < len(bills) and n.date.date() == bills[idx].date.date():
            b = bills[idx]
            s = stocks.get(b.stock_code, {'num': 0, 'money': 0})
            s['num'] += b.stock_num
            s['money'] += b.stock_money
            stocks[b.stock_code] = s
            free += b.stock_money
            if b.type == b.TYPES['PUT'] or b.type == b.TYPES['GET']:
                base += b.stock_money
            idx += 1
            balance = b.balance
        else:
            n.low = n.high = n.close = free
            for code,s in stocks.items():
                if s['num'] == 0: continue
                # 查找当天股票价格，计算波动
                h = bisect_find(yql.infos, code, day)
                if h:
                    n.low += s['num']*D(h['Low'])
                    n.high += s['num']*D(h['High'])
                    n.close += s['num']*D(h['Close'])
                else:
                    n.low += s['money']
                    n.high += s['money']
                    n.close += s['money']

            new_open = n.close
            n.close = n.close + n.base - base
            n.base = base
            n.money = n.close - n.open
            n.balance = balance
            if n.date.weekday() < 5: nodes.append( n )
            day += oneday
            n = Node(type=Node.TYPES['DAY'], open=new_open, date=day, user=request.user)
            n.low = n.high = n.close = n.open
            n.base = base

    Node.objects.bulk_create( nodes )

    profile.stocks_num = len([s for s in stocks.values() if s['num'] > 0 ])
    profile.stocks_raw = repr(stocks)
    profile.stocks_val = get_stock_worth(stocks)
    profile.base = base
    profile.free = free
    profile.is_outdate = 0
    profile.save()

    # month nodes
    m_list = []
    m = Node(type=Node.TYPES['MONTH'], open=0, date=month0(first_day), user=request.user)
    m.low = m.high = m.close = m.open
    close = 0
    for n in nodes:
        if n.date.month != m.date.month:
            logging.error("%s - %s" % (n.date,  m.date))
            m_list.append( m )
            m = Node(type=Node.TYPES['MONTH'], open=n.open+n.balance, date=month0(n.date), user=request.user)
            m.low = m.high = m.close = m.open
        if n.low+n.balance < m.low: m.low = n.low+n.balance
        if n.high+n.balance > m.high: m.high = n.high+n.balance
        if n.base > m.base: m.base = n.base
        #m.close += n.close - n.open
        m.close = n.close+n.balance
        m.money += n.money
        m.balance = n.balance
    m_list.append( m )
    Node.objects.bulk_create( m_list )

    return HttpResponseRedirect('/chart/k/')


@login_required(login_url="/account/login/")
def bill_update(request):
    setattr(request.user, 'view', "bill_update")
    if 'data' not in request.FILES:
        messages.add_message(request, messages.ERROR, '请选择一个资金流水文件。')
        return HttpResponseRedirect("/")
    data = request.FILES['data'].read()
    try: data = data.decode('UTF-8')
    except:
        try: data = data.decode('GBK')
        except: pass

    bills = []

    today = timezone.now()
    p = re.compile("    *")
    for line in data.split("\n"):
        if not line.startswith(u'人民币'):
            continue
        if u"申购配号" in line:
            continue
        line = line.replace(u"申购返款", u"1     申购返款")
        b = Bill()
        vals = p.split(line)
        if vals[3] == u'---':
            vals = [''] + vals
            b.account = vals[14]
            b.id = ";".join([ str(b.user_id), b.account, vals[2] ])
            b.date = get_date(vals[2])
            b.stock_money = D(vals[5])
            b.balance = D(vals[6])
            b.name = vals[8]
            if b.stock_money > 0:
                b.type = Bill.TYPES['PUT']
            else:
                b.type = Bill.TYPES['GET']
        else:
            b.account = vals[14]
            b.id = ";".join([ str(b.user_id), b.account, vals[2] ])
            b.date = get_date(vals[2])
            b.stock_name = vals[1]
            b.stock_code = vals[13]
            b.stock_price = D(vals[3])
            b.stock_num = D(vals[4])
            b.stock_money = D(vals[5])
            b.balance = D(vals[6])
            b.name = vals[8]
            b.fee1 = D(vals[9])
            b.tax  = D(vals[10])
            b.fee2 = D(vals[11])
            b.fee3 = D(vals[12])
            if b.stock_money > 0:
                b.type = Bill.TYPES['SELL']
            else:
                b.type = Bill.TYPES['BUY']

            if len(b.stock_code) != 6:
                logging.error(line)
            # 特殊处理转债问题
            if b.stock_code == u'704016':
                b.stock_code = u'110023'
                if b.stock_money == 0:
                    b.stock_money = 0
                    b.stock_num = 1
        if b.date.date() > today.date():
            raise "not large than today"
        b.user = request.user
        b.save()
        bills.append( b )

    request.user.profile.is_outdate = 1
    request.user.profile.save()
    return HttpResponseRedirect("/chart/k/")
    #return render(request, 'www/html/bill/update.html', {'bills': bills})

@login_required(login_url="/account/login/")
def chart_k(request):
    setattr(request.user, 'view', "chart_k")
    if request.method == 'POST':
        return chart_build(request)
    linetype = request.GET.get('linetype', "0")
    nodes = request.user.node_set.filter(type=Node.TYPES['DAY']).order_by('date').all()
    return render(request, 'www/html/chart/k.html', {'nodes': nodes, 'linetype': linetype})

@login_required(login_url="/account/login/")
def chart_e(request):
    setattr(request.user, 'view', "chart_e")
    nodes = request.user.node_set.filter(type=Node.TYPES['MONTH']).order_by("-date").all()
    return render(request, 'www/html/chart/e.html', {'nodes': nodes})

def about(request):
    setattr(request.user, 'view', "about")
    return render(request, 'www/html/about.html')

def account_reg(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.add_message(request, messages.SUCCESS, '您已注册成功。')
            return HttpResponseRedirect('/analyse/')
    return render(request, 'www/html/account/reg.html', {'form': form})

