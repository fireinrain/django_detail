#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang


# 中间件流水线



import sys,os
from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

class Mid_exec_timeline_Middleware():
    def __init__(self):pass
    # 请求中间件
    def process_request(self,request):
        print('请求中间件在工作')
        return None

    def process_view(self,request,view_func,*view_args,**view_kwargs):
        print('视图中间件在工作')
        return None

    def process_template_response(self,request,response):
        print('模板中间件在工作')
        return None

    def process_response(self,request,response):
        print('响应中间件在工作')
        return response

    def process_exception(self,request,exception):
        print('异常中间件在工作')
        return None


class Test_view(View):
    def get(self,req,*args,**kwargs):
        rsp = "this is not the point"
        return HttpResponse(rsp)

urlpatterns = [
    url(r'^$',Test_view.as_view(),name='test_view'),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]

settings.MIDDLEWARE_CLASSES = ('__main__.Mid_exec_timeline_Middleware',)

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()
