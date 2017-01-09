#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.views.decorators.http import require_GET,require_POST
from django.views.decorators.http import require_http_methods
from wsgiref.simple_server import make_server

@require_http_methods(('POST','GET'))
def v_index(req):
    if req.method == 'GET':
        rsp = """
            <h1>限制http方法</h1>
            <form action="/" method="POST">
            <input type="text" name="nick" placeholder="请输入昵称">
            <input type="submit" value="进入聊天室">
            </form>

             """

        return HttpResponse(rsp)
    else:
        nickname = req.POST['nick']
        return HttpResponse('<h1>%s</h1>' % nickname)

urlpatterns = [
    url(r'^$',v_index),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi)

print('start serving at 0.0.0.0:7000')

httpd.serve_forever()
