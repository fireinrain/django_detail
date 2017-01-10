#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
# 提取http
# 报文头

import sys,json
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,HttpResponseNotFound
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_index(req):
    body = []
    body.append('<pre>')
    for key,value in req.META.items():
        body.append(key+' : '+str(value))
    body.append('</pre>')
    body = '\n'.join(body)
    print(body)
    return HttpResponse(body)

urlpatterns = [
    url(r'^$',v_index),
]


settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi_app)
print('start serving at 7000')
httpd.serve_forever()