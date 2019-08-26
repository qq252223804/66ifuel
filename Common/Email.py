# -*- coding: utf-8 -*- 
# @Time : 2018/12/24 15:51 
# @Author : taojian 
# @File : Email.py
# coding:utf-8
import smtplib, os, time
from email.mime.text import MIMEText  # 发送文本模块
from email.mime.multipart import MIMEMultipart  # 发送附件模块
from Common.log import Log


# file_path = ('{}').format(os.path.join(os.getcwd(),'Report_html')+'\测试报告.html')
# print(file_path)
# print (os.getcwd())#获取当前文件所处的总目录
# print(os.path.abspath(os.path.dirname(__file__))) # 获取当前文件所在目录

def send_email(file_path):
    # ----------1.跟发件相关的参数------
    # smtpserver  # 发件服务器
    smtpserver = "smtp.qq.com"
    port = 465  # 端口
    sender = "252223804@qq.com"  # 账号
    shouquan = "rpybibdelqojbgfc"  # 授权码  qq邮箱
    receiver = ["252223804@qq.com"]  # 接收人

    # ----------2.编辑邮件的内容------

    subject = "主题:66ifuel接口测试报告"
    msg = MIMEMultipart('alternative')
    msg['from'] = sender
    msg['to'] = ";".join(receiver)  # 发送多个接收人
    msg['subject'] = subject
    with open(file_path, 'rb') as fb:
        mail_body = fb.read()

    # # 定义邮件正文为 html 格式
    # body = MIMEText(mail_body, 'html', 'utf-8')
    # msg.attach(body)
    # # 定义邮件正文为 text 格式
    msg.attach(MIMEText('请下载html附件进行查看', 'plain', 'utf-8'))

    # 	#附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'  # 重命名的邮件
    msg.attach(att)
    #
    #
    # 	# ----------3.发送邮件163------
    # smtp = smtplib.SMTP()
    # smtp.connect(smtpserver)  # 连服务器
    try:
        # # ----------4.发送邮件QQ------
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, shouquan)  # 登录

        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.quit()  # 关闭
    except Exception as e:
        # print(e)
        Log().warning('邮件发送失败:%s' % e)

# send_email(file_path)
#