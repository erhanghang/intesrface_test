# -*- coding:utf-8 -*-
#author:erhang
import xlrd  #读取excel
import xlwt  #写入excel
import openpyxl

class ExcelUtil():
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)

        #得到第一行标题
        self.row = self.table.row_values(0)
        #得到所有行
        self.rowNum = self.table.nrows
        #得到所有列
        self.colNum = self.table.ncols
        #定义当前列
        self.curRowNo = 1

    def read_excel(self):
        r=[]
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def write_excel(self, excelpath):
        '''excel中写入数据'''
        wb = openpyxl.Workbook(excelpath)
        sheet = wb.active #激活sheet页
        sheet.title = 'test'


# if __name__ == '__main__':
#     import os
#     curpath = os.path.dirname(os.path.realpath(__file__))
#     excelPath = os.path.join(curpath, 'test.xlsx')
#     excel = ExcelUtil(excelPath, 'test')
#     r = excel.read_excel()
#     print(r)