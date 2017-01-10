#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys,json
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse,HttpResponseNotFound
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_index(req):
    body = """
        <pre id="result"></pre>
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script>
            $(function(){
                $.ajax({
                    url : "/demo/",
                    method : "GET",
                    success : function(dt,st,xhr){
                        var headers = xhr.getAllResponseHeaders();
                        var ret = [headers,xhr.responseText].join("\\n")
                        $("#result").text(ret);
                    },
                    error : function(){}
                })
            })
 </script>


    """
    return HttpResponse(body)

def v_demo(req):
    rsp = HttpResponse()
    rsp.set_cookie('user','liuzhaoyang')
    for i in range(10):
        rsp.write('line %d\n' % i)
    rsp['HTTP_USER_AGENT'] = 'DVA love you'
    return rsp


urlpatterns = [
    url(r'^$',v_index),
    url(r'^demo/$',v_demo),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES=()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000..')
httpd.serve_forever()