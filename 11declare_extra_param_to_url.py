#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
#可以向url（）中传入附加参数
#传入的附加参数会在调用试图函数时传入函数


import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server


def v_index(req):
    rsp = '''
        <h1>Extra Parameters</h1>
        <ul>
            <li><a href="/blog/2014/">blog archive of 2014</a></li>
        </ul>
    '''
    return HttpResponse(rsp)


def v_year_archive(req, **kwargs):
    year = kwargs.pop('year')
    foo = kwargs.pop('foo')
    rsp = 'blog archive of year %s, foo:%s' % (year, foo)
    return HttpResponse(rsp)


urlpatterns = [
    url(r'^$', v_index),
    url(r'^blog/(?P<year>[0-9]{4})/$', v_year_archive, {'foo': 'bar'}),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0', 8000, wsgi_app)
print('starting serving...')
httpd.serve_forever()