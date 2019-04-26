#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2016/12/25'
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

# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testMap(self):
        print(os.getcwd())
        # 2016-12-25 输出结果: /Users/shawn/eclipse_workspace_pdev_group/pdev_v1/pythonLearnCodeExample/src/file

    def testCreatDir(self):
        os.mkdir('/Users/shawn/eclipse_workspace_pdev_group/pdev_v1/pythonLearnCodeExample/api/file/aa.txt')

    def testCreatFile(self):
        f = open('/Users/shawn/eclipse_workspace_pdev_group/pdev_v1/pythonLearnCodeExample/api/file/page_1' + ".html", 'w')
        f.write("xjf")
        f.close()
        ## 2016年12月25日 创建成功

    def testFileExist(self):
        if os.path.isfile('/Users/shawn/eclipse_workspace_pdev_group/pdev_v1/pythonLearnCodeExample/api/file/page_1.html'):
            print('exist')
        else:
            print('not exist')

