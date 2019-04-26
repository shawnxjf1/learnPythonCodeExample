#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2018/8/17'
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

import os
import re
import sys


def walk_dir_not_svn(path):
    '''
    函数接受一个路径参数，
    遍历参数path路径下的所有目录和文件，并过滤.svn的文件
    '''
    file_list = []
    for root, dirs, files in os.walk(path):
        # 目录
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not re.search(r'\.svn', dir_path):
                file_list.append(dir_path)
        # 文件
        for file in files:
            file_path = os.path.join(root, file)
            if not re.search(r'\.svn', file_path):
                file_list.append(file_path)
    return file_list


def walk_dir_svn(path):
    '''
    函数接受一个路径参数，
    遍历参数path路径下的所有目录和文件，并过滤.svn的文件
    '''
    file_list = []
    for root, dirs, files in os.walk(path):
        # 目录
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if re.search(r'\.svn', dir_path):
                file_list.append(dir_path)
        # 文件
        for file in files:
            file_path = os.path.join(root, file)
            if re.search(r'\.svn', file_path):
                file_list.append(file_path)
    return file_list


if __name__ == "__main__":
    print('here is print.')
    print(sys.argv[0])          #sys.argv[0] 类似于shell中的$0,但不是脚本名称，而是脚本的路径
    print(sys.argv[1])
    aa = walk_dir_svn('/Users/shawn/YXZN_project/yxzn_repository/ivm-marketing/trunk')
    for i in aa:
        print ('file:%s' %i)
