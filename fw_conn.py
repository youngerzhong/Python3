#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
tcp = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO \
       TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'
re_fw_conn = re.findall('(\d+\.\d+\.\d+\.\d+):(\d+)\s?\w+\s?(\d+\.\d+\.\d+\.\d+):(\d+),\s?\w+\s+\d+:\d+:\d+,\s?bytes\s?(\d+),\s?flags\s?(\w+)', tcp) #正则匹配
# print(re_fw_conn)
print('\n打印字典\n')
dict_fw_conn = {re_fw_conn[1][0:3]: re_fw_conn[1][4:6], re_fw_conn[0][0:3]: re_fw_conn[0][4:6]}  #转换为字典
print(dict_fw_conn)
print('\n格式化打印输出\n')
tcp_fw_conn ='{0:>8}{1:25}|{2:>15}{3:10}|{4:>15}{5}|{6:>15}{7:10}|\n{8}{9:25}|{10:>15}{11}'.format('str : ', re_fw_conn[0][0], 'str_p : ', re_fw_conn[0][1], 'dst : ',re_fw_conn[0][2], 'dst_p : ',re_fw_conn[0][3], 'bytes : ', re_fw_conn[0][4], 'flags : ', re_fw_conn[0][5])
print(tcp_fw_conn)
print('='* 120)
tcp2_fw_conn ='{0:>8}{1:25}|{2:>15}{3:10}|{4:>15}{5}|{6:>15}{7:10}|\n{8}{9:25}|{10:>15}{11}'.format('str : ', re_fw_conn[1][0], 'str_p : ', re_fw_conn[1][1], 'dst : ',re_fw_conn[1][2], 'dst_p : ',re_fw_conn[1][3], 'bytes : ', re_fw_conn[1][4], 'flags : ', re_fw_conn[1][5])
print(tcp2_fw_conn)
print('=' * 120)