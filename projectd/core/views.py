# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from allauth import app_settings
from allauth.account.forms import SignupForm, LoginForm



class IndexView(TemplateView):
    template_name = "pages/index.html"
    form_class1 = SignupForm
    form_class2 = LoginForm

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context.update({
            'signup_form': self.form_class1,
            'loging_form': self.form_class2,
        })
        return context
