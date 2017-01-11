#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# 基于类的视图


from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

import sys

class Class_view():
    def __call__(self, req,**kwargs):
        return HttpResponse('Hi i am from a class'+kwargs['id'])


urlpatterns = [
    url(r'^report/(?P<id>\d+)/$',Class_view()),
]
settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()
