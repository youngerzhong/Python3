#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

os.chdir('/root/pythoncentos/test/')
os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang pryton\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('thsi is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')
