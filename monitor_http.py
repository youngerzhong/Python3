#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import os, time, re
try:
    number = input('请输入要监控的端口：''\n') #输入端口号
    while True:
        netstat_result = os.popen('netstat -tulnp').read()  #打开liunx命令
        split_netstat_result = re.split('\n', netstat_result)[2:-1] #正则匹配数据
        # print(split_netstat_result)
        for i in split_netstat_result:   #遍历正则数据
            i = i.split()[3]             #提取数据
            print(i)
            i = re.match('.*\:(\d+)$', i).group(1)  #再次正则匹配数据
            # print(i)
            if i == number:   #判断
                print('{0}{1},{2}'.format('注意TCP/', number, '打开了'))
                time.sleep(2)
                break
            else:
                print('{0}{1},{2}'.format('继续监控端口:', number, '没开启'))
                time.sleep(2)
                break
except KeyboardInterrupt:
    print('接收到管理员的ctrl + C，程序退出')