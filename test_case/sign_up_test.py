from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class SignUp:
    def __init__(self, driver):
        self.driver = driver
        # self.sign_up_btn = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("회원가입 ")')))
        # self.sign_up_btn.click()
        self.sing_up_titlt = "회원가입"
        self.terms_title = "모션 M 이용약관" 
        self.all_check_title = "전체 동의"
        self.essential_service_check_title = "[필수] 서비스 이용 약관"
        self.essential_private_check_title = "[필수] 개인정보 수집 및 이용 동의"
        self.select_chekc_title = "[선택] 마케팅 수신 동의"
        self.fr_sub_title = "휴대폰 인증"
        self.sec_sub_title = "본인 명의의 휴대폰 번호로 인증합니다."
        self.th_sub_title = "타인 명의 휴대폰, 법인폰을 이용자는 본인인증이 불가합니다."
    
    def test_run(self):
        self.test_ui_check()
        return
    
    def get_all_elements(self, class_name):
        elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("{class_name}")')))
        return elements
    
    def test_ui_check(self):
        element_list = []
        detail_back_btn = None
        view_elements = self.get_all_elements("android.view.View")
        check_box_elements = self.get_all_elements("android.widget.CheckBox")
        btn_elements = self.get_all_elements("android.widget.Button")
        for i, element in enumerate(view_elements):
            content_desc = element.get_attribute("contentDescription")
            if content_desc != '':
                element_list.append(content_desc)
            if i == 8 :
                essential_service_detail = element
            if i == 10 :
                essential_user_detail = element
            if i == 12 :
                select_service_detail = element
                
                
        # for i, element in enumerate(check_box_elements):
        #     content_desc = element.get_attribute("contentDescription")
        #     print(i)
        #     print(content_desc)
        # for i, element in enumerate(btn_elements):
        #     content_desc = element.get_attribute("contentDescription")
        #     if content_desc == "Back":
        #         back_btn = element
        #     elif content_desc == "휴대폰 번호 인증":
        #         auth_btn = element
        #     print(i)
        #     print(content_desc)
        titles = [
            self.sing_up_titlt, 
            self.terms_title, 
            self.all_check_title, 
            self.essential_service_check_title, 
            self.essential_private_check_title,
            self.select_chekc_title,
            self.fr_sub_title,
            self.sec_sub_title,
            self.th_sub_title
        ]

        if any(element in titles for element in element_list):
            print("check ui title")
        
        if essential_service_detail is not None:
            essential_service_detail.click()
            service_page = self.get_all_elements("android.view.View")
            btn_elements = self.get_all_elements("android.widget.Button")
            for element in btn_elements:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "Back":
                    detail_back_btn = element
            for element in service_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "서비스 이용 약관":
                    print("essential service detail view check")
                    detail_back_btn.click()
                    break
        if essential_user_detail is not None:
            essential_user_detail.click()
            
        
        # back_btn.click()
        # auth_btn.clcik()
        
    