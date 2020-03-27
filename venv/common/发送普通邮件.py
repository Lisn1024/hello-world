#coding:utf-8
from smtplib import SMTP

# 发送html内容的邮件
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
def sendMail():

    '''发送html内容邮件'''
    #第一步：配置邮箱属性

    # 发送邮箱
    sender = 'lisn1024@126.com'
    # 接收邮箱
    receiver = '1473147172@qq.com'

    # 发送邮箱服务器
    smtpserver = 'smtp.126.com'
    # 发送邮箱用户/密码
    username = 'lisn1024'
    #SMTP服务在客户端开启后，会给一个登录授权码，在第三方登录时登录密码需要填写授权码
    password = 'UVUVZLOALHEAAQQB'
    #content = 'Python 邮件发送测试...'
    # 发送邮件主题
    #t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试结果'
    content = 'Python 邮件发送测试...'
    #第二步： 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(content)
    #msg['Subject'] = Header(subject, 'utf-8')
    msg["subject"] = subject
    msg['From'] = sender
    msg['To'] = receiver

    #第三步：登录并发送邮件
    try:
        #1--实例化smtp类
        s = smtplib.SMTP()
        #2--连接stmp服务器
        s.connect(smtpserver)
        #3--登录邮箱
        s.login(username, password)
        #4--设置发件人，收件人，邮件内容
        s.sendmail(sender, receiver, msg.as_string())
        print("成功")

    except Exception as e:
        print("失败")

    finally:
        s.quit()

#调试发送邮件
sendMail()