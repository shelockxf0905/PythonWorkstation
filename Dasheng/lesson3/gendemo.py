#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: gendemo.py
@time: 2015/12/4 0004 下午 11:12
"""

def inc(n=1):
    while True:
        yield n
        n+=1

a = inc()
print type(a),a

print a.next(),a.next(),a.next()

for cnt,x in enumerate(a):
    if cnt == 10:
        break
    else :
        print x

for cnt,x in enumerate(a):
    if cnt == 10:
        break
    else :
        print x