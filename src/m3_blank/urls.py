# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from m3 import get_app_urlpatterns
from m3_ext import workspace
import wsfactory.urls

urlpatterns = patterns('',
    url(r'^$', workspace()),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)


urlpatterns += wsfactory.urls.urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += get_app_urlpatterns()


for p in urlpatterns:
    print p