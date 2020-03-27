'''
1-导入包
2-创建对象
3-读取内容
4-关闭
'''
import os

import configparser

class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(r'..\config.ini', encoding="utf-8-sig")

    def get_email(self,config):
        return self.cf.get("EMAIL",config)


if __name__ == '__main__':
    re = ReadConfig()
    print(re.get_email('mail_user'))