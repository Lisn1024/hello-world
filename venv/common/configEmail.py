#coding:utf-8
# 发送html内容的邮件
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig1 import ReadConfig

def send_mail_html(file):

    '''发送html内容邮件-非附件形式，即直接在邮件中显示html'''
    #第一步：配置邮箱属性
    # re = ReadConfig()
    # sender = re.get_email("sender")
    # print(sender)
    # receiver = re.get_email("receiver")
    # print(receiver)
    #
    # smtpserver = re.get_email("mail_host")
    # print(smtpserver)
    # username = re.get_email("mail_user")
    # print(username)
    # password = re.get_email("mail_pass")
    # print(password)

    # 发送邮箱
    sender = 'lisn1024@126.com'
    # 接收邮箱
    receiver = '1473147172@qq.com'
    # 发送邮件主题
    #current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    subject = '自动化测试结果_'
    # 发送邮箱服务器
    smtpserver = 'smtp.126.com'
    # 发送邮箱用户/密码
    username = 'lisn1024'
    password = 'UVUVZLOALHEAAQQB'

    # 读取html文件内容

    f = open(file, 'rb')
    mail_body = f.read()
    f.close()

    # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
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
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        s.quit()


if __name__ == '__main__':
    
    file = r"E:\code\person\UI_appium\hello-world\PycharmProjects\UIvip4test\venv\testReport\test.html"
    send_mail_html(file)  # 发送html内容邮件
