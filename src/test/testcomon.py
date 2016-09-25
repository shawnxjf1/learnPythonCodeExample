# encoding=utf-8
# python version 3.4

'''
Created on 2016-09-24

@author: shawn
'''

'''
待完善：怎么只执行某一个test函数
'''

import unittest
##eclipse里不需要带src 转换到pycharm 需要做两件事 1.mark project as root  2.import 时候从顶层文件写起
from src.excel import excel_OpenPyXl


# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testMap(self):
        map1 = {1:[2,3]}
        if map1[1]:
            print('not empty')
        else:
            print('empry')

        if map1[2]:
            print('2 not empty')
        else:
            print('2 empry')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
