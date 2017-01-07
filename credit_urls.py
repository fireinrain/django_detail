
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
