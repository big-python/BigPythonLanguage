#!/usr/bin/python
#coding=utf-8

#python的switch.
#因为python是没有switch这个方法的，但是可以用字典来实现同样的内容
#下面用四则运算作为例子

def plus(x,y):
	return x+y;
def minus(x,y):
	return x-y;
def times(x,y):
	return x*y;
def chu(x,y):
	return x/y;
def yu(x,y):
	return x%y;
#设置字典，等价于switch的分支结构
operate = {'+':plus,'-':minus,'*':times,'/':chu,'%':yu};

def fun(x,o,y):
	# return operate[o](x,y);
	return operate.get(o)(x,y);


#测试
# print fun(1,'+',2);
print fun(5,'%',10);