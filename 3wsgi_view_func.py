#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest,HttpResponse

settings.configure()
settings.DEBUG = True

wsgi_app = get_wsgi_application()

def v_index(request):
    return HttpResponse('hello,liuzhaoyang')

req = HttpRequest()
print(v_index(req))

