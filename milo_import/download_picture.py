#!/usr/bin/python
#coding=utf-8

#下载空间或贴吧中的图片
#用python实现，主要是进行与php的区别

import re,urllib;

#获取url页面的源代码(其实就是HTML源码)
def getHtml(url):
	page = urllib.urlopen(url);
	return page.read();

#编译正则
def getPattern(pattern,html):
	p_url = re.compile(pattern);
	url_list = p_url.findall(html);
	return url_list;

#下载图片
def downImg(list):
	num = 1;
	for url in list:
		urllib.urlretrieve(url,'%s.jpg' % num);
		num+=1;


html = getHtml('http://tieba.baidu.com/p/3383906444');
# print getPattern(r'href=\'(/Book/\d+\.aspx)\'',html);
url_list = getPattern(r'src="(.*?\.jpg)"',html);
downImg(url_list);