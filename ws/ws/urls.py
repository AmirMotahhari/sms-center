from django.conf.urls import patterns, include, url
from pyws.adapters._django import serve
from ws.smsws import server

urlpatterns = patterns('',
    url('^api/(.*)',serve,{'server':server}),
)
