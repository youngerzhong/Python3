#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
ifconfig_result ='''
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
XHC0: flags=0<> mtu 0
XHC20: flags=0<> mtu 0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 8c:85:90:43:2c:ec
	inet6 fe80::c06:6700:3785:61d%en0 prefixlen 64 secured scopeid 0x6
	inet 172.20.10.14 netmask 0xfffffff0 broadcast 172.20.10.15
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 0e:85:90:43:2c:ec
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether da:81:6c:3a:5e:3b
	inet6 fe80::d881:6cff:fe3a:5e3b%awdl0 prefixlen 64 scopeid 0x8
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 9a:00:dc:a9:c1:01
	media: autoselect <full-duplex>
	status: inactive
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 9a:00:dc:a9:c1:00
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 9a:00:dc:a9:c1:00
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 10 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 9 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::3a5d:c7a6:95e6:1b38%utun0 prefixlen 64 scopeid 0xc
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::cf9b:f4f0:88dc:bf39%utun1 prefixlen 64 scopeid 0xd
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::47f9:c851:2e27:2be%utun2 prefixlen 64 scopeid 0xe
	nd6 options=201<PERFORMNUD,DAD>
'''
# print(ifconfig_result)
# re_ifconfig_result = re.findall('\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}\:\w{2}', ifconfig_result) #mac地址
# print(re_ifconfig_result)
# a = re.findall('\s(\d*\.\d*\.\d*\.\d*)\s', ifconfig_result)  #ip地址、掩码
# print(a)
# b =re.findall('\w{1,5}\:\s', ifconfig_result) #接口
# # print(b)
c = str(re.split('\n', ifconfig_result))
print(c)
d = re.findall('\w+\:? \s', c)
print(d)
