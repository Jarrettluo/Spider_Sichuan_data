# encoding: utf-8
"""
@version: 1.0
@author: 
@file: main.py
@time: 2020/1/19 21:49
"""

import re
import requests

r = requests.get('https://cn.bing.com/')

print(r.status_code)

print(r.headers['content-type'])

print(r.encoding) #自动编码来自服务的内容

print(r.text) #打印服务器响应的内容。

#print(r.json())