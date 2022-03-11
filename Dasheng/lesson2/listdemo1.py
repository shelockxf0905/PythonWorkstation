#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: listdemo1.py
@time: 2015/12/3 0003 下午 12:45
"""

x = range(-10,10)

result=[]
for i in x:
    if i < 0:
        result.append(i**2)
    else :
        result.append(i)
print result

result2= [i**2 for i in x if i<0]
result3= [i**2 if i <0 else i for i in x]

print result2
print result3


