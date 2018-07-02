#!/usr/bin/env python
# -*- coding:utf-8 -*-
from xlutils.copy import copy
import xlrd, xlwt
workbook = xlrd.open_workbook('1.xlsx', formatting_info=True) #打开excel文件
print(workbook.sheet_names()) #打印出获取到的全部表
mysheet = workbook.sheet_by_name('Sheet1')  #跟据工作簿的名字获取sheet内容
# print(mysheet.name, mysheet.nrows, mysheet.ncols)
# rows = mysheet.row_values(5) #行
# cols = mysheet.col_values(2) #列
# for i in range(5,mysheet.nrows-4): #遍历行列表数据(获取需要的数据范围)
#     print(mysheet.row_values(i))

# print(mysheet.cell(5,9).value)
# print(mysheet.row(5)[2].value)
# up = mysheet.cell(5,7).value
# down = mysheet.cell(6,7).value
# print(up)
# print(down)
# if up ==r'√'and down ==r'旷':
#     up = r'》'
# print(up)
mysheet_len = len(mysheet.row_values(5))
# print(a)
# for i in range(4,mysheet_len-10):
#     print(mysheet.row_values(5)[i],end='')
# print('')
# for b in range(4,mysheet_len-10):
#     print(mysheet.row_values(6)[b],end='')
# for i in range(4,mysheet_len-10):
#     if mysheet.row_values(5)[i] == r'√' and mysheet.row_values(6)[i] == r'旷':
#         print(mysheet.row_values(5)[i] == r'√')

bookTag = copy(workbook)
sheetTag = bookTag.get_sheet(0)

# sheetTag.write(0, 0, '第一行，第一列')
# sheetTag.write(0, 1, '第一行，第二列')

# 循环
for r in range(5, mysheet.nrows-2, 2):
    for i in range(4, mysheet_len-10):
        tag = mysheet.row_values(r)[i]
        if mysheet.row_values(r)[i] == r'√' and mysheet.row_values(r+1)[i] == r'旷':
            tag = r'>'
        if mysheet.row_values(r)[i] == r'旷' and mysheet.row_values(r+1)[i] == r'√':
            tag = r'<'
        sheetTag.write(r, i, tag)

bookTag.save(r'demo.xls')

