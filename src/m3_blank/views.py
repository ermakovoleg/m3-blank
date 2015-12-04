# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django import template as django_template
from django.conf import settings

from m3_ext.context_processors import DesktopProcessor


context_processors = (DesktopProcessor.process,)


def workspace_view(request):

    if not request.user.is_authenticated():
        return redirect('/login')

    context = django_template.RequestContext(
        request, {'DEBUG': settings.DEBUG},
        processors=context_processors)
    return render_to_response('m3_workspace.html', context)

