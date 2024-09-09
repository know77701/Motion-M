from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from utils.utils import *


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.utils= Utils(driver)
    
    def test_run(self):
        self.test_login_page_ui_check()
        # self.test_login_description_check()
        # self.test_non_register_user_login()
        # self.test_different_password()
        # self.test_lock_user()
        # self.test_withdrawal_user()
        # self.test_login_sucess()
        # self.test_save_user_id()
            
    def test_login_page_ui_check(self):
        view_list = self.utils.get_all_elements("android.view.View")
        btn_list = self.utils.get_all_elements("android.widget.Button")
        image_list = self.utils.get_all_elements("android.widget.ImageView")
        
        self.utils.compare_image(image_list[0],"test.png")
        
        for i,element in enumerate(view_list):
            print(i)
            print(element)
        for i,element in enumerate(btn_list):
            print(i)
            print(element)
        for i,element in enumerate(image_list):
            print(i)
            print(element)
        
        
    
    def test_login_description_check(self):
        self.edit_data_input("","")
        id_desc = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("로그인 아이디를 입력해 주세요.")')))
        pw_desc = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("비밀번호를 입력해주세요")')))
        
        assert id_desc.get_attribute("contentDescription") == "로그인 아이디를 입력해 주세요.", "id edit description Fail"
        assert pw_desc.get_attribute("contentDescription") == "비밀번호를 입력해주세요", "password edit description Fail"
        self.login_btn.click()

    def test_non_register_user_login(self):
        self.edit_data_input("error", "error")
        
        self.login_btn.click()
        
        non_register_popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
        close_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        assert non_register_popup.get_attribute("contentDescription") == "가입된 회원이 아닙니다.", "non-register popup desc check Fail"
        close_btn.click()
            
    def test_different_password(self):
        self.edit_data_input(self.id_value, "test")
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()
        
        assert "비밀번호" in content_desc, f"Check if '비밀번호' is in contentDescription: {'비밀번호' in content_desc}"
        popup_elements[1].click()
    
    def test_lock_user(self):
        self.edit_data_input(self.lock_id,self.pw_value)
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()

        assert content_desc == "로그인실패횟수5회가되어로그인이불가합니다.", f"Check if '로그인실패' is in contentDescription: {'로그인실패' in content_desc}"
        popup_elements[1].click()

    def test_withdrawal_user(self):
        self.edit_data_input(self.withdrawal_id, self.pw_value)
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()
        assert content_desc == "탈퇴처리가 되어 로그인이 불가합니다.",f"Check if '탈퇴회원' is in contentDescription: {'탈퇴처리' in content_desc}"
        popup_elements[1].click()
    
    def test_login_sucess(self):
        self.edit_data_input(self.id_value, self.pw_value) 
        password_hide_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        
        self.login_btn.click()

    def test_password_hidden(self):
        self.edit_data_input(self.id_value, self.pw_value)

    def test_save_user_id(self):
        self.edit_data_input(self.id_value, self.pw_value)
        id_save_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox").instance(0)')))
        check_value = id_save_btn.get_attribute("checked")

        if check_value == "false":
            id_save_btn.click()
        
        self.login_btn.click()
        
        self.logout_user()
        assert self.id_edit.get_attribute("text") == self.id_value, "id edit text check Fail"
        
        self.edit_data_input(self.id_value, self.pw_value)
        if check_value != "false":
            id_save_btn.click()
        self.login_btn.click()
        
        self.logout_user()
        assert self.id_edit.get_attribute("text") == "", "id edit text check Fail"
    
    def logout_user(self):
        setting_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
        setting_btn.click()
        
        login_menu = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("로그인")')))
        login_menu.click()
        
        logout_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("로그아웃")')))
        logout_btn.click()
        
        logout_popup_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')))
        logout_popup_btn.click()
        