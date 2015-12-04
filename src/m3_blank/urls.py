# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from m3 import get_app_urlpatterns
import wsfactory.urls

from views import workspace_view
import users.urls


urlpatterns = patterns('',
    url(r'^$', workspace_view),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += users.urls.urlpatterns
urlpatterns += wsfactory.urls.urlpatterns
urlpatterns += get_app_urlpatterns()
urlpatterns += staticfiles_urlpatterns()