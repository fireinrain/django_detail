#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_index(req):
    return HttpResponseRedirect('/hello/')

def v_hello(req):
    # return HttpResponseForbidden('liuzhaoyang is here')
    return HttpResponse('hahah')
urlpatterns = [
    url(r'^$',v_index),
    url(r'^hello/$',v_hello),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()
settings.USE_X_FORWARDED_HOST = True

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi_app)
print('start serving at 7000')
httpd.serve_forever()