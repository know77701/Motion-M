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
        # self.test_detail_ui_check()
        self.test_checkbox_control()
        return
    
    def get_all_elements(self, class_name):
        elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("{class_name}")')))
        return elements
    
    def test_checkbox_control(self):
        check_box_elements = self.get_all_elements("android.widget.CheckBox")
        btn_elements = self.et_all_elements("android.widget.Button")
        
        for element in btn_elements:
            content_desc = element.get_attribute("contentDescription")
            if content_desc == "휴대폰 본인 인증" : 
                next_btn = element
        next_btn.get_attribute("checked")

        if check_box_elements[0].get_attribute("checked") == "false":
            check_box_elements[0].click()
            if check_box_elements[1].get_attribute("checked") == "true" and check_box_elements[2].get_attribute("checked") == "true" and check_box_elements[3].get_attribute("checked") == "true":
                print("all check btn check")
                  
    def test_detail_ui_check(self):
        element_list = []
        view_elements = self.get_all_elements("android.view.View")
        
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
        
        if essential_service_detail is not None and essential_user_detail is not None and select_service_detail is not None:
            essential_service_detail.click()
            service_detail_page = self.get_all_elements("android.view.View")
            service_btn_elements = self.get_all_elements("android.widget.Button")
            service_detail_back_btn = self.get_detail_back_btn(service_btn_elements)
            for element in service_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "서비스 이용 약관":
                    print("essential service detail view check")
                    service_detail_back_btn.click()
                    break
                
            essential_user_detail.click()
            user_detail_page = self.get_all_elements("android.view.View")
            user_btn_elements = self.get_all_elements("android.widget.Button")
            user_detail_back_btn = self.get_detail_back_btn(user_btn_elements)
            
            for element in user_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "개인정보 처리방침":
                    print("essential user detail view check")
                    user_detail_back_btn.click()
                    break
        
            select_service_detail.click()
            select_service_detail_page = self.get_all_elements("android.view.View")
            select_btn_elements = self.get_all_elements("android.widget.Button")
            service_desc_list = []
            
            select_back_btn = self.get_detail_back_btn(select_btn_elements)
            for element in select_service_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc != '':
                    service_desc_list.append(content_desc)
            compare_arr = [
                '마케팅 수신 동의', 
                '마케팅 수신에 대한 동의(선택)', 
                '수집 · 이용 항목', 
                '수집 · 이용 목적', 
                '보유기간', 
                '이메일 주소', 
                'SMS', 
                '회원의 이메일 또는 SMS를 이용하여 \n이벤트 및 혜택 정보 안내', 
                '회원탈퇴 및 동의 철회 시 까지', 
                '본 동의를 거부하실 수 있습니다.\n다만 거부시 동의를 통해 제공 가능한 이벤트 및 혜택 정보 등의 안내를 받아 보실 수 없습니다.'
            ]
            if any(element in compare_arr for element in service_desc_list):
                print("select detail ui check")
            else:
                print("------ test check")
            select_back_btn.click()
                
    def get_detail_back_btn(self, btn_list):
        for element in btn_list:
            content_desc = element.get_attribute("contentDescription")
            if content_desc == "Back":
                detail_back_btn = element
                return detail_back_btn
                
    
        
    