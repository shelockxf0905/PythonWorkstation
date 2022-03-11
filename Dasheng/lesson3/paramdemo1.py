#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: paramdemo1.py
@time: 2015/12/4 0004 下午 12:50
"""

# def funA(x,y,z,*args,**kwargs):
#     print x,y,z
#     funB(,,*args,**kwargs)
#
# def funB(...,*args,**kwargs):
#     pass

# x = range(1,6)
# print 'x=',id(x)
#
# def funa(a):
#     print 'a=',id(a)
#     a[1]='hello world'
#
# funa(list(x))
# print x

x = 10


def fun():
    '''
    @author
    :param
    :return:
    :example:
    '''
    global x
    x += 2
    print 'in function', x

print fun.__doc__

