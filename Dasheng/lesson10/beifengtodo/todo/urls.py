#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: urls.py
@time: 2016/1/1 0001 下午 4:17
"""

from django.conf.urls import include, url
from django.contrib import admin
from todo.views import *

urlpatterns = [
    url(r'^add/$', addDream,name='add_dream'),
    url(r'^d/$',deleteDream,name='delete_dream'),
    url(r'^u/$',updateDream,name='update_dream')
]

