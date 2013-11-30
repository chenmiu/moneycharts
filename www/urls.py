#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'www.views.index'),
    url(r'^import/$', 'www.views.import_bill'),

    url(r'^chart/k/$', 'www.views.chart_k'),
    url(r'^chart/earn/$', 'www.views.chart_earn'),

    url(r'^stock/list/$', 'www.views.stock_list'),

    url(r'^build/$', 'www.views.build'),
    url(r'^stat/$', 'www.views.stat'),
    url(r'^about/$', 'www.views.stat'),

    url(r'^accounts/login/$', login, {'template_name': "www/html/login.html"}),
    url(r'^accounts/logout/$', logout, {'template_name': "www/html/logout.html"}),
    url(r'^accounts/profile/$', 'www.views.index'),
)
