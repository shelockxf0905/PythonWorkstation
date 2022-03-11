#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: propdescriptor.py
@time: 2015/12/8 0008 下午 9:55
"""


class Property(object):
    def __init__(self,propname,datatype,default =None):
        self._name='_'+propname+'_'
        self._type=datatype
        self._default = default if default else self._type()

    def __get__(self, instance, owner):
        return getattr(instance,self._name,self._default)

    def __set__(self, instance, value):
        if not isinstance(value,self._type):
            raise TypeError('Type Error , must be %s type0' % self._type)
        setattr(instance,self._name,value)

    def __del__(self):
        pass

class Email(Property):
    def __init__(self,propname,default=None):
        super(Email,self).__init__(propname,str,default)

    def __set__(self, instance, value):
        if not isinstance(value,self._type):
            raise TypeError('Type Error , must be %s type0' % self._type)
        if not '@' in value :
            raise ValueError('Email address is not valid')
        setattr(instance,self._name,value)


class Chinese(object):


    ID = Property('id',int)
    Name = Property('name',str)
    Email = Email('email')

    def __init__(self,id,name,email):
        self.ID = id
        self.Name=name
        self.Email = email

    @staticmethod
    def getPeopleByParents(mather,father):
        print mather,father
        return Chinese(10,'dasheng','ab@def')

    @classmethod
    def getPeopleBySibling(cls,sibling):
        print sibling
        return cls(20,'bajie','de@ad')

    def __str__(self):
        return 'ID = {0} , Name = {1} ,Email = {2}'.format(self.ID,self.Name,self.Email)

    def __repr__(self):
        return 'ID={0}'.format(self.ID)

    def __add__(self,other):
        return self.ID + other.ID

    # def __lt__(self, other):
    #     return self.ID < other.ID

class JiLin(Chinese):
    pass


dasheng = JiLin.getPeopleByParents('mather','father')
bajie = JiLin.getPeopleBySibling('dasheng')

print dasheng
print bajie