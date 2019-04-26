#encoding=UTF-8
'''
Created on 2016年9月4日

@author: shawn
'''
import openpyxl
'''
openpyxl 一些基本概念：
workbook 由 worksheets组成，worksheet包含columns rows，a  box at a particular row and columns is called a cell.
The grid of cell marks up a sheet.
'''

'''
问题：
print('row=s%,key=%s,value=%s' % (index,key,mapAver[key]))
ValueError: unsupported format character ',' (0x2c) at index 6
'''

'''
改进：1.异常不会捕捉，导致批量中一条出错整个程序抛出
      2.批量中  一定要通过异常捕捉到时哪一条引起的异常 打印对应的key值。
'''

'''
注意点：
openPyxl 只能操作xlsx后缀的excel文件不能操作xls后缀的
'''

def  testOpenPyXlFunction(fileName):
     wb = openpyxl.load_workbook(fileName)
     #Can 't convert 'list' object to str implicitly
     print(wb.get_sheet_names())

     '''改善print()不能自动把worksheet转化为str，也不能把lsit转化为str'''
     print('active sheet is :')
     print(wb.active)
     sheet = wb.active
     print('sheet A1.value' + sheet['A1'].value)
     c = sheet['B1']
     print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)

     ##print cell
     for i in range(1, 8, 2):
         print(i, sheet.cell(row=i, column=2).value)

     a1c3 = tuple(sheet['A1':'C3'])
     print('alc3_tuple=')
     print(a1c3)







