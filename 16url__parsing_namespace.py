#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
# 路由的命名空间

import sys

from django.conf import settings
from django.conf.urls import url,include
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.core.urlresolvers import reverse

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
        <li><a href="%s">收件箱</a></li>
        <li><a href="%s">发件箱</a></li>
    </ul>
</ul>



    """ % (reverse('r_inbox'),reverse('r_outbox'))
    return HttpResponse(body)


def v_report_income_year(req,year):
    body = "<h1>%s 年度收入报表</h1>" % year
    return HttpResponse(body)


def v_report_income_month(req,year,month):
    body = "<h1>%s-%s 月度收入报表</h1>" % (year,month)
    return HttpResponse(body)


# 使用匿名参数分组
# report_urlpatterns = [
#     url(r'^$',v_report_index,name='r_index'),
#     url(r'^income/([0-9]{4})/$',v_report_income_year,name='r_income_year'),
#     url(r'^income/([0-9]{4})/([0-9]{2})/$',v_report_income_month,name='r_income_month'),
# ]

# 使用命名参数分组
report_urlpatterns = [
    url(r'^$',v_report_index,name='r_index'),
    url(r'^income/(?P<year>[0-9]{4})/$',v_report_income_year,name='r_income_year'),
    url(r'^income/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',v_report_income_month,name='r_income_month'),
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
    url(r'^$',v_mail_index,name='r_index'),
    url(r'^inbox/$',v_mail_inbox,name='r_inbox'),
    url(r'^outbox/$',v_mail_outbox,name='r_outbox'),
]


def v_index(req):
    body = """
        <h1>liuzhaoyang‘s system</h1>

<ul>
    <li>最近更新</li>
    <ul>
        <li><a href="%s">2015年度收入报表</a></li>
        <li><a href="%s">2015-10月度收入报表</a></li>
    </ul>
    <li><a href="%s">全部报表</a></li>
</ul>



    """ % (reverse('report:r_income_year',kwargs={'year':'2015'}),reverse('report:r_income_month',kwargs={'year':'2015','month':'10'}),reverse('report:r_index'))
    return HttpResponse(body)

urlpatterns = [
    url(r'^$',v_index),
    url(r'^report/',include(report_urlpatterns,namespace='report')),
    url(r'^email/',include(mail_urlpatterns,namespace='mail')),

]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi_app)

print('start serving at 0.0.0.0:7000')
print(reverse('mail:r_index'))
print(reverse('report:r_index'))
httpd.serve_forever()

