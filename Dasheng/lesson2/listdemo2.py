#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: listdemo2.py
@time: 2015/12/3 0003 下午 1:49
"""
import time

#TRD.csv
f = open('e:/TRD.csv')

start = time.clock()
lines=[t.split(',')  for t in f]
end = time.clock()


print end- start

start2 = time.clock()
lines2=(t.split(',')  for t in f)

end2 = time.clock()

print end2- start2

print type(lines),type(lines2)

for i in lines2:
    pass