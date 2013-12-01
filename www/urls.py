#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', 'www.views.index'),
    url(r'^analyse/$', 'www.views.analyse'),
    url(r'^about/$', 'www.views.about'),

    url(r'^bill/update/$', 'www.views.bill_update'),

    url(r'^chart/build/$', 'www.views.chart_build'),
    url(r'^chart/k/$', 'www.views.chart_k'),
    url(r'^chart/e/$', 'www.views.chart_e'),

    url(r'^stock/list/$', 'www.views.stock_list'),

    url(r'^account/reg/$', 'www.views.index'),
    url(r'^account/edit/$', 'www.views.index'),
    url(r'^account/login/$', login, {'template_name': "www/html/account/login.html"}),
    url(r'^account/logout/$', logout, {'template_name': "www/html/account/logout.html"}),
    url(r'^account/profile/$', 'www.views.index'),
    url(r'^accounts/profile/$', 'www.views.index'),
)
