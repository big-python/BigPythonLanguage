#!/usr/bin/python
#coding=utf-8
__author__='bob'

#文件的操作

def file_read(path):
	f_open = open(path);
	print f_open.read();
	f_open.close();


def file_write(path,str):
	f_open = open(path,'w+');#以a+的形式写入，可以在后面追加
	f_open.write(str);
	f_open.close();


file_path = '../import.py';
#file_read(file_path);

file_write(file_path,'print "文件操作"\n');