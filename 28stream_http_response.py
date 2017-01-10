#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
# 流式响应
# 经常性的，我们需要在视图函数中，从一个数据源读取数据，处理后再生成响应对象。
#
# 如果数据源是随时就绪的，通常我们一次性读取源数据、处理即可。
# 但有两种情况 并不适合采用一次读取的方案：
#
# 源数据非常大，比如一个相当大的XML文档，一次读进来服务器就DOWN掉了
# 源数据是流式的，不能当时就绪。比如从一个网络地址读取。
# Django的StreamingHttpResponse类就是用来处理这种用例的，
# 它接受一个可迭代 的对象作为参数，使用每次迭代返回的字符串，逐步生成响应
#
import sys, time
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, StreamingHttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server


def ez_generator():
    for i in range(10):
        yield "<div>line %d</div>" % i
        yield " " * 10240  # force browser to render
        time.sleep(1)
    yield '<div>done</div>'


def v_index(req):
    rsp = StreamingHttpResponse(ez_generator())
    return rsp


urlpatterns = [
    url(r'^$', v_index),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()