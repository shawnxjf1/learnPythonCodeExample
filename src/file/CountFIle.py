#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2019/1/21'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# -*- coding: utf-8 -*-
# 参考链接：http://www.runoob.com/python/os-walk.html
import os,os.path
import unicodedata;
import sys

# 要查找的文件夹地址
dir = "/Users/shawn/Downloads/"

def get_FileSize(filePath):
    filePath = filePath
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

number = 0
size = 0
#os.walk()方法是一个简单易用的文件、目录遍历器
# root正在遍历的这个文件夹的本身的地址
# dirname是一个list,内容是该文件夹中所有的目录的名字(不包括子目录)
# filenames同样是list,内容是该文件夹中所有的文件名字(不包括子目录)
for dirpath,dirname,filenames in os.walk(dir):
       for filename in filenames:
            print(dirpath,filename,filenames)
            # os.path.splitext()是一个元组,类似于('188739', '.jpg')，索引1可以获得文件的扩展名
            if os.path.splitext(filename)[1]=='.ev4':
                number += 1
            fullName = os.path.join(dirpath,filename)
            size += get_FileSize(fullName)
print('number:' + str(number))
print('size:' + str(size))

