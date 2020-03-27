import unittest
import time
import os
import HTMLTestRunner
from common.configEmail import send_mail_html
#from common.send_fujian import ConfigEmail

file = r"C:\Users\Jason Lee\PycharmProjects\UIvip4test\venv\testReport\test.html"

def run_case(dir="Testcase"):
    case_dir = os.getcwd() + "\\" + dir
    print(case_dir)
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="TestCase.py",top_level_dir=None)
    return discover

if __name__ == '__main__':
    #current_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    report_path = os.getcwd() + "\\testReport\\test.html"
    print(report_path)
    #report_path = os.getcwd() + "\\testReport\\" + current_time + "test.html"
    fp = open(report_path,"wb")
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告",description=u"用例详情")
    runer.run(run_case())
    fp.close()
    send_mail_html(file)



