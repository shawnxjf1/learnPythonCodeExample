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

    # def testZiweiExcel(self):
    #     excelFile1 = '''D:\同步盘\Project\helper_others\(xtej1814-338_2016-09-26.xlsx'''
    #     ziwei_Use_OpenPyXl.calZiweiExcel(excelFile1)

    def testDealWithOverWork(self):
        #excelFile4 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201604-加班交通费及餐费明细表.xlsx'''
        #dealWithOverWork.loadOverWorkExcel(excelFile4,4,8,"201604.xlsx")

        # excelFile5 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201605-加班交通费及餐费明细表.xlsx'''
        # dealWithOverWork.loadOverWorkExcel(excelFile5, 4, 22, "201605.xlsx")
        #
        # excelFile6 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201606-加班交通费及餐费明细表.xlsx'''
        # dealWithOverWork.loadOverWorkExcel(excelFile6, 4, 20, "201606.xlsx")
        #
        # excelFile7 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201607-加班交通费及餐费明细表.xlsx'''
        # dealWithOverWork.loadOverWorkExcel(excelFile7, 4, 23, "201607.xlsx")
        #
        # excelFile8 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201608-加班交通费及餐费明细表.xlsx'''
        # dealWithOverWork.loadOverWorkExcel(excelFile8, 4, 25, "201608.xlsx")

        excelFile10 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201612-加班交通费及餐费明细表.xlsx'''
        dealWithOverWork.loadOverWorkExcel(excelFile10, 4, 24, "201612_new.xlsx")  ### 6 位excel开始计算的位置，28 位excel 结束的计算位置，需要改善的 起始位置和结束位置必须准确，不然会报错。

         # excelFile9 = '''D:\同步盘\Project\拉卡拉行政\加班报销\(201611-加班交通费及餐费明细表.xlsx'''
         # dealWithOverWork.loadOverWorkExcel(excelFile9, 4, 28, "201611.xlsx")



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()