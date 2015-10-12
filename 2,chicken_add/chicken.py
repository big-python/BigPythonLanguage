#!/usr/bin/python
#coding=utf-8
__author__='bob';
#解决百钱买百鸡问题
#今有钱百元，欲买百鸡，大鸡钱5，中鸡钱3，小鸡3只钱1，问大中小鸡各何？

for i in range(0,101):
	for j in range(0,101):
		for k in range(0,101):
			if i+j+k==100 and 5.0*i+3*j+k/3.0==100:
				print i,j,k;