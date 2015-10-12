#!/usr/bin/python
#coding=utf-8
__author__='bob';

#python版foreach循环的用法#

#python版的json串，同时在python中也叫做字典
list = {'name':'bob','sex':'man','age':24};

#下面开始循环
for k,v in list.items():
	print k,v;
	#python的for与其他语言区别，可以使用else作为结束
else:
	print '循环结束';
#最后命令行输出，会获得key,value
"""

age 24
name bob
sex man
循环结束

"""
