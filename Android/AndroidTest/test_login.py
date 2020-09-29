"""
@project:AppUITest
@author:lenovo
@file:test_login.py
@ide:PyCharm
@time:2020/9/29 15:41
@month:九月

"""
import sys
sys.path.append("..")
import unittest
from Android.AndroidPages.LoginPage import Login
from publicmethods.public import publicmethod
class TestLogin(unittest.TestCase):
    """
    正确的用户名和密码登录
    """
    def test_login1(self):
      login = Login()
      pub = publicmethod()
      pub.wait(10)
      login.mine()
      login.username_locate()
      login.passwd_locate()
      login.login_button()

if __name__ =="__main__":
    unittest.main()
