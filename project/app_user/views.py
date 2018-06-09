# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Logininfo

# Create your views here.

#登录页面，放在/app_user/login.html
def login(request):
    return render(request,'app_user/login.html')

#登录验证，返回1表示登录成功，返回0表示请求错误，返回-1表示登录失败
def loginVerify(request):
    if request.method == "POST":
        login_state = {}
        user_name = request.POST.get("username",None)
        user_pass = request.POST.get("password",None)
        db_info = Logininfo.objects.get(username=user_name)

        if db_info.password == user_pass:
            return HttpResponse('1')
        else:
            return HttpResponse('-1')
    else:
        return HttpResponse('0')

#主页，放在/app_user/index.html
def index(request):
    userlist = Logininfo.objects.all()
    context = {'user_list':userlist}
    return render(request, 'app_user/index.html',context)

#注册
def insert(request):
    if request.method == "POST":
        user_name = request.POST.get("username",None)
        user_pass = request.POST.get("password",None)
        Logininfo.objects.create(username=user_name,password=user_pass)
        Logininfo.save()
    return render(request,'insert.html')