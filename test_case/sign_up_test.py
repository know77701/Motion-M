from utils.utils import Utils
from config.selectors import Selectors
from selenium.webdriver.common.by import By


class SignUp:
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
        # self.test_basic_sing_up_description_check()
        self.test_hospital_info_sing_up_description_check()
 
    def element_size_check(self, element):
        element_size = element.size 
        width = element_size['width']
        height = element_size['height']
        return  print(f"Element 크기: 가로 {width}px, 세로 {height}px")
 
    def test_basic_sing_up_description_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        found_signup_info = False
        id_desc = None
        pw_desc = None
        pw_confirm_desc = None
        phone_number_desc = None
        birth_date_desc = None
        email_desc = None
        gender_desc = None
        foreigner_desc = None
        
        for items in view_list:
            element_text = items.get_attribute("text")
            if element_text == "가입 기본 정보" and not found_signup_info:
                child_element = items.find_elements(By.XPATH,".//*")
                for child in child_element:
                    child_text = child.get_attribute("text")
                    if child_text == "아이디":
                        id_desc = child_text
                    elif child_text == "비밀번호":
                        pw_desc = child_text
                    elif child_text == "비밀번호 확인":
                        pw_confirm_desc = child_text
                    elif child_text == "휴대폰 번호":
                        phone_number_desc = child_text
                    elif child_text == "생년월일":
                        birth_date_desc = child_text
                    elif child_text == "이메일 주소":
                        email_desc = child_text
                    elif child_text == "성별":
                        gender_desc = child_text
                    elif child_text == "외국인 여부":
                        foreigner_desc = child_text
        assert id_desc == "아이디", "아이디 텍스트 확인 테스트 Fail"
        assert pw_desc == "비밀번호", "비밀번호 텍스트 확인 테스트 Fail"
        assert pw_confirm_desc == "비밀번호 확인", "비밀번호 확인 텍스트 확인 테스트 Fail"
        assert phone_number_desc == "휴대폰 번호", "휴대폰 번호 텍스트 확인 테스트 Fail"
        assert birth_date_desc == "생년월일", "생년월일 텍스트 확인 테스트 Fail"
        assert email_desc == "이메일 주소", "이메일 주소 텍스트 확인 테스트 Fail"
        assert gender_desc == "성별", "성별 텍스트 확인 테스트 Fail"
        assert foreigner_desc == "외국인 여부", "외국인 여부 텍스트 확인 테스트 Fail"
        
    def test_hospital_info_sing_up_description_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        found_hospital_info = False
        
        hospital_name = None
        director_name = None
        institution_number = None
        doctor_license_number = None
        establishment_license = None
        manager_phone_number = None
        manager_email = None
        foreign_status = None

        for items in view_list:
            element_text = items.get_attribute("text")
            if element_text == "병원 기본 정보" and not found_hospital_info:
                found_hospital_info = True
                child_elements = items.find_elements(By.XPATH, ".//*")
                for child in child_elements:
                    child_text = child.get_attribute("text")
                    if child_text == "병원명":
                        hospital_name = child_text
                    elif child_text == "대표원장명":
                        director_name = child_text
                    elif child_text == "요양 기관 번호":
                        institution_number = child_text
                    elif child_text == "의사 면허 번호":
                        doctor_license_number = child_text
                    elif child_text == "의료기관 개설허가증":
                        establishment_license = child_text
                    elif child_text == "담당자 휴대폰 번호":
                        manager_phone_number = child_text
                    elif child_text == "담당자 이메일 주소":
                        manager_email = child_text
                    elif child_text == "외국인 여부":
                        foreign_status = child_text

        assert hospital_name == "병원명", "병원명 텍스트 확인 실패"
        assert director_name == "대표원장명", "대표원장명 텍스트 확인 실패"
        assert institution_number == "요양 기관 번호", "요양 기관 번호 텍스트 확인 실패"
        assert doctor_license_number == "의사 면허 번호", "의사 면허 번호 텍스트 확인 실패"
        assert establishment_license == "의료기관 개설허가증", "의료기관 개설허가증 텍스트 확인 실패"
        assert manager_phone_number == "담당자 휴대폰 번호", "담당자 휴대폰 번호 텍스트 확인 실패"
        assert manager_email == "담당자 이메일 주소", "담당자 이메일 주소 텍스트 확인 실패"
        assert foreign_status == "외국인 여부", "외국인 여부 텍스트 확인 실패"