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
##eclipse里不需要带src 转换到pycharm 需要做两件事 1.mark project as root  2.import 时候从顶层文件写起
from src.excel import ziwei_Use_OpenPyXl
from src.excel import dealWithOverWork

# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testZiweiExcel(self):
        excelFile1 = '''D:\同步盘\Project\helper_others\(xtej1814-338_2016-09-26.xlsx'''
        ziwei_Use_OpenPyXl.calZiweiExcel(excelFile1)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()