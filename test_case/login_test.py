from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time



class Login:
    def __init__(self, driver):
        self.driver = driver
        self.id_value = "1111111111"
        self.pw_value = "test12!@"
        self.lock_id = "1234562"
        self.withdrawal_id = "withdrawal"
        self.logo_image = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')))
        self.id_edit = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        self.pw_edit = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        self.view_pw_edit =  WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button")')))
        self.login_btn =  WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("로그인")')))
    
    def test_run(self):
        # self.test_login_description_check()
        # self.test_non_register_user_login()
        # self.test_different_password()
        # self.test_lock_user()
        # self.test_withdrawal_user()
        # self.test_login_sucess()
        self.test_save_user_id()
    
    def edit_data_input(self, *args):
        if len(args) == 1:
            self.id_edit.click()
            self.id_edit.send_keys(args[0])
            self.logo_image.click()
        elif len(args) == 2:
            self.id_edit.click()
            self.id_edit.send_keys(args[1])
            self.pw_edit.click()
            self.pw_edit.send_keys()
            self.logo_image.click()
        
    def return_popup(self):
        popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
        close_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        popup_elements = [popup, close_btn]
        
        return popup_elements
    
    def test_login_description_check(self):
        self.edit_data_input("","")
        id_desc = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("로그인 아이디를 입력해 주세요.")')))
        pw_desc = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("비밀번호를 입력해주세요")')))
        
        if id_desc.get_attribute("contentDescription") == "로그인 아이디를 입력해 주세요.":
            print("id description check")  
        if pw_desc.get_attribute("contentDescription") == "비밀번호를 입력해주세요":
            print("password description check")
        self.login_btn.click()

    def test_non_register_user_login(self):
        self.edit_data_input("error", "error")
        
        self.login_btn.click()
        
        non_register_popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
        close_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        if non_register_popup.get_attribute("contentDescription") == "가입된 회원이 아닙니다.":
            print("non-register popup desc check")
            close_btn.click()
        else:
            print("check popup")
            time.sleep(3)
            close_btn.click()
            
    def test_different_password(self):
        self.edit_data_input(self.id_value, "test")
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()
        
        if "비밀번호" in content_desc:
            print(f"Check if '비밀번호' is in contentDescription: {'비밀번호' in content_desc}")
            popup_elements[1].click()
        else:
            print("-------- test check -------")
            time.sleep(3)
            popup_elements[1].click()
    
    def test_lock_user(self):
        self.edit_data_input(self.lock_id,self.pw_value)
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()

        if content_desc == "로그인실패횟수5회가되어로그인이불가합니다.":
            print(f"Check if '로그인실패' is in contentDescription: {'로그인실패' in content_desc}")
            popup_elements[1].click()
        else:
            print("-------- test check -------")
        
    def test_withdrawal_user(self):
        self.edit_data_input(self.withdrawal_id, self.pw_value)
        self.login_btn.click()
        
        popup_elements = self.return_popup()
        content_desc = popup_elements[0].get_attribute("contentDescription").strip()
        print(content_desc)
        if content_desc == "탈퇴처리가 되어 로그인이 불가합니다.":
            print(f"Check if '탈퇴회원' is in contentDescription: {'탈퇴처리' in content_desc}")
            popup_elements[1].click()
        else:
            print("------ test check ------")
    
    
    def test_login_sucess(self):
        self.edit_data_input(self.id_value, self.pw_value) 
        password_hide_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        print(password_hide_btn.get_attribute("text"))        
        
        self.login_btn.click()
    

    def test_save_user_id(self):
        self.edit_data_input(self.id_value, self.pw_value)
        id_save_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox").instance(0)')))
        check_value = id_save_btn.get_attribute("checked")

        if check_value == "false":
            id_save_btn.click()
        
        self.login_btn.click()
        
        self.logout_user()
        if self.id_edit.get_attribute("text") == self.id_value:
            print("save check")
        else:
            print("-------test check")
        
        self.edit_data_input(self.id_value, self.pw_value)
        if check_value != "false":
            id_save_btn.click()
        self.login_btn.click()
        
        self.logout_user()
        if self.id_edit.get_attribute("text") == "":
            print("save check")
        else:
            print("--------test check")
    
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
        