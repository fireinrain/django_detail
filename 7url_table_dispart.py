#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from django.conf import settings
from django.conf.urls import url,include
from django.core.urlresolvers import  RegexURLResolver

settings.configure()
settings.DEBUG = True

def v_index(req):
    return "from index"

def v_about(req):
    return "from about"

def v_report(req,id='1'):
    return "from report %s" % id

def v_charge(req):
    return "from change"

credit_urlpatterns = [
    url(r'^report/$',v_report),
    url(r'^reprt/(?P<id>[0-9]+)/$',v_report),
    url(r'^charge/$',v_charge)
]
urlpatterns = [
    url(r'^$',v_index),
    url(r'^about/$',v_about),
    url(r'^credit/',include(credit_urlpatterns)),
]

resolver =RegexURLResolver(r'^/',urlpatterns)
test_urls = ['/', '/about/', '/credit/', '/credit/report/',
 '/credit/report/123/', '/credit/charge/', ]
for url in test_urls:
    try:
        view, args, kwargs = resolver.resolve(url)
        print('found match for %s.calling...' % url)
        print(view(None, *args, **kwargs))
    except:
        print('no match for %s' % url)
