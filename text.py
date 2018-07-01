#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  time
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

import test3
print(test3.change_name('aaaaa'))