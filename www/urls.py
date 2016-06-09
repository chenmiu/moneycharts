#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from www import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^analyse/$', views.analyse),
    url(r'^about/$', views.about),

    url(r'^bill/update/$', views.bill_update),

    url(r'^chart/build/$', views.chart_build),
    url(r'^chart/k/$', views.chart_k),
    url(r'^chart/e/$', views.chart_e),

    url(r'^stock/list/$', views.stock_list),

    url(r'^account/reg/$', views.account_reg),
    url(r'^account/edit/$', views.index),
    url(r'^account/login/$', login, {'template_name': "www/html/account/login.html"}),
    url(r'^account/logout/$', logout, {'template_name': "www/html/index.html"}),
    url(r'^account/profile/$', views.index),
    url(r'^accounts/profile/$', views.index),
]
