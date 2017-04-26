'''
Created on 2017年4月25日

@author: ning.lin
'''
from django.conf.global_settings import INSTALLED_APPS


print(INSTALLED_APPS)
tup=(1, '192.168.153.129', '411', 'root', '2017-04-25 23:37:43', 'cat omsys.log')
list=[1, '192.168.153.129', '411', 'root', '2017-04-25 23:37:43', 'cat omsys.log']
print(list[2:5])