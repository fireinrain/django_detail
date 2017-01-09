#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url,include
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def v_report_index(req):
    body = """
            <h1>统计报表</h1>
<ul>
    <li>收入报表</li>
    <ul>
        <li><a href="income/2012/">2012年度收入报表</a></li>
        <li><a href="income/2012/12/">2012-12月度收入报表</a></li>
    </ul>
    <li>个人邮箱</li>
    <ul>
        <li><a href="/email/inbox/">收件箱</a></li>
        <li><a href="/email/outbox/">发件箱</a></li>
    </ul>
</ul>



    """
    return HttpResponse(body)


def v_report_income_year(req,year):
    body = "<h1>%s 年度收入报表</h1>" % year
    return HttpResponse(body)


def v_report_income_month(req,year,month):
    body = "<h1>%s-%s 月度收入报表</h1>" % (year,month)
    return HttpResponse(body)

report_urlpatterns = [
    url(r'^$',v_report_index),
    url(r'^income/([0-9]{4})/$',v_report_income_year),
    url(r'^income/([0-9]{4})/([0-9]{2})/$',v_report_income_month),
]


def v_mail_index(req):
    body = '<h1>email box</h1>'
    return HttpResponse(body)


def v_mail_inbox(req):
    body = '<h1>email box收件箱</h1>'
    return HttpResponse(body)


def v_mail_outbox(req):
    body = '<h1>email box发件箱</h1>'
    return HttpResponse(body)

mail_urlpatterns = [
    url(r'^$',v_mail_index),
    url(r'^inbox/$',v_mail_inbox),
    url(r'^outbox/$',v_mail_outbox),
]


def v_index(req):
    return HttpResponse('<a href="/report/">查看报表</a>')

urlpatterns = [
    url(r'^$',v_index),
    url(r'^report/',include(report_urlpatterns)),
    url(r'^email/',include(mail_urlpatterns)),

]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',9000,wsgi_app)

print('start serving at 0.0.0.0:8000')
httpd.serve_forever()
