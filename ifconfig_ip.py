#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, re  #导入模块
ifconfig_result = os.popen('ifconfig ens33').read() #打开一个命令管道，并读取
# print(ifconfig_result) #打印内容出来
re_findall_result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ifconfig_result) #用正则.findall来匹配
# print(re_findall_result) #打印正则匹配之后的结果
for ip in  re_findall_result:  #for循环遍历 正则匹配之后的内容
    # print(ip.split('.')[3])
    if ip.split('.')[3] == '0': #再次通过使用正则.split来匹配对比结果
        mask = ip
    elif ip.split('.')[3] == '255':
        broadcast = ip
    else:
        ipv4_ip = ip
a = ('{0}{1:>14}\n{2:>14}{3:>16}\n{4:>14}{5:>16}').format('Network Mask :', mask, 'Broadcast :', broadcast, 'IPv4 Addr :', ipv4_ip) #格式化字符打印内容
print(a)