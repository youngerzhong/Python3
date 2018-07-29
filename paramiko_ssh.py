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
    a = QYT_SSHClient_SingleCMD(ip='192.168.1.105', command='interface print', user='admin', password='dggj12345')
    print(a)