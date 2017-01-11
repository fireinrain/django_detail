#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# 异常中间件
import sys,os

from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server


class A_middleware():

    def process_exception(self,request,exception):
        print("A_view is process")

        return HttpResponse("出现异常了")


class B_middleware():
    def process_exception(self, request, exception):
        print("B_view is process")

        return None


class C_middleware(object):
    def process_exception(self, request, exception):
        print("C_view is process")

        return None


def v_index(req):
    rsp = "this is a page that raise an error"
    raise Exception("raise an erron here")
    return HttpResponse(rsp)

urlpatterns = [
    url(r'^$',v_index),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=('__main__.A_middleware','__main__.B_middleware','__main__.C_middleware')


# output in console
# C_view is process
# B_view is process
# A_view is process
#
# 如果有多个异常中间件，那么Django将按照它们在配置对象的MIDDLEWARE_CLASSES 属性中注册的逆序执行。
# 例如上中，我们定义了三个异常中间件A、B和C。
# 那么， 当视图函数出现异常时，Django将先执行C，如果C返回None，那么继续执行B，如果B也返回None， 那么继续执行A。
#
wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()
