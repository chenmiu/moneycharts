#!/usr/bin/python
#-*- coding: UTF-8 -*-

import logging, re, time
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from datetime import datetime, timedelta
from www.models import *
from www.codelist import Codes


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'www/html/index.html', {'pid': 'index'})
    return render(request, 'www/html/profile.html', {'pid': 'index'})


@login_required
def chart_k(request):
    nodes = request.user.node_set.filter(type=Node.TYPES['DAY']).order_by('date').all()
    return render(request, 'www/html/k.html', {'pid': 'chart_k', 'nodes': nodes})

@login_required
def stock_list(request):
    def Name(code):
        return Codes.get(code.strip(), code)
    stocks = eval(request.user.profile.stocks_raw)
    current = [ (Name(code), s) for code,s in stocks.items() if s['num'] > 0 or code == '' ]
    history = [ (Name(code), s) for code,s in stocks.items() if s['num'] == 0 and code != '' ]
    history.sort( lambda x,y: cmp(y[1]['money'], x[1]['money']) )
    return render(request, 'www/html/stock_list.html', {'pid': 'stock_list', 'current': current, 'history': history})


@login_required
def build(request):
    def Sum(stocks):
        val = 0
        for s in stocks.values():
            val += s['money']
        return val

    profile = request.user.profile
    request.user.node_set.all().delete()

    bills = request.user.bill_set.order_by('date').all()
    idx = 0
    day = bills[idx].date
    oneday = timedelta(days=1)
    today = bills[len(bills)-1].date
    n = Node(type=Node.TYPES['DAY'], open=profile.base, date=day, user=request.user)
    n.low = n.high = n.close = n.open

    stocks = {}
    base = profile.base
    free = profile.base
    while idx < len(bills) and day <= today:
        b = bills[idx]
        if n.date.date() == b.date.date():
            n.date = b.date
            s = stocks.get(b.stock_code, {'num': 0, 'money': 0})
            s['num'] += b.stock_num
            s['money'] += b.stock_money
            free += b.stock_money
            if b.type == b.TYPES['PUT']:
                base += b.stock_money
            elif b.type == b.TYPES['GET']:
                base += b.stock_money
            stocks[b.stock_code] = s
            idx += 1
        else:
            n.close = free + Sum(stocks)
            if n.open == n.close:
                n.open -= n.close/20
            n.high = n.close
            n.base = base
            n.low = free
            n.save()
            day += oneday
            n = Node(type=Node.TYPES['DAY'], open=n.close, date=day, user=request.user)
            n.low = n.high = n.close = n.open

    profile.stocks_num = 0
    for s in stocks.values():
        if s['num'] > 0:
            profile.stocks_num += 1
    profile.stocks_raw = repr(stocks)
    profile.base = base
    profile.free = free
    profile.save()
    return render(request, 'www/html/import.html', {'bills': bills})


@login_required
def import_bill(request):
    def get_date(value):
        return datetime.strptime(value[0:8], "%Y%m%d")

    def D(val):
        if val == u'---':
            return Decimal(0)
        return Decimal(val)

    files = request.FILES
    f = files['data']
    data = f.read()
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
        b = Bill()
        vals = p.split(line)
        if vals[3] == u'---':
            vals = [''] + vals
            b.id = vals[2]
            b.date = get_date(vals[2])
            b.stock_money = D(vals[5])
            b.balance = D(vals[6])
            b.name = vals[8]
            if b.stock_money > 0:
                b.type = Bill.TYPES['PUT']
            else:
                b.type = Bill.TYPES['GET']
        else:
            b.id = vals[2]
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
            b.account = vals[14]
            if b.stock_money > 0:
                b.type = Bill.TYPES['BUY']
            else:
                b.type = Bill.TYPES['SELL']
        if b.date.date() > today.date():
            raise "not large than today"
        b.user = request.user
        b.save()
        bills.append( b )

    return render(request, 'www/html/import.html', {'bills': bills})

