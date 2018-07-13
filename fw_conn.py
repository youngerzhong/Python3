#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
tcp = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO \
       TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'
# ip_fw_result = re.findall('\d+\.\d+\.\d+\.\d+', tcp)
# po_fw_result = re.findall('\d+\.\d+\.\d+\.\d+\:(\d+)', tcp)
by_fw_result = re.findall('bytes\s(\d+)', tcp)
print(by_fw_result)
# dict_fw_result = {(ip_fw_result[0], po_fw_result[0], ip_fw_result[1], po_fw_result[1]}
# by_fw_result = re.findall()
# print(ip_fw_result, po_fw_result, by_fw_result)
