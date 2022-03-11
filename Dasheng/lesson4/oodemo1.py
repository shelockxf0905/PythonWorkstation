#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: oodemo1.py
@time: 2015/12/8 0008 下午 6:15
"""

class Chinese(object):

    nation = 'China'

    def __init__(self,id,name):
        self._id = id
        self.__name = name
        self.__email = None


    def sayHi(self,msg):
        print self.__name,msg

    def getID(self):
        return self._id

    def setID(self,id):
        self._id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @name.deleter
    def name(self):
        del self.__name

dasheng = Chinese(1,'dasheng')
print dasheng.getID()
dasheng.setID(10)

print dasheng.name
dasheng.name='bajie'
print dasheng.name

