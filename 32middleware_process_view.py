#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# 视图中间件

import sys,os
from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse,HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server



class A_middleware():

    def process_view(self,request,view_func,view_args,view_kwargs):
        print("A_view is process")
        # if request.path == '/report/123/':    #如果访问的是该路由，则返回404
        #     return HttpResponseNotFound(content=b"404")
        return None


class B_middleware():

    def process_view(self,request,view_func,view_args,view_kwargs):
        print("B_view is process")
        return None


class C_middleware(object):

    def process_view(self,request,view_func,view_args,view_kwargs):
        print("C_view is process")
        return None


def v_index(req):
    body = 'this is not the point.<a href="/report/123/">report#123</a>'
    return HttpResponse(body)

def v_report(req,id):
    body = 'report %s' % id
    return HttpResponse(body)

urlpatterns = [
    url(r'^$',v_index),
    url(r'report/(\d+)/$',v_report),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=('__main__.A_middleware','__main__.B_middleware','__main__.C_middleware')

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()
