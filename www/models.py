#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.db import models
from decimal import Decimal
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User)
    stocks_num  = models.IntegerField(default=Decimal(0))
    stocks_raw  = models.TextField(default="")
    stocks_val  = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    base        = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    free        = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    is_outdate  = models.IntegerField(default=0)


class Bill(models.Model):
    TYPES = {
            'BUY':  0,
            'SELL': 1,
            'PUT':  2,
            'GET':  3,
            }

    id      = models.CharField(primary_key=True, unique=True, max_length=16, default="")
    type    = models.IntegerField(default=Decimal(0))

    # 业务名、日期、余额
    name    = models.CharField(max_length=128, default="")
    date    = models.DateTimeField()
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))

    # 印花税、手续费、过户费、结算费
    tax     = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee1    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee2    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee3    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))

    # 股票名称、代码、价格、数量、总价
    stock_name  = models.CharField(max_length=16, default="")
    stock_code  = models.CharField(max_length=16, default="")
    stock_price = models.IntegerField(default=Decimal(0))
    stock_num   = models.IntegerField(default=Decimal(0))
    stock_money = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))

    # 用户、账户ID
    user    = models.ForeignKey(User)
    account = models.CharField(max_length=128, default="")

class Node(models.Model):
    TYPES = {
            'DAY':      0,
            'WEEK':     1,
            'MONTH':    2,
            }
    type    = models.IntegerField(default=0)
    date    = models.DateTimeField(default=datetime.now())
    low     = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    high    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    open    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    close   = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    base    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    user    = models.ForeignKey(User)

    class Meta:
        unique_together = ( ('user', 'type', 'date'), )

class SimpleCache(models.Model):
    key = models.CharField(primary_key=True, max_length="256")
    val = models.TextField(default="")

