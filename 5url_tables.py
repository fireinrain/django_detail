#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from django.conf import settings
from django.conf.urls import url
from django.core.urlresolvers import RegexURLResolver

settings.configure()
settings.DEBUG = True

def v_index(request):
    return "this is from index"

def v_news(request):
    return "this is from news"

def v_blogs(request):
    return "this is from blogs"

urlpatterns = [
    url(r'^$',v_index),
    url(r'^news/$',v_news),
    url(r'^blogs/$',v_blogs)
]
# 路由解析
for pattern in urlpatterns:
    match = pattern.resolve('news/')
    if match is None:
        print('not match')
    else:
        view,args,kwargs = match
        print(view(None))
