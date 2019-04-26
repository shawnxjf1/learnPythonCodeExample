#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2016/12/27'
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

import unittest
import os
import sys

def printi(start,end):
    for i in range(start,end):
        print("i=" + str(i))

# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testCodecs(self):
        s = '中文'  # 这里的 s 是utf-8编码的字符串类型
        s.decode('ascii').encode('gb18030')
        print(sys.getdefaultencoding())

    def testStrInt(self):
        print('member' + str(2) + 'is finised,dont need to get again')

    def testStrInt2(self):
        print('member' + 2)
        # 2016年12月27日 TypeError: Can't convert 'int' object to str implicitly。必须要显示转换<br>

    def testStrFormat(self):
        print('== thread start = {a} and end = {b}'.format(a=2,b=5))
        print('--> thread start = {0} and end = {1}'.format(7,9))
        ## 2017年01月01日 执行结果:
        # == thread start = 2 and end = 5
        # --> thread start = 7 and end = 9

    def testRange(self):
        for i in range(1,10):
            print("i=" + str(i))