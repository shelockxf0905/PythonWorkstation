#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: filedemo.py
@time: 2015/12/4 0004 下午 11:18
"""

import os
def getFilesList(rootDir):
    for path,dirlist,filelist in os.walk(rootDir):
        for filename in filelist:
            if filename.endswith('.csv'):
                yield os.path.join(path,filename)

def openFiles(fileslist):
    for filename in fileslist:
        yield (filename,open(filename))

def grep(filelist,pattern):
    for (filename,fh) in filelist:
        for line in fh :
            if pattern in line :
                yield (filename,line)

filelist = getFilesList('e:\\Data1000')
files = openFiles(filelist)
lines= grep(files,'2010-07')

for (filename,line) in lines:
    print '~ * 60'
    print filename
    print line

