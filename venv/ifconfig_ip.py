#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, re
ifconfig_result = os.popen('ifconfig ens33').read()
# print(ifconfig_result)
re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ifconfig_result)
print(re_findall_result)
for ip in  re_findall_result:
    # print(ip.split('.')[3])
    if ip.split('.')[3] == '0':
        mask = ip
    elif ip.split('.')[3] == '255':
        broadcast = ip
    else:
        ipv4_ip = ip
a = ('{0}{1:>14}\n{2:>14}{3:>16}\n{4:>14}{5:>16}').format('Network Mask :', mask, 'Broadcast :', broadcast, 'IPv4 Addr :', ipv4_ip)
print(a)