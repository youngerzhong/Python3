#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import os, time, re
while True:
    try:
        netstat_result = os.popen('netstat -tulnp').read()
        # print(a)
        split_netstat_result = re.split('\n', netstat_result)[2:-1]
        # print(b)
        for i in split_netstat_result:
            i = i.split()[3]
            # print(i)
            i = re.match('.*\:(\d+)$', i).groups()[0]
            if i == '80':
                print('(TCP/80)服务已经被打开')
                time.sleep(5)
                break
            else:
                print('等待5秒重新开始监控！')
                time.sleep(5)
                break
    except KeyboardInterrupt:
        print('接收到ctrl + c，退出程序')
        break