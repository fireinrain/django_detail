#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from django.conf import settings
from django.conf.urls import url
from django.views import static
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server
import sys,os

os.system('echo "12345678987654321" > 1.txt')
def v_index(req):
    rsp = """
        <h1>preset view function</h1>
        <ul>
            <li><a href="lib/1.txt/">static.server</a></li>
        </ul>

        """
    return HttpResponse(rsp)

urlpatterns = [
    url(r'^$',v_index),
    url(r'^lib/(.*)/$',static.serve,{'document_root':os.path.dirname(os.path.abspath(sys.argv[0]))},name='static'),
]



settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi)

print('start serving at 0.0.0.0:7000')

httpd.serve_forever()