__author__='bob'
#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
import hashlib
import time,datetime
# from blog.apps.info.models import userInfos
# from blog.apps.login_reg.models import userInfo
from blog.models.models.user_models import userInfo

#显示用户信息
def showUser(request):
    user = userInfo.objects.all();

    #转化时间戳成标准时间
    for v in user:
        x = time.localtime(v.add_time);
        v.add_time = time.strftime('%Y-%m-%d %H:%M:%S',x);
        if v.sex==1:
            v.sex = '女';
        else:
            v.sex = '男';
    return render(request,'show_user.html',{'user':user});

#修改当前用户
def user_modify(request,id):
    user = userInfo.objects.get(id=id);
    return render(request,'user_modify.html',{'user':user},context_instance=RequestContext(request));

#执行修改过程
def doUserModify(request):
    username = request.POST['username'];
    sex = request.POST['sex'];
    telephone = request.POST['telephone'];
    email = request.POST['email'];
    add_time = int(time.mktime(datetime.datetime.now().timetuple()));

    res = userInfo.objects.filter(id=request.POST['id']).update(
        username=username,
        sex=sex,
        telephone=telephone,
        email=email,
        add_time=add_time);
    if res:
        return HttpResponseRedirect('/showUser/');
    else:
        return HttpResponse('更新失败');

#删除该用户
def doUserDel(request,id):
    userInfo.objects.get(id=id).delete();
    return HttpResponseRedirect('/showUser');

