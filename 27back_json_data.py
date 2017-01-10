#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang


import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,JsonResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_index(req):
    body = '<a href="/user/">GET /user/</a>'
    return HttpResponse(body)

repo_users = [
    {'name':'liuyag','tel':'1555'},
    {'name':'xiaoqian','tel':'1444'},
]

def v_user(req):
    return JsonResponse(repo_users,safe=False)


urlpatterns = [
    url(r'^$',v_index),
    url(r'^user/$',v_user),
]


settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()