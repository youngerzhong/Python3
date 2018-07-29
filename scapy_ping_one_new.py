#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from random import randint
def scapy_ping_one(host):
    id_ip = randint(1,255)#随机产生ip ID位
    # id_ping =#随机产生ping ID位
    # seq_ping =#随机产生ping序列号位
    #构造ping数据包
    packet = IP(dst=host)/ICMP()
    ping = sr1(packet, timeout=2, verbose=False)#获取响应信息，超时为2秒，关闭详细信息
    if ping:#如果有响应信息
        return '{0}{1:>2}'.format(host, '通')
    else:
        return '{0}{1:>2}'.format(host, '不通')
if __name__ == '__main__':
    result1 = scapy_ping_one('192.168.1.8')
    print(result1)
    result2 = scapy_ping_one('192.168.125.134')
    print(result2)