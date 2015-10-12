#!/usr/bin/python
#coding=utf-8

#数据库操作

import MySQLdb；
con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456');
cur = con.cursor();
con.select_db('rgrass');
sql = "insert into user_info(user_name) value(%s)";
cur.execute(sql,('aaa'));

sqlm = "insert into user_info(user_name) values(%s)";
cur.executemany(sqlm,[('aaa'),('bbb')]);


cur.execute('select*from user_info');
cur.fetchone();#每fetch一次，执行一条
cur.scroll(0,'absolute');#重置指针，回到第一条

cur.fetchmany(17);#瞬间取17条

#最后关闭数据库
cur.close();
con.close();