# coding: utf-8
#!/usr/bin/python
import netsnmp
import rrdtool
import MySQLdb

ip='127.0.0.1'
string = 'public'
snmpport = '161'
ver = 2
fd = netsnmp.Session(DestHost=ip,Version=ver,RemotePort=snmpport,Timeout=400000,Retries=1,Community=string)
Inbytes = netsnmp.Varbind('ifInOctets.2')
Outbytes = netsnmp.Varbind('ifOutOctets.2')
output = fd.get(list)

conn = MySQLdb.connect(host="localhost",user="chart",passwd="tobaby",db="chart",charset="utf8")
db = conn.cursor()
sql = "insert into cacti_health values(NULL,'web','36','11111',%s,%s)"
db.execute(sql,[output[0],output[1]])
conn.commit()
conn.close()