import unittest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from test_case.login_test import *
from test_case.sign_up_test import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

class mainTest(unittest.TestCase):
    def setUp(self):
        # app 실행 필요 시 주석 해제
        # app = os.path.join(os.path.dirname(__file__), 'C:/works/Motion_M/', 'motionm_240809.apk')
        # app = os.path.abspath(app)

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "13"
        options.device_name = "emulator-5554"
        options.automation_name = "UiAutomator2"
        # options.app = "C:/works/Motion_M/motionm_240809.apk"

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', options=options)
        
        

    def test_case_run(self):
        try:
            # login = Login(driver=self.driver)
            # login.test_run()
            sign_up = SignUp(driver=self.driver)
            sign_up.test_run()
        except Exception as e:
            print(f"Error occurred: {e}")
    
    def setting_test_case(self):
        try:
            

            time.sleep(1)
        except Exception as e:
            print(e)
            
                
    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()