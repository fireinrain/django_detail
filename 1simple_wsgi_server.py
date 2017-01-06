#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from wsgiref.simple_server import make_server


def wsgi_app(environ, start_response):
    from  pprint import pprint
    pprint(environ)
    start_response('200 OK', [('Context-Type', 'text/plain')])
    return 'this is a tiny wsgi app!'


httpd = make_server('0.0.0.0', 8000, wsgi_app)
print('start server')
httpd.serve_forever()