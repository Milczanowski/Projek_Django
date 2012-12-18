from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'edytor.views.index'),
    url(r'^nowy_pokoj', 'edytor.views.nowy_pokoj'),
    # url(r'^edytor/', include('edytor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),     
    url(r'^room/', include('room.urls')),
)
