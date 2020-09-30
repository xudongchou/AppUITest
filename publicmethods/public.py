"""
@project:AppUITest
@author:lenovo
@file:public.py
@ide:PyCharm
@time:2020/9/29 16:04
@month:九月

"""
import time,datetime
import os
import uiautomator2 as  u2
class publicmethod:
    def wait(self,ms):
        time.sleep(ms)
    def init_App(self):
        d = u2.connect()
        return d
    def Screenshot(self):
       nowtime = datetime.now()
       stringtime = datetime.strftime(nowtime, "%Y%m%d%H%M%S")
       basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
       dir_name = "/ScreenShot/"
       # filename=stringtime+".png"
       path_dir = basedir + dir_name
       p = publicmethod()
       image = p.screenshot()
       image.save(path_dir+stringtime+'.png')

