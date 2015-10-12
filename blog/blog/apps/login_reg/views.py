#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
import hashlib
from blog.apps.login_reg.models import userInfo
from django.db import connection
#登陆的页面展示
def login(request):
    #使用post方式提交时需要注意
    #1,在form表单中需要有{% csrf_token %}
    #2,在输出模板后面需要带context_instance=RequestContext(request)，该方法需要库RequestContext
    #3,post提交的action后面记得带反斜杠,/
    return render(request, 'login.html',context_instance=RequestContext(request));


#登陆过程操作
def doLogin(request):
    #先得到从页面传过来的post参数,并且对密码进行简单的MD5加密
    username = request.POST['username'];
    password = request.POST['password'];
    md5 = hashlib.md5();
    md5.update(password);
    true_pass = md5.hexdigest();

    #然后开始查数据库进行验证
    user = userInfo.objects.filter(username = username,password = true_pass);

    #如果有值，代表存在
    if user:
        return HttpResponse('登陆成功');
    else:
        return HttpResponse('你的账号密码错误');


#用户注册
def reg(request):
    #和登陆大同小异
    return render(request,'reg.html',context_instance=RequestContext(request));

def doReg(request):
    #同样，先获取提交过来的表单并且md5
    username = request.POST['username'];
    password = request.POST['password'];
    md5 = hashlib.md5();
    md5.update(password);
    true_pass = md5.hexdigest();

    #然后进行插入数据库操作
    user = userInfo.objects.create(username=username,password=true_pass);
    if user:
        return render(request,'regSuccess.html',{'username':username});
    else:
        return HttpResponse('reg error');
