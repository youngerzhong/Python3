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
import re
cmd_str = 'Port-channel1.189   YES CONFIG up'
a=re.match('(^\w+.)', cmd_str).groups()
print(len(cmd_str))
print(a)