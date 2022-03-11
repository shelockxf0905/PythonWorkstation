#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: decadeom.py
@time: 2015/12/4 0004 下午 5:36
"""

import time

def log(func):
    def wrapper(*args,**kwargs):
        print '~' * 40
        start = time.clock()
        res = func(*args,**kwargs)
        end = time.clock()
        print 'calling',func.__name__,args,kwargs
        print 'start at ',start,' end at',end
        return res
    return wrapper

def logEx(name):
    def wrapper(func):
        def wrapper1(*args,**kwargs):
            print '~' * 40
            start = time.clock()
            res = func(*args,**kwargs)
            end = time.clock()
            print name,'calling',func.__name__,args,kwargs
            print 'start at ',start,' end at',end
            return res
        return wrapper1
    return wrapper



# def f2(x,y):
#     print 'calling f2',x,y
#     start = time.clock()
#     z = x+y
#     end = time.clock()
#     print 'start at :',start,' end at :',end
#     return z

def authorize(func):
    def wrapper(*args,**kwargs):
        if True:
            print 'Welcome'
            return func(*args,**kwargs)
        else :
            print 'You are not allowed'
    return wrapper

@authorize
@logEx('Tom')
def f(x,y):
    return x+y

print f(10,20)


