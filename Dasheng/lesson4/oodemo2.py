#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: oodemo2.py
@time: 2015/12/9 0009 下午 5:07
"""


class A(object):
    def __init__(self):
        print 'in A'

class B(A):
    def __init__(self):
        #A.__init__(self)
        super(B,self).__init__()
        print 'in B'


class C(A):
    def __init__(self):
        super(C,self).__init__()
        print 'in C'

class D(B,C):
    def __init__(self):
        super(D,self).__init__()
        print 'in D'

d= D()

