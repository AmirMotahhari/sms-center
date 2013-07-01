from django.conf.urls import patterns, include, url
from pyws.adapters._django import serve
from ws.smsws import server
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^api/(.*)',serve,{'server':server}),
    # Examples:
    # url(r'^$', 'ws.views.home', name='home'),
    # url(r'^ws/', include('ws.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
