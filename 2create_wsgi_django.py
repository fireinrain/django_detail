#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang


from django.conf import settings
from django.core.wsgi import get_wsgi_application
# from wsgiref.simple_server import make_server

settings.configure()
settings.DEBUG = True

wsgi_app = get_wsgi_application()
# httpd = make_server('0.0.0.0', 8000, wsgi_app)
# print('start server')
# httpd.serve_forever()
print(wsgi_app)