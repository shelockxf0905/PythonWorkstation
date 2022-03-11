#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: tupledemo.py
@time: 2015/12/3 0003 下午 3:29
"""
from __future__ import print_function

x = (1,u'你好',True)
print (*x)

y = (1,[1,2,3,4],True)
y[1][2]='hello world'

