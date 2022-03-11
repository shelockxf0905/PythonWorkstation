#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: demo1.py
@time: 2015/12/1 0001 下午 6:03
"""
import time
f=open('e:/TRD.csv')

start=time.clock()
lines=[t.split(',') for t in f]
end=time.clock()
print end-start


print('MySQLdb'.center(50, '='))