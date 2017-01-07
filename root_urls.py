

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
