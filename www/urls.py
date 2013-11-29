from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'www.views.index'),
    url(r'^login/$', 'www.views.login'),
    url(r'^import/$', 'www.views.import_bill'),

    url(r'^chart/k/$', 'www.views.chart_k'),
    url(r'^stock/list/$', 'www.views.stock_list'),

    url(r'^build/$', 'www.views.build'),
)
