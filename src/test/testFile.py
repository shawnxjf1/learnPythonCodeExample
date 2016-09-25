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


    ##注意一定要以test开头
    # def testReadExcel(self):
    #     '''
    #     执行错误：
    #     1.编码相关：(\201604 -> \x81604)   D:\同步盘\Project\拉卡拉行政\加班报销\201604-加班交通费及餐费明细表.xls 变成了D:\\同步盘\\Project\\拉卡拉行政\\加班报销\x81604-加班交通费及餐费明细表.xls
    #     '''
    #     ##python 会自动变成\\  D:\\同步盘\\Project\\拉卡拉行政\\加班报销
    #     #
    #     excelFile = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201604-加班交通费及餐费明细表.xlsx'''
    #     # SyntaxError: (unicodeerror) 'unicodeescape' codec can't decode bytes in position 60-61: truncated \xXX escape
    #     excelFile1='''D:\同步盘\Project\helper_others\(xtej1814-338.xlsx'''
    #     print('abcdeefg')
    #     excel_OpenPyXl.displayExcelSummaryInfo(excelFile1)

    def testZiweiExcel(self):
        excelFile1 = '''D:\同步盘\Project\helper_others\(xtej1814-338.xlsx'''
        excel_OpenPyXl.calZiweiExcel(excelFile1)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
