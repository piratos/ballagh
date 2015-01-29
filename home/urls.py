__author__ = 'piratos'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
                       url(r'^$', 'index'),
                       url(r'^article/(?P<i>\d+)/$', 'article'),
                       )