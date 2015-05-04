# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class LoginView(TemplateView):
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['menu_item'] = [u'가사 올리기', u'가사 확인하기', u'콘티 만들기', u'콘티 내려받기']
        return context


class LoginProcessView(View):

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        c = {}
        Email = request.POST.get('user_email')
        Password = request.POST.get('user_password')
        return_string = "<p>Email : "+Email+"<br>PW : "+Password+" </p>"
        return HttpResponse(return_string, c)