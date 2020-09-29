"""
@project:AppUITest
@author:lenovo
@file:run_test.py
@ide:PyCharm
@time:2020/9/29 10:06
@month:九月

"""
from BeautifulReport import BeautifulReport as bf
import unittest
import os
local_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\test"
report_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\reports"
print(local_dir)


if  __name__ =="__main__":
    testsuite = unittest.defaultTestLoader.discover(local_dir,pattern='test*.py')
    result = bf(testsuite)
    report= result.report(description="测试报告",filename="自动化报告",log_path=report_dir)
