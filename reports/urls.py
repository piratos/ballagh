__author__ = 'piratos'
from django.conf.urls import patterns, url

urlpatterns = patterns('reports.views',
                       url(r'^$', 'index'),
                       url(r'^stat', 'getstats'),
                       url(r'^addreport', 'add_report'),
                       url(r'^generate', 'gen_report'),
                       url(r'^getreport/(?P<i>\d+)', 'get_report'),
                       url(r'^vstat/$', 'stats'),
                       url(r'^getpdf/(?P<i>\d+)', 'gen_pdf'),
                       url(r'^support/(?P<i>\d+)', 'support'),
                       url(r'^nsupport/(?P<i>\d+)', 'nsupport'),
                       url(r'^printall', 'printall'),
                       url(r'^advices', 'advises'),
                       url(r'^adviceme', 'advise_me'),
                       url(r'^aboutus', 'aboutus'),
                       )