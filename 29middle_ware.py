#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# 中间件
# 视图函数适合实现业务功能的纵向切割，我们可以将不同的业务逻辑，
#  分解到不同的视图函数中去实现。
#
# 但并不是所有的代码都适合放在视图函数中实现。
# 例如，我们希望通过 检测请求对象是否携带了指定的cookie来判断用户是否为第一次访问，
# 并 将第一次访问的用户重定向到一个新手页面。
#
# 显然，在每个视图函数里都去重复这一功能不算一个好的设计。
# 更好的 方案是在请求分发之前，框架提供一个接口以便应用程序注入代码，拦截 请求对象并进行必要的处理。

import sys,random
from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server


# 实现一个中间件类，实现相应的方法即可
class FreshmanMiddleware():
    def process_request(self,req):
        if 'vid' in req.COOKIES or req.path == '/freshman/':
            return None
        else:
            return HttpResponseRedirect('/freshman/')

def v_index(req):
    return HttpResponse('you will not see this page for your first visit')

def v_freshman(req):
    rsp = HttpResponse('welcome,freshman! visit<a href="/">home page</a>now!')
    rsp.set_cookie('vid',random.random())
    return rsp


urlpatterns = [
    url(r'^$',v_index),
    url(r'^freshman/$',v_freshman),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.USE_X_FORWARD_HOST = True
settings.MIDDLEWARE_CLASSES = ('__main__.FreshmanMiddleware',)

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()

