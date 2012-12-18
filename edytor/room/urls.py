from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *


urlpatterns = patterns('room.views',     
    url(r'^(?P<room_id>\d+)/$', 'index'),
)
