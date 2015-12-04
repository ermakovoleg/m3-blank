# coding: utf-8

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        return render(request, self.template_name, {'form': form})