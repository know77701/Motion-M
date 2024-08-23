import unittest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from test_case.login_test import *

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
            login = Login(driver=self.driver)
            login.login_test()
            
            # setting_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
            # setting_btn.click()

            # back_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")')))
            # back_btn.click()

            # description_text =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("트라이업영문")')))
            # if description_text:
            #     print("back_btn action check")
            
            # status_setting_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')))
            
            
            # not_status = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(0)')))
            # bust_status = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')))
            # metting_status = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(2)')))
            # available_status = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')))
            
            
            # home_depth_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)')))
            
            # message_depth_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)')))
            # message_depth_btn.click()
            # message_depth_btn =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)')))
            
            # message_room =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(7)')))
            # message_room.click()
            # message_edit =  WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')))
            # print(message_edit)            
            # send_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
            # index_value = 10
            
            # message_edit.click()
            # send_btn.send_keys("테스트")
            # send_btn.click()

            
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