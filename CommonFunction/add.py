#!/usr/bin/python
#coding=utf-8
__author__='bob'

#实现四则运算里面的加法的函数
def add():
	a = raw_input('请输入第一个数字:');
	b = raw_input('请输入第二个数字:');
	print '执行整数加法后得到的结果为:';
	print int(a)+int(b);
add();