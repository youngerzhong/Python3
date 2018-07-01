#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
workbook = xlrd.open_workbook('1.xlsx') #打开excel表
print(workbook.sheet_names()) #打印excel表工作簿的名字:Sheet1
mysheet = workbook.sheet_by_name('Sheet1')  #跟据工作簿的名字获取sheet内容
print(mysheet.name, mysheet.nrows, mysheet.ncols)
rows = mysheet.row_values(5) #行
cols = mysheet.col_values(2) #列
print(rows, cols)