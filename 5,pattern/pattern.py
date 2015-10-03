#!/usr/bin/python
#coding=utf-8

#正则表达式

import re;

str = '123456789';

pattern = r'1';#配对正则的规则

print re.findall(pattern,str);#使用，前面是规则，后面是需要匹配的字符串

#使用对象存起正则，方便以后调用
tel = r'\d{3,4}-\d{8}';
p_tel = re.compile(tel);#用这个函数代表正则已经被编译完了，速度会比没有编译的快很多
#调用
print p_tel.findall('020-84359136');

#不区分大小写
p_f = re.compile('\w',re.I);
print p_f;
