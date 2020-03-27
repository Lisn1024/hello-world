from common.Driver import Driver
import unittest,json
import time
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.launch_app()

        def tearDown(self):
            self.driver.close_app()

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
