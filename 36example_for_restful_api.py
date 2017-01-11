#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# rest api展示


from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server
import sys,json

repo = [
    {'name':'liuzhaoyang','tel':'787878'},
    {'name':'mayuyu','tel':'123456'},
]

class Test_view():
    def default_handler(self,req):
        return HttpResponse(status=405)

    def __call__(self, req,*args, **kwargs):
        handler = getattr(self,req.method.lower(),self.default_handler)
        return handler(req)

class Index_view(Test_view):
    def get(self,req):
        body = """

                <h1>REST API DEMO</h1>
            <a href="/user/">Get Users</a>
            <form action="/user/" method="POST">
                <input type="text" name="name" placeholder="名字">
                <input type="text" name="tel" placeholder="电话">
                <input type="submit" value="Create A New User">
            </form>

            """
        return HttpResponse(body)


class User_view(Test_view):
    def get(self,req):

        return HttpResponse(json.dumps(repo))
    def post(self,req):
        name = req.POST['name']
        tel = req.POST['tel']
        repo.append({'name':name,'tel':tel})
        body = 'created.go to <a href="/user/">user list</a>'
        return HttpResponse(body,status=201)

urlpatterns = [
    url(r'^$',Index_view()),
    url(r'user/$',User_view()),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()