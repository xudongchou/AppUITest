"""
@project:AppUITest
@author:lenovo
@file:public.py
@ide:PyCharm
@time:2020/9/29 16:04
@month:九月

"""
import time
import uiautomator2 as  u2
class publicmethod:
    def wait(self,ms):
        time.sleep(ms)
    def init_App(self):
        d = u2.connect()
        return d