from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect,HttpResponse
from mainsite.forms import UserForm,CustomerForm
from mainsite.models import User
from django.template import loader
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
# Create your views here.

#登录 Diango验证
def login_view(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user =  authenticate(request,username= username,password= password)
            if user is not None and user.is_active:
                login(request, user)
                request.session['username'] = username
                messages.add_message(request, messages.INFO, 'Hello world.')
                return redirect('index')
                #return HttpResponseRedirect('index')
                #template = loader.get_template('mainsite/index.html')
                #context={'username':username}
                #return HttpResponse(template.render(context,request))
            else:
                return HttpResponseRedirect('login')
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
                #return HttpResponseRedirect('login')
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
    template = loader.get_template('mainsite/logout.html')
    return HttpResponse(template.render({}, request))

@login_required(redirect_field_name='next',login_url='login')
def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    else:
        template = loader.get_template('mainsite/index.html')
        #username = request.session['username']
        #username = request.session.keys()
        username = request.session.get('username',None)
        #storage=messages.get_messages(request)
        return HttpResponse(template.render({'username':username,},request))
#@csrf_protect
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单元素
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            #user.email = email
            user.save()

            return redirect('login')
            #return render_to_response('mainsite/login.html',{})

    else:
        uf = UserForm()
    template = loader.get_template('mainsite/register.html')
    context = {'uf': uf, }
    #return render(request, template, context)
    return HttpResponse(template.render(context, request))
    #return render_to_response('mainsite/register.html',{'uf':uf})


@login_required(redirect_field_name='next',login_url='login')
def cust_add(request):
    if request.method == 'POST':
        cf = CustomerForm(request.POST)
    else:
        cf = CustomerForm()
    template = loader.get_template('mainsite/customer-add.html')
    context = {'cf': cf, }
    return HttpResponse(template.render(context, request))