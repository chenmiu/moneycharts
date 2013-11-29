from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'www.views.index'),
    url(r'^/$', 'www.views.index'),
    url(r'^login/$', 'www.views.login'),
    url(r'^import/$', 'www.views.import_bill'),

    url(r'^k/day/$', 'www.views.k_day'),
    url(r'^k/week/$', 'www.views.index', name='home'),
    url(r'^k/month/$', 'www.views.index', name='home'),

    url(r'^build/$', 'www.views.build'),
)
