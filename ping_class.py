#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
class qty_ping:
    def __init__(self, ip):
        self.ip = IP(dst=ip)/ICMP()

    def src(self, srcip):
        self.ip = IP(dst=self.ip, src=srcip)/ICMP()

    def size(self, length):
        self.ip = IP(dst=self.ip, src=self.ip, len=length)/ICMP()

    def one(self):
        self.ip = sr1(self.ip, timeout=2, verbose=False)



if __name__ == '__main__':
    ping = qty_ping('192.168.1.8')
    print(ping.ip.show())
    print(ping.one())