# -*- coding:utf-8 -*-
#author:erhang
import requests
from interface.glzx.login_inter.login_interface import login_inter
from common.conf.readconfig import ReadConfig
from common.logger import Log
log=Log()

readconfig = ReadConfig()
glzx_host = readconfig.get_http("glzx")
get_ins_list_url = readconfig.get_url('get_ins_list_url')
get_area_list_url = readconfig.get_url('get_area_list_url')

class Ins_New(object):
    def __init__(self, s):
        self.s = s

    def get_ins_list(self):
        '''获取机构列表'''
        url = glzx_host+get_ins_list_url
        r = self.s.get(url)
        res = r.json()
        assert res["status"] == 1 and res["errorCode"] == 0 and r.status_code == 200, '获取机构列表失败'
        log.info(res)

    def get_area_list(self):
        '''机构列表-地区列表'''
        url = glzx_host+get_area_list_url
        r =self.s.get(url)
        res = r.json()
        assert res["status"] == 1 and res["errorCode"] == 0 and r.status_code == 200, "获取地区列表失败"
        log.info(res)

if __name__=='__main__':
    login=login_inter()
    session=login.glzx_login_inter()
    getarea=Ins_New(session)
    getarea.get_area_list()




