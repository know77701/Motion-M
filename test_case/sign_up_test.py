from utils.utils import Utils
from config.selectors import Selectors

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
    SELECT_CONTENT = [
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
    MOBILE_AUTH_TEXTS = [
        '회원가입', '휴대폰 인증', '본인 확인을 위해 휴대폰 번호 인증이 필요합니다.', '이름*', '휴대폰번호*'
    ]

    
    def __init__(self, driver):
        self.driver = driver
        self.btn_screenshot = "button_screenshot.png"
        self.enabled_btn = "./compare_image/`button`_screenshot_enabled.png"
        self.active_btn = "./compare_image/button_screenshot_active.png"
        self.mobile_auth_enabled_btn = "./compare_image/mobile_number_auth_enabled_btn.png"
        self.mobile_auth_active_btn = "./compare_image/mobile_number_auth_active_btn.png"
        self.already_registered_number = '01074417631'
        self.utils = Utils(driver)
        self.selectors = Selectors()
        # self.sign_up_btn = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("회원가입 ")')))
        # self.sign_up_btn.click()
    
    def test_run(self):
        # self.test_detail_ui_check()
        # self.test_checkbox_control()
        # self.test_mobile_auth()
        self.test_user_infomation_page()
 
    def test_checkbox_control(self):
        self.test_select_checkbox()
        self.test_all_check_checkbox()
        btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_elements[1].click()
 
    def test_mobile_auth(self):
        self.test_mobile_auth_ui_check()
        self.test_edit_description_check()
        self.test_signup_with_registered_phone_number()
        self.test_auth_description_check()
        self.test_sucess_authcation()
        self.test_validate_job_ui_check()
    
    
    def test_detail_ui_check(self):
        element_list = []
        view_elements = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
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


        if any(element in self.TITLE_CONTENT for element in element_list):
            print("check ui title")
        
        if essential_service_detail is not None and essential_user_detail is not None and select_service_detail is not None:
            essential_service_detail.click()
            service_detail_page = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            service_btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
            service_detail_back_btn = self.get_element_by_content_desc(service_btn_elements, "Back")
            for element in service_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "서비스 이용 약관":
                    print("essential service detail view check")
                    service_detail_back_btn.click()
                    break
                
            essential_user_detail.click()
            user_detail_page = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            user_btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
            user_detail_back_btn = self.get_element_by_content_desc(user_btn_elements, "Back")
            
            for element in user_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc == "개인정보 처리방침":
                    print("essential user detail view check")
                    user_detail_back_btn.click()
                    break
        
            select_service_detail.click()
            select_service_detail_page = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            select_btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
            service_desc_list = []
            
            select_back_btn = self.get_element_by_content_desc(select_btn_elements, "Back")
            for element in select_service_detail_page:
                content_desc = element.get_attribute("contentDescription")
                if content_desc != '':
                    service_desc_list.append(content_desc)

            if any(element in self.SELECT_CONTENT for element in service_desc_list):
                print("select detail ui check")
            else:
                print("------ test check")
            select_back_btn.click()
            
        
        
    def test_select_checkbox(self):
        check_box_elements = self.get_all_elements("")
        btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        index_sets = [[3],[1],[2],[3, 1],[3, 2],[1, 2]]
        
        for i, indices in enumerate(index_sets, start=1):   
            for index in indices:
                check_box_elements[index].click()
            
            current_check_states = [checkbox.get_attribute("checked") for checkbox in check_box_elements]
            if i <= 3:
                self.compare_and_assert(btn_elements[1], self.enabled_btn, "not authaction button ui Fail")
                for index in indices:
                    check_box_elements[index].click()
            elif i >= 3 and current_check_states == ['false','true','true','false'] or current_check_states == ['true','true', 'true','true']:
                self.compare_and_assert(btn_elements[1], self.active_btn, "not authaction button ui Fail")
                for index in indices:
                    check_box_elements[index].click()
            elif i >= 3:
                self.compare_and_assert(btn_elements[1], self.enabled_btn, "not authaction button ui Fail")
                for index in indices:
                    check_box_elements[index].click()


    def test_all_check_checkbox(self):
        check_box_elements = self.get_all_elements(self.selectors.CHECKBOX_CLASS_NAME)
        btn_elements = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)

        self.toggle_all_checkboxes_and_verify(check_box_elements[0], check_box_elements[1:], btn_elements)
        btn_elements[1].click()

    def toggle_all_checkboxes_and_verify(self, all_checkbox, individual_checkboxes, btn_elements):
        all_checkbox.click()
        for checkbox in individual_checkboxes:
            assert checkbox.get_attribute("checked") == "true", f"{checkbox.get_attribute('contentDescription')} is not checked."
        
        result = self.compare_image(self.get_element_by_content_desc(btn_elements, "휴대폰 번호 인증"), self.active_btn)
        assert result, "Next button is not active after selecting all checkboxes."

        all_checkbox.click()
        for checkbox in individual_checkboxes:
            assert checkbox.get_attribute("checked") == "false", f"{checkbox.get_attribute('contentDescription')} is still checked."
        all_checkbox.click()


        
    def test_mobile_auth_ui_check(self):
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        element_desc_arr = ([el.get_attribute("contentDescription") for el in view_list if el.get_attribute("contentDescription") and 
                            el.get_attribute("contentDescription") != ' '])

        assert all(element in element_desc_arr for element in self.MOBILE_AUTH_TEXTS), "Mobile auth UI check failed."

        compare_result = self.compare_image(btn_list[2], self.mobile_auth_enabled_btn)
        assert compare_result, "Mobile auth button UI check failed."
    
    def test_edit_description_check(self):
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        btn_list[1].click()
        
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        compare_list = ['이름을 입력해주세요', '휴대폰 번호를 입력하세요.']
        element_desc_arr = ([el.get_attribute("contentDescription") for el in view_list if el.get_attribute("contentDescription") and 
                             el.get_attribute("contentDescription") != ' ' and 
                             el.get_attribute("contentDescription") == "이름을 입력해주세요" 
                             or el.get_attribute("contentDescription") == "휴대폰 번호를 입력하세요."])
        
        assert all(element in element_desc_arr for element in compare_list),"Edit description check failed"
        
    def edit_send_data(self, user_name, mobile_number):
        edit_list = self.get_all_elements("")
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        for i,elements in enumerate(edit_list):
            elements.click()
            if i == 0: 
                elements.send_keys(user_name)
            else:
                elements.send_keys(mobile_number)
                break
            
        btn_list[1].click()
        popup_element = self.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        return popup_element
    
    def test_signup_with_registered_phone_number(self):
        popup_element = self.edit_send_data("테스트",self.already_registered_number)
        
        for element in popup_element:
            assert "이미 등록된 핸드폰번호 입니다." in element.get_attribute("contentDescription"), "Popup message is not as expected."
        
        popup_btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        popup_btn_list[0].click()
        
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        assert btn_list[1].get_attribute("contentDescription")=="인증요청", "auth button description Fail"
            
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        compare_result = self.compare_image(btn_list[2], self.mobile_auth_enabled_btn)
        assert compare_result, "Non authcation test Fail"
    
    def test_auth_description_check(self):
        self.edit_send_data("테스트", "01000009412")

        popup_btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        popup_btn_list[0].click()
        
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        edit_list = self.get_all_elements(self.selectors.EDIT_CLASS_NAME)
        
        btn_list[2].click()
        
        assert btn_list[1].get_attribute("contentDescription") == "재전송", "auth button description Fail"        
        assert edit_list[2], None

        edit_list[2].click()
        edit_list[2].send_keys("")
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert "인증번호를 입력하세요" in view_list[12].get_attribute("contentDescription"), "auth number input description Fail"
        
        
        edit_list[2].click()
        edit_list[2].send_keys("000000")
        btn_list[2].click()
        
        assert "인증번호가 일치하지 않습니다." in view_list[12].get_attribute("contentDescription"), "auth number input description Fail"
    
    def test_sucess_authcation(self):
        self.edit_send_data("테스트", "01000009412")
        popup_btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        popup_btn_list[0].click()
        
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        edit_list = self.get_all_elements(self.selectors.EDIT_CLASS_NAME)
        
        auth_number = input("auth number : ")
        edit_list[2].click()
        edit_list[2].send_keys("")
        edit_list[2].send_keys(auth_number)
        btn_list[2].click()

    # def description_clean(self, content):
    #     return content.replace("\n", "").replace(" ", "")

    def test_validate_job_ui_check(self):
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        assert view_list[4].get_attribute("contentDescription") == "회원가입", "test_validate_job_ui_check job validate ui Fail"
        self.compare_and_assert(view_list[5],"./compare_image/validate_doctor.png", "test_validate_job_ui_check doctor element ui Fail")
        self.compare_and_assert(view_list[6],"./compare_image/validate_employee.png", "test_validate_job_ui_check employee element ui Fail")
        
        check_box_elements = self.get_all_elements(self.selectors.CHECKBOX_CLASS_NAME)
        
        self.click_and_verify(check_box_elements[0], view_list[5], "./compare_image/validate_doctor_active.png", "test_validate_job_ui_check doctor active element ui Fail")
        self.click_and_verify(check_box_elements[1], view_list[6], "./compare_image/validate_employee_active.png", "test_validate_job_ui_check employee active element ui Fail")
        
        view_list[5].click()
        btn_list[1].click()
        
    def compare_and_assert(self, element, image_path, error_message):
        element_compare = self.compare_image(element, image_path)
        assert element_compare, error_message
        
    def click_and_verify(self, check_box, element, image_path, error_message):
        check_box.click()
        self.compare_and_assert(element, image_path, error_message)
        check_box.click()


    def test_user_infomation_page(self):
        # self.test_user_infomation_ui_check()
        self.test_description_check()

    def get_element_descriptions(self, list):
        descriptions = []
        for element in list:
            description = element.get_attribute("contentDescription")
            if description.strip():
                descriptions.append(description)
        return descriptions



    def test_user_information_ui_check(self):
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_arr = self.get_element_descriptions(view_list)

        self.scroll_action(self.selectors.BUTTON_CLASS_NAME, "회원가입")

        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        desc_list = self.get_element_descriptions(view_list)

        view_arr = list(set(view_arr + desc_list))

        view_compare_arr = [
            '비밀 번호*', 
            '사용자 ID*', 
            '회원가입',
            '성별*', 
            '* 권장 확장자 : PNG (투명 배경 이미지)',
            '* 권장 사이즈 및 용량 : 375 X 375,  1MB이하', 
            '외국인 여부*', 
            '생년월일*',
            '비밀 번호 확인*', 
            '프로필 이미지*', 
            '서명 이미지', 
            '의사면허번호', 
            '* 권장 사이즈 및 용량 : 74 X 74,  1MB이하', 
            '이메일 주소'
        ]

        assert view_arr == view_compare_arr, "test_user_information_ui_check ui text check Fail"
        
    def test_description_check(self):
        view_list = self.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        

        self.scroll_action(self.selectors.BUTTON_CLASS_NAME, "회원가입")
        btn_list = self.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[5].click()
        
        self.scroll_action(self.selectors.BUTTON_CLASS_NAME, "중복확인")
        
        for i,element in enumerate(view_list):
            desc = element.get_attribute("contentDescription")
            print(i)
            print(desc)
    
    def test_popup_descripition_check(self):
        return