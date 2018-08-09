#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
import sys
platform = sys.platform
if platform == 'linux':
    print('this is liunx!')
elif platform == 'win32':
    print('this is windows!')
else:
    print('other system')
print(sys.path)