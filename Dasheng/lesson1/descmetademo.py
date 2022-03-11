#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: descmetademo.py
@time: 2015/12/8 0008 下午 3:48
"""


class Email(object):
    def __init__(self,default=None):
        self.name=None
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


class DescMeat(type):
    def __new__(cls, name,base, dict):
        slots=[]
        for key,value in dict.items():
            if isinstance(value,Email):
                value.name='+' + key
                slots.append(value.name)
        dict['__slot__']=slots
        return type.__new__(cls,name,base,dict)

class Model(object):
    __metaclass__ = DescMeat

class User(Model):
    email1=Email()
    email2=Email()

