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
    rsp = """
        <form id="test" >
    <input type="text" name="name" placeholder="联系名字">

    <input type="text" name="tel" placeholder="联系电话">
    <input type="submit" value="Ajax post">
    </form>
    <div id="status"></div>
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
<script>
                $(function(){
                    $("form#test").submit(function(){
                        var data = $("form#test").serializeArray();
                        var jsondata = {}
                        data.forEach(function(d){jsondata[d.name] = d.value});
                        $.ajax({
                            url : "/user/",
                            method : "POST",
                            data : JSON.stringify(jsondata),
                            contentType : "application/json;charset=UTF-8",
                            success : function(dt,er,xhr){
                                $("#status").text(dt);
                            },
                            error : function(){console.log('发生错误');}
                        });
                        return false;
                    });
                })
 </script>

        """
    return HttpResponse(rsp)

repo_users = []
def v_user(req):
    if req.method != 'POST':
        return HttpResponse(status=405)
    raw = req.body
    # req.body获取的是二进制的表单值
    # 需要使用decode变成字符串
    # 才可以使用json.dumps,转化为json数据格式
    user = json.loads(raw.decode('utf-8'))
    # print(user)
    repo_users.append(user)

    return HttpResponse(json.dumps(repo_users),status=201)


urlpatterns = [
    url(r'^$',v_index),
    url(r'^user/$',v_user),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES = ()

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',9000,wsgi_app)
print('start serving at 9000')
httpd.serve_forever()