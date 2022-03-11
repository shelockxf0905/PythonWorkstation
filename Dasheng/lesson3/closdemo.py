#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: closdemo.py
@time: 2015/12/4 0004 下午 5:13
"""


def f(x):
    y = 222
    def inner(z):
        return x* y +z
    return inner

a10=f(14)
a20=f(20)

print a10(29),a20(29)

