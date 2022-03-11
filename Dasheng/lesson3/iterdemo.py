#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: iterdemo.py
@time: 2015/12/4 0004 下午 10:11
"""

import itertools

x = range (1,10)
citer = itertools.combinations(x,3)
# for c in citer:
#     print c

piter = itertools.permutations(x,4)
# print type(piter)
# for p in piter:
#     print p

z=['a','b','c']
y=range(1,4)
priter = itertools.product(z,y)
# for pr in priter:
#     print pr

c = itertools.chain(citer,piter,priter)
for i in c:
    print i