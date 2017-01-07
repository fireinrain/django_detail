#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang


import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server


def v_index(req):
    rsp = '''
        <h1>URL Patterns</h1>
        <ul>
            <li><a href="/articles/">default archive</a></li>
            <li><a href="/articles/2003/">special case 2003</a></li>
            <li><a href="/articles/2004/">year archive of 2004</a></li>
            <li><a href="/articles/2004/08/">month archive of 2004-08</a></li>
            <li><a href="/articles/2004/08/23/">article detail of 2004-08-03</a></li>
        </ul>
    '''
    return HttpResponse(rsp)


def v_special_case_2003(req):
    return HttpResponse('special case 2003')


def v_year_archive(req, year):
    rsp = 'year archive of %s' % year
    return HttpResponse(rsp)


def v_month_archive(req, year='2013', month='07'):
    rsp = 'month archive of %s-%s' % (year, month)
    return HttpResponse(rsp)


def v_article_detail(req, year, month, day):
    rsp = 'article detail of %s-%s-%s' % (year, month, day)
    return HttpResponse(rsp)


urlpatterns = [
    url(r'^$', v_index),
    url(r'^articles/$', v_month_archive),
    url(r'^articles/2003/$', v_special_case_2003),
    url(r'^articles/([0-9]{4})/$', v_year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', v_month_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$', v_article_detail),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0', 80, wsgi_app)
print('starting serving...')
httpd.serve_forever()