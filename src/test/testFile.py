# encoding=utf-8
# python version 3.4

'''
Created on 2016-09-24

@author: shawn
'''
import unittest
##eclipse里不需要带src 转换到pycharm 需要做两件事 1.mark project as root  2.import 时候从顶层文件写起
from src.file import excelManager


# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')


    ##注意一定要以test开头
    def testReadExcel(self):
        '''
        执行错误：
        1.编码相关：(\201604 -> \x81604)   D:\同步盘\Project\拉卡拉行政\加班报销\201604-加班交通费及餐费明细表.xls 变成了D:\\同步盘\\Project\\拉卡拉行政\\加班报销\x81604-加班交通费及餐费明细表.xls
        '''
        ##python 会自动变成\\  D:\\同步盘\\Project\\拉卡拉行政\\加班报销
        #
        excelFile = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201604-加班交通费及餐费明细表.xls'''
        print('abcdeefg')
        excelManager.calculateExel(excelFile)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
