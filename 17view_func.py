#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.views.decorators.http import require_GET,require_POST
from wsgiref.simple_server import make_server

@require_POST
def v_index(req):
    print(req.method)
    rsp = HttpResponse('啊哈')
    rsp.set_cookie('user','liuzhaoyang')
    return rsp

urlpatterns = [
    url(r'^$',v_index),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi)

print('start serving at 0.0.0.0:7000')
httpd.serve_forever()