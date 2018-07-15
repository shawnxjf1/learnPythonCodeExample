# encoding=utf-8
# python version 3.4

'''
Created on 2016-09-24

@author: shawn
'''

'''
待完善：怎么只执行某一个test函数
'''

'''
报错：
 1.'There is no item named %r in the archive' % name)
KeyError: "There is no item named 'xl/_rels/workbook.xml.rels' in the archive"  是由于本身是xls格式手动修改后缀成xlsx导致

2.openpyxl 不支持 xls格式（）
'''

import unittest
import configparser
##eclipse里不需要带src 转换到pycharm 需要做两件事 1.mark project as root。  2.import 时候从顶层文件写起。
from src.excel import dealWithOverWork

# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testConfigParser(self):
        cf = configparser.ConfigParser()
        cf.read("excel_config.ini")
        keyValues = cf.options("overwork") ## 1.ini中是中文的话乱码。 2.
        print("keyValues=%s"%keyValues)

    def testDealWithOverWork(self):
        excelFile702 = '''D:\我的坚果云\Project\拉卡拉行政\加班报销\(201702-加班交通费及餐费明细表.xlsx'''
        dealWithOverWork.loadOverWorkExcel(excelFile702, 4, 10, "201702_new.xlsx")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()