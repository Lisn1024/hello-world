from appium import webdriver
import time

class GetWebDriver(object):
    def __init__(self):
        print("启动中…")
        self.desire_caps = {
            "deviceName": "127.0.0.1:21503",
            # "deviceName": "d98c87ab",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            # "platformVersion": "4.3",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True
        }

        # 定义driver
    def startUP(self):
        driver  = webdriver.Remote("127.0.0.1:4723/wd/hub",*self.desire_caps)
        print("启动中，等待6秒")
        time.sleep(6)
        dri = driver
        return dri




if __name__ == '__main__':

    p = GetWebDriver()
    GetWebDriver.startUP(p)



