#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import os, datetime
now = datetime.datetime.now()
# print(now)
othernow = now.strftime('%Y-%m-%d_%H:%M:%S')
# print(othernow)
before = now - datetime.timedelta(days= 5)
# print(before)
# file = os.mknod('save_fivedayago_time_' + othernow +'.txt')
a = open('save_fivedayago_time_' + othernow +'.txt', 'w')
a.write(str(before))