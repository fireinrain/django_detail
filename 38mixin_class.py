#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# Mixin是一种编程理念，用来将代码注入到一个类里，使被注入的类具备Mixin所 实现的功能。
# 当需要在多个类之间复用代码时，将这部分代码抽出来定义一个新的类，就构成 一个Mixin。
# Mixin通常作为父类，使继承类具备了它实现的功能。

import sys,os

from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

class LogMixin():
    def info(self,txt):
        print('info:%s' % txt)

    def warn(self,txt):
        print('warning:%s' % txt)

    def error(self,txt):
        print('error:%s' % txt)


class LayoutMixin():
    def get_header(self):
        return """
                  <div style="height:40px;background:gray;color:white;">
                <h1>Header</h1>
            </div>
            """
    def get_footer(self):
        return """
                  <div style="height:40px;background:gray;color:white;">
                <h1>footer</h1>
            </div>

                """

class Index_view(LayoutMixin,LogMixin,View):
    def get(self,req):
        self.info('a man is visiting %s' % req.path)
        body = """
                 %s
            <div><a href="/about/">about us</a></div>
            <p>There is nothing special about mixin, but a concept only.</p>
            %s


            """ %  (self.get_header(),self.get_footer())
        return HttpResponse(body)

class About_view(LogMixin,LayoutMixin,View):
    def get(self,req):
        self.warn('a child is visiting %s' % req.path)
        body = """
                %s
                <p>we are happy everyday.</p>
                %s
                """ % (self.get_header(), self.get_footer())

        return HttpResponse(body)

urlpatterns = [
    url(r'^$',Index_view.as_view()),
    url(r'^about/$',About_view.as_view()),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()