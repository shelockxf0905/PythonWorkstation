#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: listdemo3.py
@time: 2015/12/3 0003 下午 1:33
"""

def a(x):
    if x > 0 :
        return True
    else :
        return False

x = range (-10,10)
print filter(a,x)

def m(x):
    if x < 0:
        return x**2
    else :
        return x
print map(m,x)