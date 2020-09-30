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
from publicmethods.public import publicmethod
pub1 = publicmethod()
d = pub1.init_App()
d.app_start("com.creditease.vip_xzbx")
class Login:
    """
    正确账号密码登录
    """
    def __init__(self):
        self.username_element = "com.creditease.vip_xzbx:id/et_user_name"
        self.passwd_element = "com.creditease.vip_xzbx:id/et_pwd"
        self.login_button_element = "com.creditease.vip_xzbx:id/btnSignIn"
        self.mine_button_element = '//*[@resource-id="com.creditease.vip_xzbx:id/mainTabBar"]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
        self.workstudio_element = '//*[@resource-id="com.creditease.vip_xzbx:id/mainTabBar"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
        self.setting_element = "com.creditease.vip_xzbx:id/ivWorkRoomSetting"
        self.exit_element ="com.creditease.vip_xzbx:id/set_exitLy"
    def username_locate(self):
        d.clear_text()
        d(resourceId=self.username_element).send_keys(UserName)
    def passwd_locate(self):
        d(resourceId=self.passwd_element).clear_text()
        d(resourceId=self.passwd_element).send_keys(Passwd)
    def login_button(self):
        d(resourceId=self.login_button_element).click()
        d.implicitly_wait(5)
        d.screenshot()
        # assert d(resourceId="com.creditease.vip_xzbx:id/tab_icon").exists

    def mine(self):
        d.xpath(self.mine_button_element).click()
    def workstudio(self):
        # d(resourceId=self.workstudio_element).click()
        d.xpath(self.workstudio_element).click_exists()
    def setting(self):
       d(resourceId=self.setting_element).click_exists()
    def exit(self):
         d(resourceId=self.exit_element).click()
         d.app_stop("com.creditease.vip_xzbx")


