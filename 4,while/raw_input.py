#!/usr/bin/python
#coding=utf-8
__author__='bob'

#通过while循环，实现按q回车退出的效果
#注意，需要在循环外赋空值
x = '';
while x != 'q':
	x = raw_input('按q后回车，可以退出本程序:');