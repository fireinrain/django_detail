#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url,include
from django.core.urlresolvers import RegexURLResolver
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server
from django.http import HttpResponse

settings.configure()
settings.DEBUG = True

wsgi_app = get_wsgi_application()

def v_index(req):
    body = """
        <h1>Navigation</h1>
<ul>
    <li><a href="/about/">about</a></li>
    <li>credit</li>
    <ul>
        <li><a href="/credit/report/">default report</a></li>
        <li><a href="/credit/report/7878/">report #7878</a></li>
        <li><a href="/credit/charge/">charge detail</a></li>
    </ul>
    <li><a href="/a/b/c/d/e/f/g/">trigger an exception</a></li>
</ul>


    """
    return HttpResponse(body)

def v_about(req):
    return HttpResponse('from about')

def v_report_index(req):
    body = '''
        <h1>reports</h1>
        <ul>
            <li><a href="credit/report/">default report</a></li>
            <li><a href="credit/report/7878/">report #7878</a></li>
            <li><a href="credit/charge/">charge detail</a></li>
        </ul>
    '''
    return HttpResponse(body)

def v_report(req,id="1"):
    return HttpResponse('from report %s' % id)

def v_charge(req):
    return HttpResponse('from charge')

credit_urlpatterns = [
    url(r'^/$',v_report_index),
    url(r'^report/$',v_report),
    url(r'^report/(?P<id>[0-9])/$',v_report),
    url(r'^charge/$',v_charge),
]

urlpatterns = [
    url(r'^$',v_index),
    url(r'^about/$',v_about),
    url(r'^credit/',include(credit_urlpatterns)),
]

settings.ROOT_URLCONF = sys.modules[__name__]
# settings.ROOT_URLCONF = credit_urlpatterns       #wrong

httpd = make_server('0.0.0.0',8000,wsgi_app)
print('start serving...')
httpd.serve_forever()
