# -*- coding:utf-8 -*-


import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait   # 显示等待导入
from selenium.common.exceptions import TimeoutException   # 错误异常
from selenium.common.exceptions import NoSuchElementException



def login(driver):


    driver.find_element_by_id("tw.android.mingzhi.motv:id/phone").click()

    # 截图到当前脚本目录图片
    driver.save_screenshot("login1.png")

    # 定位并点击手机号区号
    time.sleep(0.5)
    driver.find_element_by_id('tw.android.mingzhi.motv:id/country_code').click()

    # 选择手机号区号
    iphoneCode = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]")
    time.sleep(0.5)
    iphoneCode.click()

    # 输入手机号
    time.sleep(0.5)
    driver.find_element_by_id('tw.android.mingzhi.motv:id/phone').send_keys("18403558945")

    # 判断是否存在密码登录按钮
    try:
        time.sleep(0.5)
        SiginPwd = driver.find_element_by_id("tw.android.mingzhi.motv:id/signin_password")
    except NoSuchElementException:
        print("no password Signin button")
    else:
        SiginPwd.click()

    # 截图到指定文件夹目录图片
    time.sleep(0.5)
    driver.get_screenshot_as_file(
        r"/Users/chenhang/Desktop/pythonFile/python/untitled/appium/appium_test/screenshot/image/login2.png")

    # 输入密码
    time.sleep(0.5)
    driver.find_element_by_id('tw.android.mingzhi.motv:id/password').send_keys("111111Qq")


    # 登录按钮点击
    time.sleep(0.5)
    driver.find_element_by_id('tw.android.mingzhi.motv:id/signin').click()


def check_cancelBtn():
    print('check cancelBtn')
    while True:
        try:
            # 隐式等待
            # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))
            cancelBtn = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
            print("已找到")
        except NoSuchElementException:
            print("no cancel")
            break
        else:
            cancelBtn.click()



# 主程序

# 配置参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platforVersion'] = '6.0.1'
desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['deviceName'] = "CLB0218522012520"

desired_caps['app'] = r'/Users/chenhang/Desktop/台湾版0717.apk'
desired_caps['appPackage'] = 'tw.android.mingzhi.motv'
desired_caps['appActivity'] = 'tw.android.mingzhi.motv.mvp.ui.activity.SplashActivity'
desired_caps['noReset'] = 'false'   # 是否记录当前会话（false相当于新安装打开app，true表示已经打开过）

# desired_caps['unicodeKeyboard'] = 'true'    # 中文输入字符编码乱码问题
desired_caps['resetKeyboard'] = 'true'      # 键盘清空

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




# 运行用例


# 检测权限弹窗
time.sleep(3)
check_cancelBtn()

# 检测启动图跳过按钮
try:
    print("check skip")
    skip = driver.find_element_by_id("tw.android.mingzhi.motv:id/ll_advertise_time")
except NoSuchElementException:
    print("no skip")
else:
    skip.click()
    print("click skip")

# 判断是否有手机号登陆选项
try:
    time.sleep(1)
    iphoneId = driver.find_element_by_id("tw.android.mingzhi.motv:id/phone")
except NoSuchElementException:
    print("no phone sigin")
    time.sleep(1)
    driver.find_element_by_id("tw.android.mingzhi.motv:id/me_img").click()
    time.sleep(2)
    driver.find_element_by_id("tw.android.mingzhi.motv:id/ll_no_login_layout").click()
else:
    iphoneId.click()

login(driver)


# 等待3s后退出会话
time.sleep(5)
driver.quit()