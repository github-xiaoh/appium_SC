# -*- coding:utf-8 -*-
import datetime
import time
import logging
import unittest
import sys
sys.path.append("..")
from tools.fileOperation import newFile, openFile
from tools.sendEmail import mail
from BeautifulReport import BeautifulReport

# 用例存放位置

test_case_path="../testCase"
# 测试报告存放位置
reportPath='../report/'
# 测试报告名称
now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
# now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = reportPath + now_time + 'requort.html'
#用例名称
description='smartCinema_TW '
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern="*.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename,description=description,log_path=reportPath)



    '''发送邮件'''

    # 创建email_content容器
    email_content = {}


    # 读取最新报告路径
    reportPath2 = newFile(reportPath)
    email_content['reportPath'] = reportPath2
    print("测试报告路径："+"\n" + reportPath2)

    # 读取最新报告内容
    reportHtml = openFile(reportPath2)
    email_content['reportHtml'] = reportHtml
    # print("测试报告内容："+"\n" + reportHtml)


    '''将获取的报告内容发送邮件'''

    # 发送邮箱用户名、账号/密码
    user_email = '小h'                        # 发件人邮箱昵称
    sender_email = '443990096@qq.com'         # 收件人邮箱账号
    password_email = 'btsfupcotihybhhj'       # 发件人邮箱密码

    # 收件人邮箱
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver_email = ['chenhang@smartcinema.com.cn']
    # receiver_email = 'chenhang@smartcinema.com.cn'
    # receiver_email = 'shaomingbo@smartcinema.com.cn'
    # receiver_email = '1779505264@qq.com'





    retMail = mail(user_email,sender_email,password_email,receiver_email,reportHtml)
    if retMail:
        logging.info("========邮件发送成功========")
    else:
        logging.info("========邮件发送失败========")



    logging.info("========邮件发送内容=======")
    logging.info(email_content)
    logging.info("========邮件发送内容=======")
