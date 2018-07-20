#-*- coding:utf-8 -*-
#author:yupeng
import requests
from common.conf.readconfig import ReadConfig
readconfig=ReadConfig()

class login_inter(object):
    def glzx_login_inter(self):
        '''管理中心登录接口'''
        s = requests.session()
        glzx_host = readconfig.get_http("glzx")
        login_url = glzx_host+"/surrogates/manage/passwordLogin"

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

        body = {
            'username': '%s'%readconfig.get_glzx_login("username"),
            'password': '%s'%readconfig.get_glzx_login("password")
        }

        r = s.post(login_url, headers=header, data=body)
        res = r.json()
        assert res["status"] == 1 and res["errorCode"] == 0 and r.status_code == 200, "登录失败"
        #获取token
        token = res["body"]["token"]
        token_m = token.replace(',', '%2C')
        header_add = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
             "Cookie": "token_m=%s" % token_m
        }
        s.headers.update(header_add)
        return s

    def new_glzx_login_inter(self):
        '''新管理中心登录接口'''
        newglzx_host = readconfig.get_glzx_login("new_glzx")
        login_url = newglzx_host+"/surrogates/manage/passwordLogin"
        s = requests.session()
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

        body = {
            'username': '%s'%readconfig.get_glzx_login("username"),
            'password': '%s'%readconfig.get_glzx_login("password")
        }

        r = s.post(login_url, headers=header, data=body)
        res = r.json()
        assert res["status"] == 1 and res["errorCode"] == 0 and r.status_code == 200, "登录失败"
        #获取token
        token = res["body"]["token"]
        token_m = token.replace(',', '%2C')
        header_add = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
             "Cookie": "token_m=%s" % token_m
        }
        s.headers.update(header_add)
        return s

if __name__ == '__main__':
    login = login_inter()
    s = login.glzx_login_inter()
    print(s)

