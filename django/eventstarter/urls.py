from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from et import apiviews, views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/events/$', apiviews.event_list),
    url(r'^api/events/(?P<pk>[0-9]+)/$', apiviews.event_details),
    url(r'^events/create/$', views.create_event),
    url(r'^events/(?P<pk>[0-9]+)/$', views.event_details),
)
