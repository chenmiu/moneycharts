# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from www.models import *
import logging, re, time
from decimal import Decimal
from datetime import datetime, timedelta

def index(request):
    user = get_object_or_404(User, pk="talebook@foxmail.com")
    return render(request, 'www/html/index.html', {'user': user})

def login(request):
    return HttpResponse("login")

def k_day(request):
    user = get_object_or_404(User, pk="talebook@foxmail.com")
    nodes = user.node_set.filter(type=Node.TYPES['DAY']).order_by('date').all()
    return render(request, 'www/html/k.html', {'nodes': nodes})

def build(request):
    user = get_object_or_404(User, pk='talebook@foxmail.com')
    bills = user.bill_set.order_by('date').all()
    idx = 0
    day = bills[idx].date
    oneday = timedelta(days=1)
    n = Node(type=Node.TYPES['DAY'], open=user.capital, date=day, user=user)
    n.low = n.high = n.close = n.open
    while idx != len(bills):
        b = bills[idx]
        if n.date == b.date:
            n.date = b.date
            n.low += b.stock_money
            n.high += b.stock_money
            n.close += b.stock_money
            idx += 1
        else:
            n.save()
            day += oneday
            n = Node(type=Node.TYPES['DAY'], open=n.close, date=day, user=user)
            n.low = n.high = n.close = n.open

    return render(request, 'www/html/import.html', {'bills': bills})

def get_date(value):
    return datetime.strptime(value[0:8], "%Y%m%d")

def import_bill(request):
    files = request.FILES
    f = files['data']
    data = f.read()
    try: data = data.decode('UTF-8')
    except:
        try: data = data.decode('GBK')
        except: pass

    user = get_object_or_404(User, pk='talebook@foxmail.com')
    bills = []

    p = re.compile("    *")
    for line in data.split("\n"):
        if not line.startswith(u'人民币'):
            continue
        b = Bill()
        vals = p.split(line)
        if '---' in line:
            vals = [''] + vals
            b.id = vals[2]
            b.date = get_date(vals[2])
            b.stock_money = Decimal(vals[5])
            b.balance = Decimal(vals[6])
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
            b.stock_price = Decimal(vals[3])
            b.stock_num = Decimal(vals[4])
            b.stock_money = Decimal(vals[5])
            b.balance = Decimal(vals[6])
            b.name = vals[8]
            b.fee1 = Decimal(vals[9])
            b.tax  = Decimal(vals[10])
            b.fee2 = Decimal(vals[11])
            b.fee3 = Decimal(vals[12])
            b.account = vals[14]
            if b.stock_money > 0:
                b.type = Bill.TYPES['BUY']
            else:
                b.type = Bill.TYPES['SELL']
        b.user = user
        b.save()
        bills.append( b )

    return render(request, 'www/html/import.html', {'bills': bills})

