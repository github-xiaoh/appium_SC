# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage



# my_sender = '443990096@qq.com'  # 发件人邮箱账号
# my_pass = 'btsfupcotihybhhj'  # 发件人邮箱密码
# my_user = 'chenhang@smartcinema.com.cn'  # 收件人邮箱账号，我这边发送给自己

# 发送邮箱用户名、账号/密码
# user_email = '小h'                        # 发件人邮箱昵称
# sender_email = '443990096@qq.com'         # 收件人邮箱账号
# password_email = 'btsfupcotihybhhj'       # 发件人邮箱密码

# 收件人邮箱
# 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
# receiver_email = ['443990096@qq.com', 'chenhang@smartcinema.com.cn']

# receiver_email = 'chenhang@smartcinema.com.cn'





def mail(user_email,sender_email,password_email,receiver_email,reportHtml):
    ret = True
    try:

        # 编写 HTML类型的邮件正文
        # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
        #    msg = MIMEText(mail_body,'html','utf-8')

        msg = MIMEMultipart('mixed')

        # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
        #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
        # 中文测试ok
        #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
        #    msg_plain = MIMEText(text,'plain', 'utf-8')
        #    msg.attach(msg_plain)

        msg_html1 = MIMEText(reportHtml, 'html', 'utf-8')     # 文本模式将html改成plain
        msg.attach(msg_html1)

        msg_html2 = MIMEText(reportHtml, 'html', 'utf-8')     # 文本模式将html改成plain
        msg_html2["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html2)



        msg['From'] = formataddr([user_email, sender_email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(["云途时代测试", receiver_email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        # 多个收件人
        msg['To'] = ";".join(receiver_email)
        msg['Subject'] = Header("appium自动化测试报告", 'utf-8')   # 邮件的主题，也可以说是标题
        # msg['Subject'] = "接口测试报告"  # 邮件的主题，也可以说是标题


        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender_email, password_email)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender_email,receiver_email, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret




# from fileOperation import openFile
#
# reportHtml = openFile("/Users/chenhang/Desktop/pythonFile/python/untitled/practice/三角形判断/report/2019-03-55-14_55_24requort.html")
# retMail=mail(user_email,sender_email,password_email,receiver_email,reportHtml)
# if retMail:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")






# import smtplib
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = '443990096@qq.com'
# receivers = ['chenhang@smartcinema.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# msgRoot = MIMEMultipart('related')
# msgRoot['From'] = Header("菜鸟教程", 'utf-8')
# msgRoot['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# msgRoot['Subject'] = Header(subject, 'utf-8')
#
# msgAlternative = MIMEMultipart('alternative')
# msgRoot.attach(msgAlternative)
#
# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
# <p>图片演示：</p>
# <p><img src="cid:image1"></p>
# """
# msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
#
# # 指定图片为当前目录
# fp = open('test.jpg', 'rb')
# msgImage = MIMEImage(fp.read())
# fp.close()
#
# # 定义图片 ID，在 HTML 文本中引用
# msgImage.add_header('Content-ID', '<image1>')
# msgRoot.attach(msgImage)
#
#
#
# # 构建附件
# text_html = MIMEText(mail_msg, 'html', 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="text.html"'
# msgRoot.attach(text_html)
#
#
#
#
# try:
#     smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     smtpObj.login(sender,"btsfupcotihybhhj")
#     smtpObj.sendmail(sender, receivers, msgRoot.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
#



