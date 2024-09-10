from utils.utils import Utils
from config.selectors import Selectors

class Home():
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
    
    def test_run(self):
        self.test_home_page_ui_check()
        self.test_profile_image_check()
        self.test_bottom_sheet_action()
    
    def test_home_page_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        user_name_replace = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        assert view_list[5].get_attribute("contentDescription") == "트라이업영문", "home page business name ui test Fail"
        assert user_name_replace == "이말년의사/대표원장", "home page user name ui test Fail"
        assert self.utils.compare_image("user_image.png",view_list[8],"home_user_image.png","home"), "home user image compare test Fail"
        assert self.utils.compare_image("setting_button.png",image_list[0],"home_setting_button.png","home"), "home setting btn ui test Fail"
        assert self.utils.compare_image("status_setting.png",image_list[1],"home_status_setting.png","home"), "home status setting btn ui test Fail"
        assert self.utils.compare_image("alert_setting.png",image_list[2],"home_alert_setting.png","home"), "home alert setting btn ui test Fail"
        assert self.utils.compare_image("user_message_chatting_room.png",btn_list[0],"user_message_chatting_room.png","home"), "meessage chatting room button ui test Fail"
        assert self.utils.compare_image("home_tap.png",image_list[3],"bottom_home_tap.png","home"),"bottom home tap active ui test Fail"
        assert self.utils.compare_image("message_tap.png",image_list[4],"bottom_message_tap.png","home"), "bottom messsage tap enabled ui test Fail"
        assert self.utils.compare_image("organization_chart_enabled.png",image_list[5],"bottom_organization_chart_enabled.png","home"), "bottom organization chart tap enabled ui test Fail"
        
    def test_profile_image_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[8].click()
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        assert self.utils.compare_image("view_user_image.png",image_list[0],"view_user_image.png","home"), "bottom organization chart tap enabled ui test Fail"
        btn_list[0].click()
    
    def test_user_status_bottom_sheet_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[1].click()
        self.utils.get_element_list_print(self.selectors.VIEW_CLASS_NAME)
        self.utils.screenshot_image("status_bottom_sheet2.png", view_list[2])
        self.utils.screenshot_image("status_bottom_sheet3.png", view_list[3])
        self.utils.screenshot_image("status_bottom_sheet4.png", view_list[4])
        self.utils.screenshot_image("status_bottom_sheet5.png", view_list[5])
        # assert self.utils.compare_image("")
    
    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "logout popup description test Fail"
        btn_list[1].click()
        
        
        
        
