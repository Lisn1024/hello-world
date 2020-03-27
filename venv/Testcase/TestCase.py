#导入包
import unittest,json
import time
import HTMLTestRunner
from common.Driver import Driver
from common.Driver import Driver
from common.MyTest import MyTest
from common.readexcel import readExcel
class HomeTest(MyTest):
 #用例：首页发布微头条
    # def test_weitoutiao(self):
    #     # 点击发布
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/byg").click()
    #     time.sleep(1)
    #     # 点击发微博
    #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
    #     time.sleep(2)
    #
    #     # 输入发布内容
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/a8j").send_keys("我要发微博，哈哈哈哈……")
    #     time.sleep(1)
    #     # 点击发布
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/cm4").click()
    #     time.sleep(2)

 # 搜索的测试用例（测试数据从excel中来）
    def test_sousuo(self):
        print(self._testMethodName)
        print(self.__class__.__name__)
        re = readExcel()
        text = re.read(
            classname = self.__class__.__name__,
            methodname = self._testMethodName
        )
        print(text)

        #定位搜索输入框
        self.driver.find_element_by_id("com.ss.android.article.news:id/crm").click()
        #输入搜索内容
        self.driver.find_element_by_id("com.ss.android.article.news:id/csp").send_keys(text)
        #点击搜索按钮
        self.driver.find_element_by_id("com.ss.android.article.news:id/cm6").click()
        time.sleep(6)


    # def test_sousuo1(self):
    #     print(self._testMethodName)
    #     print(self.__class__.__name__)
    #     re = readExcel()
    #     text = re.read(
    #         classname=self.__class__.__name__,
    #         methodname=self._testMethodName
    #     )
    #
    #     print(text)
    #
    #     # 定位搜索输入框
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/crm").click()
    #     # 输入搜索内容
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/csp").send_keys(text)
    #     # 点击搜索按钮
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/cm6").click()
    #     time.sleep(6)
    #
    # def test_sousuo2(self):
    #     print(self._testMethodName)
    #     print(self.__class__.__name__)
    #     re = readExcel()
    #     text = re.read(
    #         classname = self.__class__.__name__,
    #         methodname = self._testMethodName
    #     )
    #     print(text)
    #
    #     #定位搜索输入框
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/crm").click()
    #     #输入搜索内容
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/csp").send_keys(text)
    #     #点击搜索按钮
    #     self.driver.find_element_by_id("com.ss.android.article.news:id/cm6").click()
    #     time.sleep(6)



#启动driver
if __name__ == '__main__':
    unittest.main()
    #实例化TestSuit,创建测试套件
    # suite = unittest.TestSuite()
    # #addtest方法可以添加单个test开头的测试用例到测试套件
    # suite.addTest(HomeTest("test_weitoutiao"))
    # #实例化TextTestRunner
    # runner = unittest.TextTestRunner()
    # #调用run方法，运行测试套件
    # runner.run(suite)


