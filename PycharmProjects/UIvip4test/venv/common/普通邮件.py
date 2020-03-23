import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
'''发送html附件形式邮件'''
# 第一步：配置邮箱属性
# 发送邮箱
sender = 'lishengnantest@163.com'
# 接收邮箱
receiver = '18332300241@163.com'
# receiver = ['xxaugus@163.com','xxaugus@163.com']#使用该方法，可发送给多人
# 发送邮件主题
localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
subject = '自动化测试结果_' + localTime
content = '玩安卓接口测试结果已发送，详见附件，请查收！'  # 邮件正文内容
# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
username = 'lishengnantest@163.com'
password = 'l19921024'
class sendEmailAttachment(object):
    def __init__(self):
        pass
    def send_mail_html(self,file):
    # 读取html文件内容
        with open(file,'rb') as f:
            mail_body = f.read()
        # 组装邮件内容和标题，中文需参数‘utf-8’
        body= MIMEText(content, 'html', 'utf-8')#该处为添加邮件正文
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver#收件人为单人
        #msg['To'] = ';'.join(receiver)#与前面发送多人结合使用
        msg.attach(body)#添加正文内容
        # 添加附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # att["Content-Disposition"] = 'attachment; filename={}.html'.format(file)#添加文件、及文件名后缀名
        att["Content-Disposition"] = 'attachment; filename={}'.format(file)  # 直接添加文件
        msg.attach(att)
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

    def find_new_file(self, test_report):
        '''查找目录下最新的文件'''
        file_lists = os.listdir(test_report)  # 打开报告目录
        file_lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn)
        if not os.path.isdir(test_report + "\\" + fn)
        else 0)
        # print('最新的文件为： ' + file_lists[-1])
        file = os.path.join(test_report, file_lists[-1])  # 获取最新文件
        print('完整文件路径：', file)  # 打印路径
        return file

    if __name__ == '__main__':
        addAttachment = sendEmailAttachment()  # 实例化发带附件类
        testReport = r'G:\code\interfaceTest\testReport'  # 指定文件目录
        file_name = addAttachment.find_new_file(testReport)  # 查找最新的html文件
        # 将上述调用注释，直接找到文件路径可发送选择文件
        # file_name = r'G:\code\interfaceTest\testReport\test2020-01-11-22-05-01.html'
        addAttachment.send_mail_html(file_name)  # 发送html内容邮件