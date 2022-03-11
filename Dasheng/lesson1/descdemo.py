#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: descdemo.py
@time: 2015/12/8 0008 下午 3:22
"""


class Email(object):
    def __init__(self,name,default=None):
        self.name='_'+name
        self.type=str
        self.default=self.default if default  else str()

    def __get__(self, instance, owner):
        return getattr(instance,self.name,self.default)

    def __set__(self, instance, value):
        if not isinstance(value,self.type):
            raise TypeError('Must be %s' % self.type)
        if not '@' in value:
            raise ValueError('Email Address is not valid')
        setattr(instance,self.name,value)

    def __del__(self,instance):
        pass

class User(object):
    email1 = Email("email1")
    email2= Email("email2")

    def __init__(self):
        pass







