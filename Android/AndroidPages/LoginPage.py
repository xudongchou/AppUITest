"""
@project:AppUITest
@author:lenovo
@file:LoginPage.py
@ide:PyCharm
@time:2020/9/29 11:27
@month:九月

"""
import uiautomator2 as  u2
from settings.login_settings import UserName,Passwd
class Login:
    """
    正确账号密码登录
    """
    def __init__(self):
        self.username_element = "com.creditease.vip_xzbx:id/et_user_name"
        self.passwd_element = "com.creditease.vip_xzbx:id/et_pwd"
        self.login_button_element = "com.creditease.vip_xzbx:id/btnSignIn"
        self.mine_button_element = '//*[@resource-id="com.creditease.vip_xzbx:id/mainTabBar"]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
        self.app = u2.connect()
        self.app.app_start("com.creditease.vip_xzbx")

    def username_locate(self):
        self.app.clear_text()
        self.app(resourceId=self.username_element).send_keys(UserName)
    def passwd_locate(self):
        self.app(resourceId=self.passwd_element).clear_text()
        self.app(resourceId=self.passwd_element).send_keys(Passwd)
    def login_button(self):
        self.app(resourceId=self.login_button_element).click()
    def mine(self):
        self.app.xpath(self.mine_button_element).click()



