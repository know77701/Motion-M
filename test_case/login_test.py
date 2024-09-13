from test_case.home_test import Home
from config.selectors import Selectors
from utils.utils import Utils
import time


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.utils= Utils(driver)
        self.home = Home(driver)
        self.selector = Selectors()
        self.lock_id = self.utils.get_data_json("lock_id")
        self.sucess_id = self.utils.get_data_json("sucess_id")
        self.sucess_pw = self.utils.get_data_json("sucess_password")
        self.withdrawal_id = self.utils.get_data_json("withdrawal_id")
        self.withdrawal_password = self.utils.get_data_json("sucess_password")

    def test_run(self):
        # self.test_login_page_ui_check()
        # self.test_edit_validation()
        # self.test_edit_description_check()
        # self.test_non_register_user_login()
        # self.test_different_password()
        self.test_user_lock_account()
        # self.test_lock_user()
        # self.test_withdrawal_user()
        # self.test_password_hidden()
        # self.test_save_user_id()
        # self.test_automatic_login()
        # self.test_login_sucess()
    
    def edit_data_input(self, id,pw):
        image_list = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        edit_list = self.utils.get_all_elements(self.selector.EDIT_CLASS_NAME)
        edit_list[0].click()
        edit_list[0].send_keys("")
        edit_list[0].send_keys(id)
        edit_list[1].click()
        edit_list[1].send_keys("")
        edit_list[1].send_keys(pw)
        image_list[0].click()
    
    def test_login_page_ui_check(self):
        text_list = []
        test_compare_list = ['로그인', '아이디 저장', '자동 로그인', '회원가입 ']
        btn_index = None
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        edit_list = self.utils.get_all_elements(self.selector.EDIT_CLASS_NAME)
        logo_compare_result = self.utils.compare_image("logo.png",image_list[0],"login_logo.png","login")
        
        id_edit_compare_result = self.utils.compare_image("id_edit.png",edit_list[0],"login_id_edit.png","login")
        password_edit_compare_result = self.utils.compare_image("pw_edit.png",edit_list[1],"login_password_edit.png","login")

        for i,element in enumerate(view_list):
            element_desc = element.get_attribute("contentDescription")
            if element_desc != '' and element_desc != ' ':
                text_list.append(element_desc)
            if element_desc == "로그인":
                btn_index = i
        login_btn_compare_result = self.utils.compare_image("btn.png", view_list[btn_index],"login_btn.png","login")
        
        assert logo_compare_result, "login logo image ui test Fail"
        assert id_edit_compare_result, "login id edit ui test Fail"
        assert password_edit_compare_result, "login password edit ui test Fail"
        assert login_btn_compare_result, "login button ui test Fail"
        assert text_list == test_compare_list, "login text ui test Fail"

    def test_edit_validation(self):
        validation_id = "`가나다~#!@`"
        validation_pw = "가나다"
        max_value = "11111111111111111111111"
        self.edit_data_input(validation_id, validation_pw)
        
        edit_list = self.utils.get_all_elements(self.selector.EDIT_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        
        id_edit_value = edit_list[0].get_attribute("text")
        pw_edit_value = edit_list[1].get_attribute("text")
        if "••" in pw_edit_value:
            btn_list[0].click()
        
        assert id_edit_value != validation_id, "id edit validation test Fail" 
        assert pw_edit_value != validation_pw, "password edit vaildation test Fail"
        
        self.edit_data_input(max_value, max_value)
        
        assert id_edit_value != max_value, "id edit max value validation test Fail" 
        assert pw_edit_value != max_value, "password edit max value vaildation test Fail"

    def test_edit_description_check(self):
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list, "로그인")
        
        self.edit_data_input("test","")
        login_btn.click()
        assert "비밀번호를 입력해주세요" in view_list[5].get_attribute("contentDescription"),"login password description test Fail"
        
        self.edit_data_input("","test")
        assert "로그인 아이디를 입력해 주세요." in view_list[4].get_attribute("contentDescription") ,"login id description test Fail"
       
        self.edit_data_input("","")
        
        assert (
            "로그인 아이디를 입력해 주세요." in view_list[4].get_attribute("contentDescription") and
            "비밀번호를 입력해주세요" in view_list[6].get_attribute("contentDescription")
            ), "login id and password description test fail"

    def test_non_register_user_login(self):
        self.edit_data_input("error","error")
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list,"로그인")
        login_btn.click()
        popup_desc = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        popup_btn = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        assert popup_desc[0].get_attribute("contentDescription") == "가입된 회원이 아닙니다.", "non register user login popup description test Fail"
        popup_btn[0].click()
        
    def test_different_password(self):
        self.edit_data_input(self.sucess_id, "test")
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list, "로그인")
        login_btn.click()
        
        popup_desc = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        popup_close_btn = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        
        assert "비밀번호" in popup_desc[0].get_attribute("contentDescription"), "different password popup description test Fail"
        popup_close_btn[0].click()
        assert "아이디와 비밀번호를 확인해 주세요." in view_list[4].get_attribute("contentDescription"), "different password edit description test Fail"

    def test_user_lock_account(self):        
        self.edit_data_input(self.lock_id, "error")
        
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        self.utils.get_element_list_print(self.selector.VIEW_CLASS_NAME)
        popup_close_btn = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list, "로그인")
        login_btn.click()
        
        popup_desc = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        replace_desc = self.utils.element_replace(popup_desc[0].get_attribute("contentDescription"))
        compare_desc = "로그인실패횟수5회가되어로그인이불가합니다."
                    
        assert compare_desc in replace_desc, "lock user login test Fail"
        popup_close_btn[0].click()

    def test_withdrawal_user(self):
        self.edit_data_input(self.withdrawal_id, self.withdrawal_password)
        
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list, "로그인")
        login_btn.click()
        
        popup_desc = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        popup_close_btn = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        compare_desc = "탈퇴처리가 되어 로그인이 불가합니다."
        
        assert compare_desc in popup_desc[0].get_attribute("contentDescription"), "withdrawal user login test Fail"
        popup_close_btn[0].click()
    

    def test_password_hidden(self):
        self.edit_data_input(self.sucess_id, self.sucess_pw)
        
        btn_list = self.utils.get_all_elements(self.selector.BUTTON_CLASS_NAME)
        edit_list = self.utils.get_all_elements(self.selector.EDIT_CLASS_NAME)
        
        edit_value = edit_list[1].get_attribute("text")
        
        if not "••" in edit_value:
            btn_list[0].click()
        time.sleep(1)
        
        hidden_btn_compare = self.utils.compare_image("hidden_btn.png", btn_list[0], "hidden_btn.png","login")
        assert hidden_btn_compare, "password hidden btn ui test Fail"

        if "••" in edit_value:
            btn_list[0].click()
        time.sleep(1)
        
        hidden_active_compare = self.utils.compare_image("hidden_btn_active.png", btn_list[0], "hidden_btn_active.png","login")
        assert hidden_active_compare, "password hidden btn active ui test Fail"
        btn_list[0].click()
          
    def test_login_sucess(self):
        self.edit_data_input(self.sucess_id, self.sucess_pw)
        
        view_list = self.utils.get_all_elements(self.selector.VIEW_CLASS_NAME)
        login_btn = self.utils.get_element_by_content_desc(view_list, "로그인")
        login_btn.click()

    def test_save_user_id(self):
        checkbox_list = self.utils.get_all_elements(self.selector.CHECKBOX_CLASS_NAME)
        
        if checkbox_list[0].is_enabled():
            checkbox_list[0].click()
        self.test_login_sucess()
        self.home.test_logout()
        
        edit_list = self.utils.get_all_elements(self.selector.EDIT_CLASS_NAME)
        save_edit_value = edit_list[0].get_attribute("text")
        if save_edit_value == self.sucess_id:
            if checkbox_list[0].is_enabled():
                checkbox_list[0].click()
                self.test_login_sucess()
                self.home.test_logout()
                non_save_edit_value = edit_list[0].get_attribute("text")
                if non_save_edit_value == self.sucess_id:
                    assert edit_list == self.sucess_id, "user id non save test Fail"
        else:
            assert edit_list == self.sucess_id, "user id save test Fail"
            
    def test_automatic_login(self):
        checkbox_list = self.utils.get_all_elements(self.selector.CHECKBOX_CLASS_NAME)
        checkbox_status = self.utils.compare_image("automatic_checkbox_enabled.png", checkbox_list[1], "automatic_checkbox_enabled.png","login")
        if checkbox_status:
            checkbox_list[1].click()
        
        self.test_login_sucess()
        self.driver.terminate_app(self.selector.PACKAGE_NAME)
        self.driver.activate_app(self.selector.PACKAGE_NAME)
        time.sleep(2)
        
        image_list = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
        logo_compare_result = self.utils.compare_image("element_image.png",image_list[0],"login_logo.png","login")
        assert not logo_compare_result, "automation login test Fail"

        self.home.test_logout()
        time.sleep(2)

        checkbox_status = self.utils.compare_image("element_image.png", checkbox_list[1], "automatic_checkbox_active.png","login")
        if checkbox_status:
            checkbox_list[1].click()
            self.test_login_sucess()
            self.driver.terminate_app(self.selector.PACKAGE_NAME)
            self.driver.activate_app(self.selector.PACKAGE_NAME)
            time.sleep(1)
            
            checkbox_status = self.utils.compare_image("logo.png", checkbox_list[1], "automatic_checkbox_enabled.png","login")
            
            if checkbox_status:
                image_list = self.utils.get_all_elements(self.selector.IMAGE_CLASS_NAME)
                logo_compare_result = self.utils.compare_image("logo.png",image_list[0],"login_logo.png","login")
                assert logo_compare_result, "automation login test Fail"
                
            else:
                assert checkbox_status, "automatic login checkbox enabled value test Fail"
        else:
            assert checkbox_status, "automatic login checkbox active value test Fail"
        