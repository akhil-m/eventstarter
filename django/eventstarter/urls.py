from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from et.apiviews import event_list, event_detail
from et.views import create_event, thanks
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/events/$', event_list),
    url(r'^api/events/(?P<pk>[0-9]+)/$', event_detail),
    url(r'^events/create/$', create_event),
    url(r'^events/thanks/$', thanks),
)
