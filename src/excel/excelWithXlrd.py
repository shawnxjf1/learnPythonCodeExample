#encoding=utf-8
##attention : python 版本号变化比较大经常网上有一些错误的代码，所以自己写代码的时候一定要表明自己开发的版本号
'''
Created on 2016年9月24日
@author: shawn
'''
##env:python 3.5

#xlutils  module ：This package provides a collection of utilities for working with Excel files. Since these utilities may require either or both of the xlrd and xlwt packages, they are collected together here, separate from either package.
from xlrd import open_workbook
from xlutils.copy import copy

def append2Excel(filename, datas, beginRow):
    rb = open_workbook(filename)
    wb = copy(rb)

    ##获取sheet
    sheet = wb.get_sheet(0)

    ##do something in sheet
    x = beginRow
    y = 1
    for article in datas:
        sheet.write(x, y, article)
        y +=1
    wb.save(filename)

def calculateExel(fileName):
    rb = open_workbook(fileName)
    wb = copy(rb)

    ##获取sheet
    sheet = wb.get_sheet(0)
    print('nrows='+sheet.nrows)