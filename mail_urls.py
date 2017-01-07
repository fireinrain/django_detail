
from django.conf.urls import url

def mail_private(req):
    return "this is from module mail"

urlpatterns = [
    url(r'^private/',mail_private)
]


