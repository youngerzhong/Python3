#!/usr/bin/env python3.6.5
# -*- coding:utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler
while True:
    try:
        port = 80
        httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
        print('Starting simple httpd on port:' + str(httpd.server_port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('接收到管理员ctrl + c，退出程序')
        break