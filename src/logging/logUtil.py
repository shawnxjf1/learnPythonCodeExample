#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2017/1/1'
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

##  参考 http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html

import logging
import unittest
import os

logging.basicConfig(level=logging.DEBUG,
                format='%(pathname)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s %(process)d ',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='testLog.log',
                filemode='w')

def addLogToConsole():
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def debuger(msg):
    logging.debug(msg)

def info(msg):
    logging.info(msg)

def error(msg):
    logging.error(msg)



# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testLog(self):
        addLogToConsole() ## 一定要加这个函数才输出到控制台
        logging.info('testLog executing...')
        ## 2017年01月01日 输出  Testing started at 上午11:04 ..., logging/testLog.log文件


