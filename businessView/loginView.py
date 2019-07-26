# -*- coding:utf-8 -*-

import logging
import sys
import time

from selenium.common.exceptions import NoSuchElementException

sys.path.append("..")
from tools.common import Common
from selenium.webdriver.common.by import By
from tools.desired_caps import appium_desired


class LoginView(Common):

    # 手机号登陆按钮和手机号输入框是一个id
    iphoneSiginBtn = (By.ID,"tw.android.mingzhi.motv:id/phone")
    iphoneCode = "tw.android.mingzhi.motv:id/country_code"
    iphoneCode_ZH = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]"
    iphoneInput = (By.ID,"tw.android.mingzhi.motv:id/phone")
    pwd_Verif_Sign = (By.ID,"tw.android.mingzhi.motv:id/signin_password")
    pwdInput = (By.ID,"tw.android.mingzhi.motv:id/password")
    siginBtn = (By.ID,"tw.android.mingzhi.motv:id/signin")


    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()
        self.check_iphone()

        self.driver.find_element(*self.iphoneSiginBtn).click()

        # 定位并点击手机号区号
        logging.info("============find iphoneCode===============")
        time.sleep(0.5)
        self.driver.find_element_by_id(self.iphoneCode).click()

        # 选择手机号区号
        logging.info("============find&click iphoneCode_ZH===============")
        iphoneCode = self.driver.find_element_by_xpath(self.iphoneCode_ZH)
        time.sleep(0.5)
        iphoneCode.click()

        # 输入手机号
        logging.info("============find&send iphoneInput===============")
        time.sleep(0.5)
        self.driver.find_element(*self.iphoneInput).send_keys(username)

        # 判断是否存在密码登录按钮
        try:
            logging.info("============find pwd_Verif_Sign===============")
            time.sleep(0.5)
            SiginPwd = self.driver.find_element(*self.pwd_Verif_Sign)
        except NoSuchElementException:
            logging.info("no password Signin button")
        else:
            SiginPwd.click()

        # 输入密码
        logging.info("============find&send pwdInput===============")
        time.sleep(0.5)
        self.driver.find_element(*self.pwdInput).send_keys(password)

        # 登录按钮点击
        logging.info("============find&click siginBtn===============")
        time.sleep(0.5)
        self.driver.find_element(*self.siginBtn).click()





# if __name__ == '__main__':
    # driver = appium_desired()
    # login = LoginView(driver)
    # login.login_action('18403558945','111111Qq')




