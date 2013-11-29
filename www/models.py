# -*- coding: UTF-8 -*-
from django.db import models
from decimal import Decimal
from datetime import datetime

# Create your models here.
class User(models.Model):
    email       = models.EmailField(primary_key=True, unique=True, max_length=128)
    password    = models.CharField(max_length=128, default="")
    stocks      = models.IntegerField(default=Decimal(0))
    capital     = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))

class Bill(models.Model):
    TYPES = {
            'BUY':  0,
            'SELL': 1,
            'PUT':  2,
            'GET':  3,
            }

    id      = models.CharField(primary_key=True, unique=True, max_length=16, default="")
    type    = models.IntegerField(default=Decimal(0))
    name    = models.CharField(max_length=128, default="")        # 业务名
    date    = models.DateTimeField()
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    tax     = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee1    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee2    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    fee3    = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    account = models.CharField(max_length=128, default="")
    stock_name  = models.CharField(max_length=16, default="")        # 股票名
    stock_code  = models.CharField(max_length=16, default="")        # 股票代码
    stock_price = models.IntegerField(default=Decimal(0))
    stock_num   = models.IntegerField(default=Decimal(0))
    stock_money = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    user    = models.ForeignKey("User")

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
    capital = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0))
    user    = models.ForeignKey("User")
    unique_together = ( ('user', 'type, date'), )

