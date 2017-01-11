#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
# 预置视图基类

import sys,os

from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

class Base_view(View):
    title = "sth from a class view"
    def get(self,request):
        return HttpResponse(self.title)

urlpatterns = [
    url(r'^$',Base_view.as_view()),
]


settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()