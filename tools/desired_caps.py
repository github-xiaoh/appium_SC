# -*- coding:utf-8 -*-

import yaml
import logging.config
from appium import webdriver


CON_LOG = "../config/log.config"
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():

    # 读取配置文件
    with open('../config/desiredInfo.yaml','r') as f :
        desired_caps_data = yaml.load(f)

    # 配置参数
    desired_caps = {}
    desired_caps['platformName'] = desired_caps_data['platformName']
    desired_caps['platforVersion'] = desired_caps_data['platforVersion']
    desired_caps['deviceName'] = desired_caps_data['deviceName']
    # desired_caps['deviceName'] = "CLB0218522012520"

    desired_caps['app'] = desired_caps_data['app']
    desired_caps['appPackage'] = desired_caps_data['appPackage']
    desired_caps['appActivity'] = desired_caps_data['appActivity']
    desired_caps['noReset'] = desired_caps_data['noReset']  # 是否记录当前会话（false相当于新安装打开app，true表示已经打开过）

    # desired_caps['unicodeKeyboard'] = 'true'    # 中文输入字符编码乱码问题
    desired_caps['resetKeyboard'] = desired_caps_data['resetKeyboard']  # 键盘清空

    logging.info("start run app······")
    driver = webdriver.Remote("http://"+str(desired_caps_data['ip'])+':'+str(desired_caps_data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(2)

    return driver




# if __name__ == '__main__':
#     appium_desired()