#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import paramiko_ssh, scapy_ping_one_new, ip_list, re
for ip in  ip_list.ip_list:
    list_all = scapy_ping_one_new.scapy_ping_one(ip)
    # print(ip)#这里的ip只显示ip地址
    list_result = re.match('\d+\.\d+\.\d+\.\d+\s+(.*)', list_all).group(1)
    if list_result == '通':
        print(ip, '通了！')
        user = input('请输入用户名：')
        password = input('请输入密码：')
        while True:
            command = input('请输入命令：')
            print('如果想退出就输入" exit() "')
            if command == 'exit()': break
            print(paramiko_ssh.QYT_SSHClient_SingleCMD(ip=ip, command=command, user=user, password=password))
    else:
        print(ip, '不可达')