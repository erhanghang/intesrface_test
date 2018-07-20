#-*- coding:utf-8 -*-
#author:yupeng
import unittest
from interface.glzx.login_inter.login_interface import login_inter
from interface.glzx.ins_manage.ins_new.get_ins_list import Ins_New
from common.logger import Log

class Test_QueryIns(unittest.TestCase):
    def setUp(self):
        '''登录接口'''
        login = login_inter()
        session = login.glzx_login_inter()#登录获取token
        self.newins = Ins_New(session)

    def test_getinslist(self):
        '''获取机构列表'''
        self.newins.get_ins_list()

    def test_getarealist(self):
        '''获取地区列表'''
        self.newins.get_area_list()

    def tearDown(self):
        print("执行完成")

if __name__ == '__main__':
    unittest.main(warnings='ignore')