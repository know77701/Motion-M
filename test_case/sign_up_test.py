from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from PIL import Image
import cv2
import numpy as np


class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.btn_screenshot = "button_screenshot.png"
        self.enabled_btn = "./compare_image/button_screenshot_enabled.png"
        self.active_btn = "./compare_image/button_screenshot_abled.png"
        self.mobile_auth_enabled_btn = "./compare_image/mobile_number_auth_enabled_btn.png"
        self.mobile_auth_active_btn = "./compare_image/mobile_number_auth_enabled_btn.png"
        
        # self.sign_up_btn = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("회원가입 ")')))
        # self.sign_up_btn.click()
    
    def test_run(self):
        # self.test_detail_ui_check()
        # self.test_checkbox_control()
        self.mobile_auto_ui_check()
        return
    
    def get_all_elements(self, class_name):
        elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("{class_name}")')))
        return elements
    
    def get_detail_back_btn(self, btn_list):
        for element in btn_list:
            content_desc = element.get_attribute("contentDescription")
            if content_desc == "Back":
                detail_back_btn = element
                return detail_back_btn
    
    def compare_image(self, element, comapre_image):
        element_screenshot = element.screenshot_as_png
        with open(self.btn_screenshot, "wb") as file:
            file.write(element_screenshot)
        
        img1 = cv2.imread(comapre_image)
        img2 = cv2.imread(self.btn_screenshot)

        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
        difference = cv2.absdiff(img1_gray, img2_gray)
        result = not np.any(difference)
        
        return result    
        
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
            "회원가입",
            "모션 M 이용약관" ,
            "전체 동의",
            "[필수] 서비스 이용 약관",
            "[필수] 개인정보 수집 및 이용 동의",
            "[선택] 마케팅 수신 동의",
            "휴대폰 인증",
            "본인 명의의 휴대폰 번호로 인증합니다.",
            "타인 명의 휴대폰, 법인폰을 이용자는 본인인증이 불가합니다."
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
            
    def test_checkbox_control(self):
        test_select_checkbox()
        test_all_check_checkbox()
        btn_elements = self.get_all_elements("android.widget.Button")
        btn_elements[1].click()
        
        
        def test_select_checkbox(self):
            check_box_elements = self.get_all_elements("android.widget.CheckBox")
            btn_elements = self.get_all_elements("android.widget.Button")

            check_box_elements[3].click()
            result = self.compare_image(btn_elements[1], self.enabled_btn)
            if result:
                print("next button enable")
                check_box_elements[3].click()
            else:
                print("FAIL")
            
            check_box_elements[1].click()
            result = self.compare_image(btn_elements[1], self.enabled_btn)
            if result:
                print("next button enable")
            else:
                print("FAIL")
            
            check_box_elements[2].click()
            result = self.compare_image(btn_elements[1], self.active_btn)
            if result:
                print("next button active")
        
        def test_all_check_checkbox(self):
            check_box_elements = self.get_all_elements("android.widget.CheckBox")
            btn_elements = self.get_all_elements("android.widget.Button")

            for element in btn_elements:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "휴대폰 번호 인증":
                    next_btn = element
                    break
            
            if check_box_elements[0].get_attribute("checked") == "false":
                check_box_elements[0].click()
                if check_box_elements[1].get_attribute("checked") == "true" and check_box_elements[2].get_attribute("checked") == "true" and check_box_elements[3].get_attribute("checked") == "true":
                    print("all check btn check")
                else:
                    print("FAIL")
                    
            result = self.compare_image(next_btn, self.active_btn)
            
            if result:
                print("enabled btn check")
            else: 
                print("Fail")
            if check_box_elements[0].get_attribute("checked") == "true":
                check_box_elements[0].click()
                if check_box_elements[1].get_attribute("checked") == "false" and check_box_elements[2].get_attribute("checked") == "false" and check_box_elements[3].get_attribute("checked") == "false":
                    print("all check btn check")
                else:
                    print("all check btn fail")
                    
            result = self.compare_image(next_btn, self.enabled_btn)
            
            if result:
                print("active btn check")
            else:
                print("FAIL")

    def mobile_auto_ui_check(self):
        view_list = self.get_all_elements("android.view.View")
        btn_list = self.get_all_elements("android.widget.Button")
        edit_list = self.get_all_elements("android.widget.EditText")
        compare_arr = ['회원가입', '휴대폰 인증', '본인 확인을 위해 휴대폰 번호 인증이 필요합니다.', '이름*', '휴대폰번호*']
        element_desc_arr = []
        
        for el in view_list:
            el_desc = el.get_attribute("contentDescription")
            if el_desc != "" and el_desc != ' ':
                element_desc_arr.append(el_desc)
        
        if any(element in element_desc_arr for element in compare_arr):
            print("mobile_auto_ui_check PASS")
        else:
            print("FAIL")
            
        for el in btn_list:
            print(el.get_attribute("contentDescription"))
        
        compare_result = self.compare_image(btn_list[2], self.mobile_auth_enabled_btn)
        
        if compare_result:
            print("Button ui check PASS")
        else:
            print("FAIL")
        