#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, re

# os.mkdir('test')
os.chdir('test')
# qytang1 = open('qytang1', 'w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2', 'w')
# qytang2.write('test file\n')
# qytang2.write('qytang pryton\n')
# qytang2.close()
# qytang3 = open('qytang3', 'w')
# qytang3.write('test file\n')
# qytang3.write('thsi is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
print(os.getcwd())
keyword = '文件中包含"qytang"关键字的文件为：\n'
result_file_conn = []
all_file_list = os.listdir() #赋值罗列出来的目录
# print(all_file_list)
# print(os.path.isfile(all_file_list[0]))
for i in all_file_list:    #遍历整个目录
    if os.path.isfile(i):  #判断目录里那些是文件（此时的i是布尔型）
        # print(os.path.isfile(i))
        for line in  open(i): #遍历打开文件
            # print(re.match('.*qytang.*', line))
            if re.match('.*qytang.*', line):  #正则配关键字'qytang'
                # print('文件中包含"qytang"关键字的文件为：\n',i)  #自己做的打印效果有问题，借鉴下面的
                #第一次用，才知道原来keyword 赋值 keyword 加变量i时，原始的keyword会不重复打印，只有变量i才会变
                keyword = keyword + '{0:>13}'.format(i) + '\n'
                # result_file_conn.append(i)
print(keyword)