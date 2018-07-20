# -*- coding:utf-8 -*-
#author:erhang
import unittest
import os
from ddt import ddt,unpack,data
from read_excel.excelunit import ExcelUtil

#采用ddt配合excel来做数据管理

curpath = os.path.dirname(os.path.realpath(__file__))
excelpath = os.path.join(curpath, 'test.xlsx')#加载excel路径

excel = ExcelUtil(excelpath, 'test')    #test为sheet页命名       excel为实例化的对象

@ddt
class datatest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')
    @classmethod
    def tearDownClass(cls):
        print('stop')
    @data(*excel.read_excel())         #实例化的excel加载类方法实现数据提取
    def test(self, data):   #这个data随意命名，使用时使用这个命名就OK
        print(data)

if __name__ == '__main__':
    unittest.main()
