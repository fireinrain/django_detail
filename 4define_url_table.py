#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# wsgi服务器  python内置模块
from wsgiref.simple_server import make_server

# wsgi应用
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest,HttpResponse
from django.conf.urls import url

settings.configure()
settings.DEBUG = True

wsgi_app = get_wsgi_application()

def v_index(request):
    return HttpResponse('hello,this is define a url table')

def v_test(request):
    return HttpResponse('we are testing the url dispatch')

urlpatterns = [
    url(r'^$',v_index),
    url(r'^test/$',v_test)
]
# urlpattern =  url(r'^test/$',v_test)

settings.ROOT_URLCONF = sys.modules[__name__]
print(urlpatterns)
print(sys.modules[__name__])

# def v_about(req):pass
#
# urlpattern = url(r'^about/$',v_about)
# print(urlpattern.match('about/'))

httpd = make_server('0.0.0.0',8000,wsgi_app)
httpd.serve_forever()