#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang
from django.conf import settings
from django.conf.urls import url,include
from django.core.urlresolvers import RegexURLResolver

# 初始化django默认设置
settings.configure()
settings.DEBUG = True


def init_urls_module(fname,cnt):
    import os
    try:
        with open(fname,'w') as f:
            f.write(cnt)
    except:
        pass


init_urls_module('root_urls.py','''

from django.conf.urls import url,include
def v_index(req):
    return 'from index'

def v_about(req):
    return 'from about'

urlpatterns = [
    url(r'^$', v_index),
    url(r'^about/$',v_about),
    url(r'^credit/', include('credit_urls')),
    url(r'^mail/',include('mail_urls')),
]
'''


)

init_urls_module('credit_urls.py','''
from django.conf.urls import url
def v_report(req,id="1"):
    return 'from report %s' % id

def v_charge(req):
    return 'from charge'
urlpatterns = [
    url(r'^report/$', v_report),
    url(r'^report/(?P<id>[0-9]+)/$', v_report),
    url(r'^charge/$', v_charge),
]
''')

init_urls_module('mail_urls.py',
'''
from django.conf.urls import url

def mail_private(req):
    return "this is from module mail"

urlpatterns = [
    url(r'^private/',mail_private)
]


'''

)

# 路由拆分
resolver = RegexURLResolver(r'^/','root_urls')

# 测试路由
test_urls = [
    '/', '/about/', '/credit/', '/credit/report/',
    '/credit/report/123/', '/credit/charge/','/mail/private/',
]

for url in test_urls:
    try:
        #路由解析
        view_func,args,kwargs = resolver.resolve(url)
        print('found match for %s calling...' % url )
        print(view_func(None,*args,**kwargs))
    except:
        print('no match for %s' % url)