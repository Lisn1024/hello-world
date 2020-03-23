from appium import webdriver
import time


def Driver():
    print("启动中…")

    desire_caps = {
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
    driver  = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
    print("启动中，等待6秒")
    time.sleep(6)
    return driver

if __name__ == '__main__':
    pass

    # driver = Driver()

    # driver.find_element_by_id("com.ss.android.article.news:id/byg").click()
    # time.sleep(3)
    # driver.quit()

