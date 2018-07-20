# -*- coding:utf-8 -*-
#author:erhang

#暂时不用，稍后有需求再使用，主要是用来封装get、post方法，将请求入参做管理（现在一些情况下用不到该类）

import requests
from common.conf import readconfig
from common.logger import Log

localReadConfig = readconfig.ReadConfig()

class ConfigHttp:
    def __init__(self,baseurl):
        global host, port, timeout
        host = localReadConfig.get_http(baseurl)#在配置文件中取对应系统的baseurl
        #port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url
        return self.url
    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.log.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.log.error("Time out!")
            return None


# if __name__ == '__main__':
#     ch=ConfigHttp('axx')
