#!/usr/bin/env python
# -*- coding:utf-8 -*-
# def say(name):
#     """ prints a hello message.
#     """
#     cap_name = name.capitalize()
#     print('hello' + cap_name + ', how are you?')

# import math
# def dist(x, y, a, b):
#     s = (x - a) ** 2 + (y - b)**2
#     return math.sqrt(s)
# def rect_area(x, y, a, b):
#     width = abs(x - a)
#     height = abs(y - b)
#     return width * height

# name = 'Jack'
# def say_hello():
#     print('Hello ' + name + '!')
# def change_name(new_name):
#     name = new_name

# def main():
#     pwd = input('what is the password?')
#     if pwd == 'apple':
#         print('Logging on ...')
#     else:
#         print('Incorrect password.')
#     print('All done!')
import scapy_ping_one_new
a = input('请输入ip地址:')
print(scapy_ping_one_new.scapy_ping_one(a))
import paramiko