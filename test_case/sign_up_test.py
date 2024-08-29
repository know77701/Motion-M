from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from PIL import Image
import cv2
import numpy as np


class SignUp:
    TITLE_CONTENT = [
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
    MOBILE_AUTH_TEXTS = [
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

    
    def __init__(self, driver):
        self.driver = driver
        self.btn_screenshot = "button_screenshot.png"
        self.enabled_btn = "./compare_image/button_screenshot_enabled.png"
        self.active_btn = "./compare_image/button_screenshot_active.png"
        self.mobile_auth_enabled_btn = "./compare_image/mobile_number_auth_enabled_btn.png"
        self.mobile_auth_active_btn = "./compare_image/mobile_number_auth_enabled_btn.png"
        self.content_description = "contentDescription"
        
        # self.sign_up_btn = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("회원가입 ")')))
        # self.sign_up_btn.click()
    
    def test_run(self):
        # self.test_detail_ui_check()
        self.test_checkbox_control()
        # self.test_mobile_auth()
        return
    
    def get_all_elements(self, class_name):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("{class_name}")')))
    
    def get_element_by_content_desc(self, elements, content_desc):
        for element in elements:
            if element.get_attribute("contentDescription") == content_desc:
                return element
        return None
    
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
            content_desc = element.get_attribute(self.content_description)
            if content_desc != '':
                element_list.append(content_desc)
            if i == 8 :
                essential_service_detail = element
            if i == 10 :
                essential_user_detail = element
            if i == 12 :
                select_service_detail = element


        if any(element in self.TITLE_CONTENT for element in element_list):
            print("check ui title")
        
        if essential_service_detail is not None and essential_user_detail is not None and select_service_detail is not None:
            essential_service_detail.click()
            service_detail_page = self.get_all_elements("android.view.View")
            service_btn_elements = self.get_all_elements("android.widget.Button")
            service_detail_back_btn = self.get_element_by_content_desc(service_btn_elements, "Back")
            for element in service_detail_page:
                content_desc = element.get_attribute(self.content_description)
                if content_desc == "서비스 이용 약관":
                    print("essential service detail view check")
                    service_detail_back_btn.click()
                    break
                
            essential_user_detail.click()
            user_detail_page = self.get_all_elements("android.view.View")
            user_btn_elements = self.get_all_elements("android.widget.Button")
            user_detail_back_btn = self.get_element_by_content_desc(user_btn_elements, "Back")
            
            for element in user_detail_page:
                content_desc = element.get_attribute(self.content_description)
                if content_desc == "개인정보 처리방침":
                    print("essential user detail view check")
                    user_detail_back_btn.click()
                    break
        
            select_service_detail.click()
            select_service_detail_page = self.get_all_elements("android.view.View")
            select_btn_elements = self.get_all_elements("android.widget.Button")
            service_desc_list = []
            
            select_back_btn = self.get_element_by_content_desc(select_btn_elements, "Back")
            for element in select_service_detail_page:
                content_desc = element.get_attribute(self.content_description)
                if content_desc != '':
                    service_desc_list.append(content_desc)

            if any(element in self.MOBILE_AUTH_TEXTS for element in service_desc_list):
                print("select detail ui check")
            else:
                print("------ test check")
            select_back_btn.click()
            
    def test_checkbox_control(self):
        # self.test_all_check_checkbox()
        self.test_select_checkbox()
        btn_elements = self.get_all_elements("android.widget.Button")
        btn_elements[1].click()
        
        
    def test_select_checkbox(self):
        check_box_elements = self.get_all_elements("android.widget.CheckBox")
        btn_elements = self.get_all_elements("android.widget.Button")
        
        index_sets = [[3],[1],[2],[3, 1],[3, 2],[1, 2]]
        
        for i, indices in enumerate(index_sets, start=1):   
            for index in indices:
                check_box_elements[index].click()
            
            current_check_states = [checkbox.get_attribute("checked") for checkbox in check_box_elements]
            if i <= 3:
                self.toggle_checkbox_and_verify(check_box_elements[indices[-1]], btn_elements[1], self.enabled_btn)
                for index in indices:
                    check_box_elements[index].click()
            elif i >= 3 and current_check_states == ['false','true','true','false'] or current_check_states == ['true','true', 'true','true']:
                self.toggle_checkbox_and_verify(check_box_elements[indices[1]], btn_elements[1], self.active_btn)
                for index in indices:
                    check_box_elements[index].click()
            elif i >= 3:
                self.toggle_checkbox_and_verify(check_box_elements[indices[-1]], btn_elements[1], self.enabled_btn)
                for index in indices:
                    check_box_elements[index].click()
            else:
                print("FAIL: Not enableed btn")

    def toggle_checkbox_and_verify(self, checkbox, button, expected_image):
        result = self.compare_image(button, expected_image)
        assert result, f"Button state after clicking checkbox {checkbox.get_attribute('contentDescription')} is incorrect."

    def test_all_check_checkbox(self):
        check_box_elements = self.get_all_elements("android.widget.CheckBox")
        btn_elements = self.get_all_elements("android.widget.Button")

        self.toggle_all_checkboxes_and_verify(check_box_elements[0], check_box_elements[1:], btn_elements)

    def toggle_all_checkboxes_and_verify(self, all_checkbox, individual_checkboxes, btn_elements):
        all_checkbox.click()
        for checkbox in individual_checkboxes:
            assert checkbox.get_attribute("checked") == "true", f"{checkbox.get_attribute('contentDescription')} is not checked."
        
        result = self.compare_image(self.get_element_by_content_desc(btn_elements, "휴대폰 번호 인증"), self.active_btn)
        assert result, "Next button is not active after selecting all checkboxes."

        all_checkbox.click()
        for checkbox in individual_checkboxes:
            assert checkbox.get_attribute("checked") == "false", f"{checkbox.get_attribute('contentDescription')} is still checked."

    def test_mobile_auth(self):
        self.test_mobile_auth_ui_check()
        self.test_edit_description_check()
        
    def test_mobile_auth_ui_check(self):
        view_list = self.get_all_elements("android.view.View")
        btn_list = self.get_all_elements("android.widget.Button")

        element_desc_arr = [el.get_attribute("contentDescription") for el in view_list if el.get_attribute("contentDescription")]


        assert all(element in element_desc_arr for element in SignUp.MOBILE_AUTH_TEXTS), "Mobile auth UI check failed."

        compare_result = self.compare_image(btn_list[2], self.mobile_auth_enabled_btn)
        assert compare_result, "Mobile auth button UI check failed."
    
    def test_edit_description_check(self):
        edit_list = self.get_all_elements("android.widget.EditText")
        edit_list[0].click()
        edit_list[1].click()
        
        view_list = self.get_all_elements("android.view.View")
        
        for el in view_list:
            print(el)