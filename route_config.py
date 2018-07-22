#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, re
route_result = os.popen('route -n').read()
# print('返回数据：\n', route_result)
print(route_result.split('\n')[2:-1])
a = re.match('(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*)', '192.168.101.0   0.0.0.0         255.255.255.0   UG     100    0        0 ens33').group()

for list in route_result.split('\n')[2:-1]:
    if re.match('(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*)', list).group(4) == 'U':
        print('网关地址为：', re.match('(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*)', list).group(2))