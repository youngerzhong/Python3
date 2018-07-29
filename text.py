#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  time, os
# age = input('How old are you today?')
# age10 = int(age) + 10
# print('in 10 years you will be '.capitalize() + str(age10) + ' years old.')


# print('jack ate ', end='')
# print('no fat')

# a = int(input('a '))
# print("%s"  %a)

# nowyear = time.strftime('%Y')
# oldyear = input('请输入出生年份：')
# if  int(nowyear) - int(oldyear) <= 2:
#     print('免费')
# elif int(nowyear) - int(oldyear) < 13:
#     print('儿童票')
# else:
#     print('成人票')
# print('完成')

# x = '哈 哈哈 哈哈哈'
# for i in range (len(x)):
#     print(x[i], end="")

# n =int(input('How many numbers to sum? '))
# total = 0
# for i in range(n):
#     s = input('enter number' + str(i + 1) + ':')
#     total = total + int(s)
# print('the sum is ' + str(total))


# n = int(input('enter an integer >= 0: '))
# fact = 1
# i = 2
# while i <= n:
#     fact = fact * i
#     i = i +1
# print(str(n) + 'factorial is' + str(fact))

# for row in range(1, 4):
#     for col in range(1, 4):
#         prod = row * col
#         if prod < 10:
#             print(' ', end='')
#         print(row * col, ' ', end='')
#     print()

# from test3 import say  #一般用这个  后面应用可以不加文件 直接函数名
# print(say(' aaaa'))

# import test3    #一般用这个 后面要加函数和变量名字
# print(test3.say("mrzangh"))

# import test3
# print(test3.change_name('aaaaa'))
import re
# str5 = 'dflsjdf qerewr'
# print(re.match('\w{3}([a-s])\w*\s+\w{2}([a-z])', str5).groups())
# str1 = 'Port-channel1.189          192.168.123.234  YES     GONFIG   UP'
# str2 = '187    54a2.74f7.0248    DYNAMIC     Gi1/0/11'
# a = re.match('([\w]*.{1,13})\s*(\d{3}.\d{3}.\d{3}.\d{3})\s*\w*\s*\w*\s*(.*)', str1).groups()
# b = re.match('(\d*)\s*(\w*.\w*.\d*)\s*(\w*)\s*(.*)', str2).groups()
# length = len(str1)
# print('-' * length)
# print('{0:7}:{1:>18}\n{2:7}:{3:>16}\n{4:7}:{5:>3}'.format('接口', a[0], 'IP地址', a[1], '状态', a[2]))
# # print('{0:7}:{1:>16}'.format('IP地址', a[1]))
# # print('{0:7}:{1:>3}'.format('状态', a[2]))
#
# length1 = len(str2)
# print('-' * length1)
# print('{0:10}:{1:>4}'.format('VLAN ID',b[0]))
# print('{0:10}:{1:>15}'.format('MAC ADD',b[1]))
# print('{0:10}:{1:>8}'.format('Type',b[2]))
# print('{0:10}:{1:>9}'.format('Type',b[3]))

# shuru = input('请输入：')
# res = []
# for c in shuru:
#     res.append(c * 4)
# print(res)

List1 = ['aaa', 111, (4, 5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4, 5)]
for i in List1:
    if i not in List2:
        print(i, 'only in List1')
for i in List2:
    if i in List1:
        print(i, 'in List1 and List2')
