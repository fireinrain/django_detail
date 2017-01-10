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
        <form action="/upload/" method="post" enctype="multipart/form-data">
    <input type="file" name="upload_file">

    <input type="submit" value="上传">
    </form>

        """
    return HttpResponse(rsp)

def v_upload(req):
    upload_file = req.FILES['upload_file']
    file_stream = upload_file.read()
    with open(upload_file.name,'wb') as file:
        file.write(file_stream)
    return HttpResponse('you have upload file:%s' % upload_file.name)

urlpatterns = [
    url(r'^$',v_index),
    url(r'^upload/$',v_upload),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi_app)
print('start serving at 7000')
httpd.serve_forever()