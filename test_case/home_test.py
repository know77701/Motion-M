from utils.utils import Utils
from config.selectors import Selectors

class Home():
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
    
    def test_run(self):
        self.test_home_page_ui_check()
    
    def test_home_page_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        assert view_list[5].get_attribute("contentDescription") == "트라이업영문", "home page business name ui test Fail"
        assert view_list[7].get_attribute("contentDescription") == "이말년 의사/대표원장", "home page user name ui test Fail"
        assert self.utils.compare_image("user_image.png",view_list[8],"home_user_image.png"), "home user image compare test Fail"
        assert self.utils.compare_image("setting_button.png",image_list[0],"home_setting_button.png"), "home setting btn ui test Fail"
        assert self.utils.compare_image("status_setting.png",image_list[1],"home_status_setting.png"), "home status setting btn ui test Fail"
        assert self.utils.compare_image("alert_setting.png",image_list[2],"home_alert_setting.png"), "home alert setting btn ui test Fail"
        assert self.utils.compare_image("user_message_chatting_room.png",btn_list[2],"user_message_chatting_room.png"), ""
        assert self.utils.compare_image("home_tap.png",image_list[3],"bottom_home_tap.png"),"bottom home tap active ui test Fail"
        assert self.utils.compare_image("message_tap.png",image_list[4],"bottom_message_tap.png"), "bottom messsage tap enabled ui test Fail"
        assert self.utils.compare_image("organization_chart_enabled.png",image_list[5],"bottom_organization_chart_enabled.png"), "bottom organization chart tap enabled ui test Fail"
        
    def test_profile_image(self):
        return
    
    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "logout popup description test Fail"
        btn_list[1].click()
        
        