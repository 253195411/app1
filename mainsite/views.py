from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
from mainsite.models import User
from django.template import loader
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label = '用户名 :',max_length = 50)
    password = forms.CharField(label = '密码 :',widget = forms.PasswordInput())

#登录 Diango验证
def login_view(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user =  authenticate(request,username= username,password= password)
            if user is not None:
                login(request, user)
                return redirect('index')
                #return HttpResponseRedirect('index')
                #template = loader.get_template('mainsite/index.html')
                #context={'username':username}
                #return HttpResponse(template.render(context,request))
            else:
                return HttpResponseRedirect('')
                #template = loader.get_template('mainsite/login.html')
                #context = {'uf': uf, }
                #return HttpResponse(template.render(context, request))
    else:
        uf = UserForm()
    template = loader.get_template('mainsite/login.html')
    context = {'uf': uf, }
    return HttpResponse(template.render(context, request))

#登录
def login_view01(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #return render_to_response('mainsite/index.html',{'username':username})
                template = loader.get_template('mainsite/index.html')
                context={'username':username}
                return HttpResponse(template.render(context,request))
            else:
                #return HttpResponseRedirect('')
                template = loader.get_template('mainsite/login.html')
                context = {'uf': uf, }
                return HttpResponse(template.render(context, request))
    else:
        uf = UserForm()
    #return render_to_response('mainsite/login.html',{'uf':uf})
    template = loader.get_template('mainsite/login.html')
    context = {'uf': uf, }
    return HttpResponse(template.render(context, request))
#登出
def logout_view(request):
    logout(request)
    uf = UserForm()
    template = loader.get_template('mainsite/login.html')
    context = {'uf': uf, }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('mainsite/index.html')
    return HttpResponse(template.render({},request))