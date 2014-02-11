#!/usr/bin/python
# -*- coding: UTF-8 -*-
import rrdtool
import MySQLdb
import os

filerrd = '/root/s6509_traffic_in_79.rrd'
data = rrdtool.fetch(filerrd,"AVERAGE")
firsttime =data[0][0]
endtime = data[0][1]
step = data[0][2]
time = (endtime - firsttime)/step

conn = MySQLdb.connect(host="localhost",user="app",passwd="tften8sfpkz45hpw",db="app",charset="utf8")
db = conn.cursor()
sql = "insert into show_rss values(NULL,WEB,35,11111111,%s,%s)"
for x in counts:
	 db.execute(sql，
count = 0
while count <5761:
	time = firsttime+15*count
	value = data[2][count][0]
	if value = None:
		count+=1
		continue
	if
		pass
count = len(feed_['entries']) 
counts = [i for i in range(count)]
conn = MySQLdb.connect(host="localhost",user="app",passwd="tften8sfpkz45hpw",db="app",charset="utf8")
db = conn.cursor()
db.execute('truncate table show_rss')
sql = "insert into show_rss values(NULL,%s,%s,%s,%s,%s,NUll,%s,%s,'1')"
for x in counts:
    db.execute(sql,[feed_.entries[x].title,BeautifulSoup(feed_.entries[x].content[0].value).findAll('img')[0]['src'],feed_.entries[x].link,BeautifulSoup(feed_.entries[x].content[0].value).findAll('p')[0],parser.parse(feed_.entries[x].published).strftime("%Y-%m-%d %I:%M:%S"),random.randint(1000, 9999),random.randint(100, 300)])
conn.commit()
conn.close()
