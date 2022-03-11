#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: 01.reqdemo.py
@time: 2015/12/10 0010 下午 3:07
"""

import requests
header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}
response = requests.get('http://www.haoyisheng.com',headers=header)
#print response.text

print response.content.decode('gbk')