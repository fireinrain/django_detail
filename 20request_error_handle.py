#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import (url,
handler400,handler403,handler404,handler500)
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def ez_404(req):
    return HttpResponse('<h1>寻人启示</h1>')

def ez_500(req):
    return HttpResponse('<h1>崩了：（</h1>')

# handler404
# 当用户请求的URL地址未找到（对应状态码：404）时，
# Django框架将调用handler404 变量指向的视图，
# 它的默认值为'django.views.defaults.page_not_found'
handler404 = ez_404
handler500 = ez_500

def v_index(req):
    rsp = """
        <h1>定制错误处理</h1>
        <p><a href="/787878/565656/343434/121212/">触发404错误</a></p>
        <p><a href="/demo_500/">触发500错误</a></p>

        """
    return HttpResponse(rsp)

def v_500(req):
    raise Exception('故意的')
    return HttpResponse('')

urlpatterns = [
    url(r'^$', v_index),
    url(r'^demo_500/$', v_500),
]


settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = False
settings.ALLOWED_HOSTS = [ '*',]

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi_app)
print('starting serving at 7000...')
httpd.serve_forever()