# coding=utf-8
import unittest
import time
from common import HTMLTestRunner_PY3
import os
from BeautifulReport import BeautifulReport

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

# def run_case(all_case, reportpath=report_path):
#     '''执行所有的用例, 并把结果写入测试报告'''
#     htmlreport = reportpath+r"\result.html"
#     print("测试报告生成地址：%s"% htmlreport)
#     fp = open(htmlreport, "wb")
#     runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,
#                                                verbosity=2,
#                                                title="测试报告",
#                                                description="用例执行情况")
#
#     # 调用add_case函数返回值
#     runner.run(all_case)
#     fp.close()

def run_case(all_case, reportName="report"):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_path = os.path.join(curpath, reportName)  # 用例文件夹
    #调用BeautifulReport报告模板的方法  没有错误截图
    runner = BeautifulReport(all_case)
    runner.report(filename="report%s.html"%now, description='爱学习自动化测试报告', log_path=report_path)

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)

