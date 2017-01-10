#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,HttpResponseNotFound
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_index(req):
    rsp = """
            <form action="/login/" method="post">

    <input type="text" name="user">

    <input type="password" name="pwd">
    <input type="submit" value="登录">
    </form>

            """
    return HttpResponse(rsp)

def v_lgin(req):
    user = req.POST['user']
    pwd = req.POST['pwd']
    return HttpResponse('user:%s,pass:%s' % (user,pwd))

urlpatterns = [
    url(r'^$',v_index),
    url(r'^login/$',v_lgin),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('start serving at 8000')
httpd.serve_forever()