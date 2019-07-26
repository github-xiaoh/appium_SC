# -*- coding:utf-8 -*-

import sys
import time

sys.path.append("..")
from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from tools.desired_caps import appium_desired




class Common(BaseView):
    cancelBtn = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
    skipBtn = (By.ID,'tw.android.mingzhi.motv:id/ll_advertise_time')
    iphoneSiginBtn = (By.ID,"tw.android.mingzhi.motv:id/phone")
    myBtn = (By.ID,"tw.android.mingzhi.motv:id/me_img")
    logoutBtn = (By.ID,"tw.android.mingzhi.motv:id/ll_no_login_layout")


    # 检测启动权限按钮
    def check_cancelBtn(self):
        logging.info("============check_cancelBtn===============")
        while True:
            try:
                # 隐式等待
                # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))
                cancelBtn = self.driver.find_element(*self.cancelBtn)
                logging.info("find cencelBtn")
            except NoSuchElementException:
                logging.info("no cancel")
                break
            else:
                cancelBtn.click()


    def check_skipBtn(self):
        logging.info("============check_skipBtn===============")
        # 检测启动图跳过按钮
        try:
            logging.info("check skip")
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("no ship")
        else:
            skipBtn.click()
            logging.info("click skip")


    def check_iphone(self):
        logging.info("============check_iphoneSiginBtn==============")
        # 判断是否有手机号登陆选项
        try:
            time.sleep(1)
            iphoneId = self.driver.find_element(*self.iphoneSiginBtn)
        except NoSuchElementException:
            logging.info("============no phone sigin")
            time.sleep(1)
            self.driver.find_element(*self.myBtn).click()
            time.sleep(2)
            self.driver.find_element(*self.logoutBtn).click()
        else:
            iphoneId.click()

    def get_win_size(self):
        logging.info("============get windows size==============")
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeUp(self):
        logging.info("============get swipee==============")
        winSize = self.get_win_size()
        x1 = int(winSize[0] * 0.5)
        y1 = int(winSize[1] * 0.8)
        x2 = int(winSize[0] * 0.5)
        y2 = int(winSize[1] * 0.2)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def close_app(self):
        self.driver.close_app()




# if __name__ == '__main__':
#     driver = appium_desired()
#     com = Common(driver)
#     com.check_cancelBtn()
#     com.check_skipBtn()
#
#     time.sleep(0.5)
#     for i in range(2):
#         com.swipeUp()
#         time.sleep(1)



