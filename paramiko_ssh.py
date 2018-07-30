#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import paramiko
def QYT_SSHClient_SingleCMD(ip, command, port=22, user='root', password='root'):#参数ip地址，命令，端口，用户名，密码
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=user, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(command)
        x = stdout.read().decode()
        return x
    except Exception as e:
        print('%tErrorn %s'%(ip, e))

if __name__ == '__main__':
    text = QYT_SSHClient_SingleCMD(ip='192.168.125.135', command='ls')
    print(text)
#     ip = input('请输入ip地址:')
#     user = input('请输入用户名：')
#     password = input('请输入密码：')
# while True:
#     command = input('请输入命令：')
#     print('如果要退出命令，请输入"exit()"')
#     if command == 'exit()':break
#     test = QYT_SSHClient_SingleCMD(ip=ip, command=command, user=user, password=password)
#     print(test)