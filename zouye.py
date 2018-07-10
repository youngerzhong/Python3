#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a = int(input('请输入整数:'))
# b = int(input('请再次输入整数:'))
# resuly = a + b
# print(a,'+',b,'的结果')
# print('计算结果为：',resuly)

# department1 = 'Security'
# department2 = 'Python'
# depart1_m = 'cq_bomb'
# depart2_m = 'qinke'
# COURSE_FEES_SEC = 456789.123456
# COURSE_FEES_Python = 1234.3456
# print('第一种方法：')
# line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End' % (department1, depart1_m, COURSE_FEES_SEC)
# line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End' %(department2, depart2_m, COURSE_FEES_Python)
# length = len(line1)
# print('=' * length)
# print(line1)
# print(line2)
# print('=' * length)
# print('第二种方法：')
# Line1 = 'Department1 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End' .format(department1, depart1_m, COURSE_FEES_SEC)
# Line2 = 'Department2 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End' .format(department2, depart2_m, COURSE_FEES_Python)
# length1 = len(Line1)
# print('=' * length1)
# print(Line1)
# print(Line2)
# print('=' * length1)

# import copy
# l1 = [4, 5, 7, 1, 3, 9, 0]
# l2 = l1
# # l2 = l1.copy()
# l2.sort()
# for i in range(len(l1)):
#     print(l1[i], l2[i])

import os, re
ifconfig_result = os.popen('ifconfig ens33').read()
# print(ifconfig_result)
re_findall_result = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)
# print(re_findall_result)
for ip in re_findall_result:
    # print(ip)
    print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', ip))
    if re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip) == '0':
        mask = ip
    elif re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip) == '255':
        broadcast = ip
    else:
        ipv4_ip = ip
a = '{0}\n{1}\n{2}'.format('Networn')
# a = 'fsdf.fsfsd.dfasdf '
