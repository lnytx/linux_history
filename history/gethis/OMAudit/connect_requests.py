'''
Created on 2017年4月25日

@author: ning.lin
'''
#-*- coding:utf-8 -*-

import requests

#!/usr/bin/env python
#coding:utf-8
import logging
import socket
import struct
import sys

from config import *




logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(filename)s %(lineno)d [%(levelname)s] %(message)s',
            filename=sys.path[0]+'/omsys.log',
            filemode='a')

if len(sys.argv)<6:#对$(history 1)对行校验，正常的输出是这样的，136 root 2017-04-24 21:17:38 ls，如果不是这样就说明/etc/profile配置文件有问题
    logging.error('History not configured in /etc/profile!')
    sys.exit()

def get_local_ip(ethname):#获取本机IP
    if sys.platform == 'win32':
        return socket.gethostbyname(socket.gethostname())
    else:
        mod_name = 'fcntl'
        mod_obj = __import__(mod_name)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = mod_obj.ioctl(sock.fileno(), 0x8915, struct.pack('256s', bytes(ethname[:15], 'utf-8')))
            return socket.inet_ntoa( addr[20:24] )
        except Exception as e:
            logging.error('get localhost IP address error:'+str(e))
            return "127.0.0.1"



def pull_history(url,http_get_param=""):
    try:
        r = requests.get(url, params=http_get_param)
    except Exception as e:
        logging.error('connection django-cgi server error:'+str(e))
        sys.exit()

Sysip = get_local_ip(Net_driver)
SysUser = sys.argv[2]
History_Id = sys.argv[1]
History_date = sys.argv[3]
History_time = sys.argv[4]
History_command = ""

for i in range(5, len(sys.argv)):
    History_command+= sys.argv[i]+" "
s={'History_Id':History_Id,'history_ip':Sysip,'history_user':SysUser,'history_datetime':(History_date+History_time).encode('utf-8'),'history_command':History_command.strip()}
url='http://172.17.39.225:8000/home'
#s= "/omaudit/omaudit_pull/?history_id="+History_Id+"&history_ip="+Sysip+"&history_user="+SysUser+"&history_datetime="+History_date+urllib.parse.quote(" ")+History_time+"&history_command="+urllib.parse.quote(History_command.strip())
pull_history(url,s)