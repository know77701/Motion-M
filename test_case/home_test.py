from utils.utils import Utils
from config.selectors import Selectors
import time
from appium.webdriver.common.appiumby import AppiumBy


class Home():
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
        self.status_list = ["default","busy","metting","off","default"]
    
    def test_run(self):
        # self.test_home_page_ui_check()
        # self.test_profile_image_check()
        # self.test_status_bottom_sheet_ui_check()
        # self.test_status_stting()
        # self.test_user_card_ui_check()
        # self.test_user_card_status()
        # self.test_user_card_org_chart_oepn()
        # self.test_user_card_value_copy()
        # self.test_user_card_my_chattroom_open()
        # self.test_user_list_ui_check()
        # self.test_pause_notifications_ui_check()
        # self.test_notifications_paused_list_ui_check()
        # self.test_is_notifications_paused_ui_check()
        # self.test_configure_notification_time()
        self.test_auto_message_response()
        
    
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
    
    def test_status_bottom_sheet_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[1].click()
        assert self.utils.compare_image("status_bottom_sheet.png",view_list[3],"status_bottom_sheet.png","home"), "status bottom sheet ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_default.png",view_list[8],"status_bottom_sheet_default.png","home"), "status bottom sheet default ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_busy.png",view_list[9],"status_bottom_sheet_busy.png","home"), "status bottom sheet busy ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_metting.png",view_list[10],"status_bottom_sheet_metting.png","home"), "status bottom sheet metting ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_out_of_office.png",view_list[11],"status_bottom_sheet_out_of_office.png","home"), "status bottom sheet out of office ui test Fail"
        
        self.utils.bottom_sheet_close()
        
    def status_setting(self, status):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        if status == "default":
            view_list[8].click()
        elif status == "busy":
            view_list[9].click()
        elif status == "metting":
            view_list[10].click()
        else:
            view_list[11].click()
        
    def check_status_setting(self, view_element=None, btn_element=None, status=None):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        if view_element:
            view_element.click()
            btn_element.click()
            self.status_setting(status)
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} status user image compare test Fail"
            view_element.click()
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} status setting sheet test Fail"
            self.utils.bottom_sheet_close()
        else:
            btn_element.click()
            self.status_setting(status)
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} status user image compare test Fail"
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} status setting sheet test Fail"
            self.utils.bottom_sheet_close()
        
    def test_status_stting(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
       
        
        for item in self.status_list:
            self.check_status_setting(btn_element=image_list[1],status=item)
        
    def test_user_card_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        compare_text = "이말년의사/대표원장트라이업영문의사/대표원장휴대폰010-7441-7631메일know701@triupcorp.com"
        user_infomation = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        assert user_infomation == compare_text, "user card infomation text compare test Fail"
        assert self.utils.compare_image("user_card.png", view_list[7], "user_card.png","home"), "user bottom sheet ui test Fail" 
        assert self.utils.compare_image("user_card_my_chattingroom_btn.png", image_list[0], "user_card_my_chattingroom_btn.png","home"), "user card my chatting room btn ui test Fail"
        assert self.utils.compare_image("user_card_status_btn.png",btn_list[0],"user_card_status_btn.png","home"), "user card status btn ui test Fail"
        assert self.utils.compare_image("user_card_org_chart_btn.png",btn_list[1],"user_card_org_chart_btn.png","home"), "user card org chart btn ui test Fail"
        assert self.utils.compare_image("user_card_email_copy_btn.png", image_list[1], "user_card_email_copy_btn.png","home"), "user card email copy btn ui test Fail"
        assert self.utils.compare_image("user_card_phone_copy_btn.png", image_list[2], "user_card_phone_copy_btn.png","home"), "user card phone copy btn ui test Fail"
        self.utils.bottom_sheet_close()
        
    def test_user_card_status(self):
        for element in self.status_list:
            view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
            self.check_status_setting(view_list[7],btn_list[0],element)
    
    def test_user_card_org_chart_oepn(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        time.sleep(0.5)
        assert view_list[4].get_attribute("contentDescription") == "조직도", "user card org chart open test Fail"
        for index, element in enumerate(view_list):
            replace_desc = self.utils.element_replace(element.get_attribute("contentDescription"))
            if replace_desc == "이말년의사/대표원장":
                assert self.utils.compare_image("org_chart_my_image.png",view_list[index+1],"org_chart_my_image.png","org_chart"), "org chart user image test Fail"
                assert replace_desc == "이말년의사/대표원장", "org chart user oepn test Fail"
                break
        btn_list[0].click()
    
    def test_user_card_value_copy(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[1].click()
        mobile_copy = self.utils.return_value_copy()
        print(mobile_copy)
        image_list[2].click()
        email_copy = self.utils.return_value_copy()
        print(email_copy)
    
    def test_user_card_my_chattroom_open(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)

        view_list[7].click()
        image_list[0].click()

        assert self.utils.compare_image("my_chatting_room.png",image_list[0], "my_chatting_room.png","home")
        btn_list[0].click()
        self.utils.bottom_sheet_close()

    
    def test_user_list_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        replace_user_name = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        if "의사" in replace_user_name:
            view_list[12].click()
        elif "간호" in replace_user_name:
            view_list[14].click()
        elif "상담" in replace_user_name:
            view_list[16].click()
        elif "간호조무사" in replace_user_name:
            view_list[18].click()
        elif "에스테틱" in replace_user_name:
            view_list[20].click()
        elif "영업" in replace_user_name:
            view_list[22].click()
        elif "마케팅" in replace_user_name:
            view_list[24].click()
        self.utils.get_element_list_print(self.selectors.VIEW_CLASS_NAME)
        
    
    def test_user_ui_check(self):
        return
    
    def test_pause_notifications_ui_check(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[2].click()

        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        assert self.utils.element_replace(view_list[8].get_attribute("contentDescription")) == '알림일시정지설정안함', "is_notifications_paused text compare test Fail"
        assert self.utils.element_replace(view_list[9].get_attribute("contentDescription")) == '알림수신시간설정꺼짐', "message_auto_setting text compare test Fail"
        assert self.utils.element_replace(view_list[10].get_attribute("contentDescription")) == '메시지자동응답꺼짐', "automatic_message_response text compare test Fail"
        assert self.utils.compare_image("pause_notifications_image.png", view_list[5], "pause_notifications_image.png", "home"), "pause_notifications_image ui test Fail"
        assert self.utils.compare_image("is_notifications_paused.png",image_list[0], "is_notifications_paused.png", "home"), "is_notifications_paused ui test Fail"
        assert self.utils.compare_image("is_notifications_paused_open.png",image_list[1], "is_notifications_paused_open.png", "home"), "is_notifications_paused_open ui test Fail"
        assert self.utils.compare_image("message_auto_setting.png",image_list[2], "message_auto_setting.png", "home"), "message_auto_setting ui test Fail"
        assert self.utils.compare_image("message_auto_setting_open.png",image_list[3], "message_auto_setting_open.png", "home"), "message_auto_setting_open ui test Fail"
        assert self.utils.compare_image("automatic_message_response.png",image_list[4], "automatic_message_response.png", "home"), "automatic_message_response ui test Fail"
        assert self.utils.compare_image("automatic_message_response_open.png",image_list[5], "automatic_message_response_open.png", "home"), "automatic_message_response_open ui test Fail"
        self.utils.bottom_sheet_close()
    
    def test_notifications_paused_list_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[2].click()
        image_list[0].click()
        time.sleep(0.5)

        assert view_list[4].get_attribute("contentDescription") == "알림 일시 정지", "is_notifications_paused title text compare test Fail"
        assert view_list[17].get_attribute("contentDescription") == "알람을 일시적으로 끕니다.", "is_notifications_paused sub text compare test Fail"

        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        assert btn_list[1].get_attribute("contentDescription") == "1시간", "is_notifications_paused 1H menu ui test Fail"
        assert btn_list[2].get_attribute("contentDescription") == "2시간", "is_notifications_paused 2H menu ui test Fail"
        assert btn_list[3].get_attribute("contentDescription") == "3시간", "is_notifications_paused 3H menu ui test Fail"
        assert btn_list[4].get_attribute("contentDescription") == "오전 8시까지", "Notification pause menu UI test failed: 4th button's contentDescription does not match 'Until 8 AM'"
        assert btn_list[5].get_attribute("contentDescription") == "오전 9시까지", "Notification pause menu UI test failed: 5th button's contentDescription does not match 'Until 9 AM'"
        assert btn_list[6].get_attribute("contentDescription") == "해제 할 때까지", "Notification pause menu UI test failed: 6th button's contentDescription does not match 'Until turned off'"
        btn_list[0].click()

    def test_configure_notification_time(self):
        # image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        # image_list[2].click()
        # image_list[2].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        switch_list = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)
        
        notification_time_title = self.utils.element_replace(view_list[4].get_attribute("contentDescription"))
        notification_time_menu_title = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        notification_time_menu_title2 = self.utils.element_replace(switch_list[1].get_attribute("contentDescription"))
        
        assert notification_time_title == "알림수신시간", "notification time title description does not match '알림 수신 시간'"
        assert notification_time_menu_title == "알림수신시간설정", "notification time title description does not match '알림 수신 시간 설정'"
        assert notification_time_menu_title2 == "공휴일알림끄기", "notification time title description does not match '공휴일 알림 끄기'"
        assert self.utils.compare_image("notification_time_setting_switch.png", switch_list[0], "notification_time_setting_switch.png", "home")
        assert self.utils.compare_image("weekendotification_switch.png", switch_list[1], "weekendotification_switch.png", "home")
        notification_setting_btn = switch_list[0]
        holiday_setting_btn = switch_list[1]
    
        notification_setting_btn.click()
        holiday_setting_btn.click()
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        
    def test_is_notifications_paused_ui_check(self):
        notification_steps = [
            (1, "active_1hour_list.png"),
            (2, "active_2hour_list.png"),
            (3, "active_3hour_list.png"),
            (4, "active_8hour_list.png"),
            (5, "active_8hour_list.png"),
            (6, "active_8hour_list.png"),
        ]
        
        self.notification_menu_text_compare("설정안함")

        for (setting_num, expected_image) in notification_steps:
            self.perform_notification_test(setting_num, expected_image)

        self.notificaiton_test_setting_reset()

    def perform_notification_test(self, setting_num, expected_image):
        self.set_notifications(setting_num)
        self.notification_resubscribe_button(setting_num)
        return_time = self.notifications_paused_list_ui_check(setting_num, expected_image)
        self.notifications_puased_menu_icon_ui_check()
        self.notification_menu_text_compare(return_time)
        
 
    def notificaiton_test_setting_reset(self):
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_description = self.utils.element_replace(btn_list[7].get_attribute("contentDescription"))
        if "알림다시받기" in btn_description:
            btn_list[7].click()
        btn_list[0].click()
 
    def notifications_paused_list_ui_check(self, btn_number=None, file_name=None):
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        return_time = ""
        
        if btn_number == 1 or btn_number == 2 or btn_number == 3:
            return_time = self.utils.get_time_with_hour_added(btn_number)
            active_time_list = self.set_notifications_button_check(file_name, btn_list[btn_number], "home")
            assert return_time in view_list[19].get_attribute("contentDescription"), "notifications_paused time text test Fail"
            assert active_time_list, "list setting ui check test Fail"
            btn_list[0].click()
            
            return return_time
        else:
            if btn_number == 4:
                return_time = "08:00"
            elif btn_number == 5:
                return_time = "09:00"
            elif btn_number == 6:
                return_time = "해제"

            active_time_list = self.set_notifications_button_check(file_name, btn_list[btn_number], "home")
            assert return_time in view_list[19].get_attribute("contentDescription"), "notifications_paused time text test Fail"
            assert active_time_list, "list setting ui check test Fail"
            btn_list[0].click()
            return return_time

    def notifications_puased_menu_icon_ui_check(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        notifications_icon_compare = self.utils.compare_image("is_notifications_paused_menu_icon.png", image_list[2], "is_notifications_paused_menu_icon.png", "home")
        assert notifications_icon_compare, "notification icon ui test Fail"
 
        
    def notification_menu_text_compare(self, compare_index):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[2].click()
        return_menu_text = self.utils.element_replace(view_list[8].get_attribute("contentDescription"))
        assert compare_index in return_menu_text, f"{return_menu_text} is not in {compare_index} test Fails"
        image_list[0].click()

    def notification_resubscribe_button(self,index):
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        reactive_btn_result = self.set_notifications_button_check("reactivate_notifications.png", btn_list[7], "home")
        assert reactive_btn_result, "reactivate_notifications_btn ui check test Fail"
        btn_list[7].click()
        self.set_notifications(index)

    def set_notifications_button_check(self, image_name, element, compoent):
        sucess_value = self.utils.compare_image(image_name, element, image_name, compoent)
        return sucess_value
    
    def set_notifications(self,index):
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[index].click()
        
    def test_auto_message_response(self):
        # view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        # switch_btn = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)[0]
        
        # self.verify_auto_message_off_title(view_list)
        # self.verify_auto_message_off_ui(view_list, switch_btn)
        # self.set_message_auto_resopnse(switch_btn)
        
        # active_setting_view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        # self.verify_auto_message_on_title(active_setting_view_list)
        # self.verify_auto_message_on_ui(active_setting_view_list, switch_btn)

        # self.verify_auto_message_list_menu_modal()
        # self.set_message_auto_resopnse(switch_btn)
        
        # self.menu_back_btn_click()
        self.auto_message_time_update()

        
    def verify_auto_message_off_title(self, view_list):
        auto_message_response_title = view_list[4].get_attribute("contentDescription")
        auto_message_response_setting_list_title = view_list[8].get_attribute("contentDescription")
        assert auto_message_response_title == "메시지 자동 응답", "메시지 자동 응답 타이틀 비교 테스트 실패"
        assert auto_message_response_setting_list_title == "메시지 자동 응답", "메시지 자동 응답 설정 타이틀 비교 테스트 실패"
    
    def verify_auto_message_off_ui(self, view_list, switch_btn):
        auto_message_title_ui_check = self.utils.compare_image("message_auto_response_title.png", view_list[4], "message_auto_response_title.png", "home")
        auto_message_setting_list_title_ui_check = self.utils.compare_image("message_auto_response_setting_list_title.png", view_list[8], "message_auto_response_setting_list_title.png", "home")
        auto_message_switch_btn_image_compare = self.utils.compare_image("message_auto_response_setting_btn.png", switch_btn, "message_auto_response_setting_btn.png", "home")
        assert auto_message_title_ui_check, "메시지 자동 응답 타이틀 UI 비교 테스트 실패"
        assert auto_message_setting_list_title_ui_check, "메시지 자동 응답 리스트 타이틀 UI 비교 테스트 실패"
        assert auto_message_switch_btn_image_compare, "메시지 자동 응답 OFF 버튼 UI 비교 테스트 실패"
    
    def verify_auto_message_on_title(self, view_list):
        auto_message_notification_time_title = view_list[9].get_attribute("contentDescription")
        base_country_time = view_list[10].get_attribute("contentDescription")
        auto_message_notification_setting_time = self.utils.element_replace(view_list[11].get_attribute("contentDescription"))
        auto_message_notification_setting_append_btn_text = view_list[12].get_attribute("contentDescription")
        auto_message_setting_title = view_list[13].get_attribute("contentDescription")
        
        assert auto_message_notification_time_title == "알림 수신 시간", "알림 수신 시간 서브 타이틀 비교 테스트 실패"
        assert base_country_time == "GMT +09:00 서울", "기준 나라 시간 타이틀 비교 테스트 실패"
        assert auto_message_notification_setting_time == "매일오전07:00~오후10:00", "알림 수신 시간 기본 값 텍스트 비교 테스트 실패"
        assert auto_message_notification_setting_append_btn_text == "시간설정 추가", "시간설정 추가 버튼 텍스트 비교 테스트 실패"
        assert auto_message_setting_title == "자동 응답 내용", "자동 응답 내용 입력 타이틀 비교 테스트 실패"
        
    def verify_auto_message_on_ui(self, view_list,switch_btn):
        auto_message_notification_time_title_compare_value = self.utils.compare_image("auto_message_notification_time_title.png",view_list[9],"auto_message_notification_time_title.png", "home")
        auto_message_base_country_time_compare_value = self.utils.compare_image("auto_message_base_country_time.png",view_list[10],"auto_message_base_country_time.png", "home")
        auto_message_notification_setting_time_compare_value = self.utils.compare_image("auto_message_notification_setting_time.png",view_list[11],"auto_message_notification_setting_time.png", "home")
        auto_message_notification_setting_append_btn_text_compare_value = self.utils.compare_image("auto_message_notification_setting_append_btn_text.png",view_list[12],"auto_message_notification_setting_append_btn_text.png", "home")
        auto_message_setting_title_compare_value = self.utils.compare_image("auto_message_setting_title.png",switch_btn,"auto_message_setting_title.png", "home")
        
        assert auto_message_notification_time_title_compare_value, "알림 수신 시간 서브 타이틀 비교 테스트 실패"
        assert auto_message_base_country_time_compare_value, "기준 나라 시간 타이틀 비교 테스트 실패"
        assert auto_message_notification_setting_time_compare_value, "알림 수신 시간 기본 값 텍스트 비교 테스트 실패"
        assert auto_message_notification_setting_append_btn_text_compare_value, "시간설정 추가 버튼 텍스트 비교 테스트 실패"
        assert auto_message_setting_title_compare_value, "자동 응답 내용 입력 타이틀 비교 테스트 실패"
    
    def verify_auto_message_list_menu_modal(self):
        self.auto_message_setting_list_menu_oepn()
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        self.verify_auto_message_modal_title(btn_list)
        self.verify_auto_message_modal_ui(view_list, btn_list)
        self.verify_auto_message_defalut_time_delete(btn_list[1])
    
    def menu_back_btn_click(self):
        back_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[0]
        back_btn.click()
        
    def auto_message_setting_list_menu_oepn(self):
        setting_menu_btn = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)[0]
        setting_menu_btn.click()
    
    def verify_auto_message_modal_title(self, btn_list):
        update_btn = btn_list[0].get_attribute("contentDescription")
        delete_btn = btn_list[1].get_attribute("contentDescription")
        
        assert update_btn == "편집", "메시지 자동 응답 모달 업데이트 버튼 텍스트 비교 테스트 실패"
        assert delete_btn == "삭제", "메시지 자동 응답 모달 삭제 버튼 텍스트 비교 테스트 실패"
        
    def verify_auto_message_modal_ui(self, view_list, btn_list):
        update_btn_ui_compare = self.utils.compare_image("auto_message_menu_modal_update_btn.png", btn_list[0], "auto_message_menu_modal_update_btn.png", "home")
        delete_btn_ui_compare = self.utils.compare_image("auto_message_menu_modal_delete_btn.png", btn_list[1], "auto_message_menu_modal_delete_btn.png", "home")
        modal_ui_compare = self.utils.compare_image("auto_message_menu_modal.png", view_list[6], "auto_message_menu_modal.png", "home")
        assert modal_ui_compare, "메시지 자동 응답 모달 UI 비교 테스트 실패"
        assert update_btn_ui_compare, "메시지 자동 응답 모달 업데이트 버튼 UI 비교 테스트 실패"
        assert delete_btn_ui_compare, "메시지 자동 응답 모달 삭제 버튼 UI 비교 테스트 실패"
        
    def verify_auto_message_defalut_time_delete(self, delete_btn):
        delete_btn.click()
        toast_popup = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)[19]
        toast_popup_compare = self.utils.compare_image("auto_message_default_delete_toast.png", toast_popup, "auto_message_default_delete_toast.png", "home")
        
        assert toast_popup.get_attribute("contentDescription") == "최소 하나의 알림시간이 설정되어야 합니다", "메시지 자동 응답 기본값 삭제 토스트 팝업 문구 비교 테스트 실패"
        assert toast_popup_compare, "메시지 자동 응답 기본값 삭제 토스트 팝업 UI 비교 테스트 실패"

    def auto_message_time_update_menu_open(self, update_btn):
        update_btn.click()

    def auto_message_time_update(self):
        update_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[0]
        menu_active_btn = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)[0]
        # self.set_message_auto_resopnse(menu_active_btn)
        # self.auto_message_setting_list_menu_oepn()
        # self.auto_message_time_update_menu_open(update_btn)
        self.verify_auto_message_time_update_page()

    def verify_auto_message_time_update_page(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        checkbox_list = self.utils.get_all_elements(self.selectors.CHECKBOX_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        switch_list = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)
        
        # self.verify_auto_message_update_title(view_list, image_list)
        # self.verify_auto_message_update_ui(view_list, image_list, switch_list, checkbox_list)
        # day_list = [
        #     'enabled_mon_day.png',
        #     'enabled_tue_day.png',
        #     'enabled_wen_day.png',
        #     'enabled_thu_day.png',
        #     'enabled_fri_day.png',
        #     'enabled_sta_day.png',
        #     'enabled_sun_day.png',
        # ]
        # self.auto_message_select_all_day_select(checkbox_list, day_list)
        # self.verify_auto_message_none_day_select(checkbox_list)
        self.auto_message_update_time_setting(image_list)
        
        
    def auto_message_select_all_day_select(self,checkbox_list,day_list):
        for index,day in enumerate(day_list):
            self.verify_auto_message_update_day_setting(checkbox_list[index], day)
        for index,day in enumerate(day_list):
            self.verify_auto_message_update_day_setting(checkbox_list[index])
    
    def verify_auto_message_update_title(self, view_list, image_list):
        setting_save_btn = view_list[5].get_attribute("contentDescription")
        setting_basic_time = view_list[11].get_attribute("contentDescription")
        default_menu_start_time = self.utils.element_replace(image_list[0].get_attribute("contentDescription"))
        default_menu_end_time = self.utils.element_replace(image_list[1].get_attribute("contentDescription"))
        
        assert setting_save_btn == "확인", "확인 버튼 텍스트 비교 테스트 실패"
        assert setting_basic_time == "GMT + 09:00 서울", "확인 버튼 텍스트 비교 테스트 실패"
        assert default_menu_start_time == "시작오전07:00", "메시지 자동응답 시작시간 텍스트 비교 테스트 실패"
        assert default_menu_end_time == "종료오후10:00", "메시지 자동응답 종료시간 텍스트 비교 테스트 실패"
    
    def verify_auto_message_update_ui(self,view_list, image_list, switch_list, checkbox_list):
        save_btn_ui_compare_value = self.utils.compare_image("auto_message_update_setting_save_btn.png", view_list[5], "auto_message_update_setting_save_btn.png","home")
        # all_time_enabled_ui_compare_value = self.utils.compare_image("auto_message_all_time_enabled.png", switch_list[0], "auto_message_update_setting_save_btn.png","home")
        update_setting_start_time_ui_compare_value = self.utils.compare_image("auto_message_update_setting_start_time.png", image_list[0], "auto_message_update_setting_start_time.png","home")
        update_setting_end_time_ui_compare_value = self.utils.compare_image("auto_message_update_setting_end_time.png", image_list[1], "auto_message_update_setting_end_time.png","home")
        auto_message_mon_ui_compare_value = self.utils.compare_image("auto_message_mon.png", checkbox_list[0], "auto_message_mon.png","home")
        auto_message_tue_ui_compare_value = self.utils.compare_image("auto_message_tue.png", checkbox_list[1], "auto_message_tue.png","home")
        auto_message_wen_ui_compare_value = self.utils.compare_image("auto_message_wen.png", checkbox_list[2], "auto_message_wen.png","home")
        auto_message_thu_ui_compare_value = self.utils.compare_image("auto_message_thu.png", checkbox_list[3], "auto_message_thu.png","home")
        auto_message_fri_ui_compare_value = self.utils.compare_image("auto_message_fri.png", checkbox_list[4], "auto_message_fri.png","home")
        auto_message_sat_ui_compare_value = self.utils.compare_image("auto_message_sat.png", checkbox_list[5], "auto_message_sat.png","home")
        auto_message_sun_ui_compare_value = self.utils.compare_image("auto_message_sun.png", checkbox_list[6], "auto_message_sun.png","home")
        
        assert save_btn_ui_compare_value, "메시지 자동응답 수정 페이지 확인 버튼 UI 비교 테스트 실패"
        # assert all_time_enabled_ui_compare_value, "메시지 자동응답 수정 페이지 종일 버튼 UI 비교 테스트 실패"
        assert update_setting_start_time_ui_compare_value, "메시지 자동응답 수정 페이지 시작 시간 UI 비교 테스트 실패"
        assert update_setting_end_time_ui_compare_value, "메시지 자동응답 수정 페이지 종료 시간 UI 비교 테스트 실패"
        assert auto_message_mon_ui_compare_value, "메시지 자동응답 수정 페이지 월요일 UI 비교 테스트 실패"
        assert auto_message_tue_ui_compare_value, "메시지 자동응답 수정 페이지 화요일 UI 비교 테스트 실패"
        assert auto_message_wen_ui_compare_value, "메시지 자동응답 수정 페이지 수요일 UI 비교 테스트 실패"
        assert auto_message_thu_ui_compare_value, "메시지 자동응답 수정 페이지 목요일 UI 비교 테스트 실패"
        assert auto_message_fri_ui_compare_value, "메시지 자동응답 수정 페이지 금요일 UI 비교 테스트 실패"
        assert auto_message_sat_ui_compare_value, "메시지 자동응답 수정 페이지 토요일 UI 비교 테스트 실패"
        assert auto_message_sun_ui_compare_value, "메시지 자동응답 수정 페이지 일요일 UI 비교 테스트 실패"
    
    def verify_auto_message_none_day_select(self,checkbox_list):
        for index in range(7):
            self.verify_auto_message_update_day_setting(checkbox_list[index])
            
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        for item in view_list:
            desc = item.get_attribute("contentDescription")
            assert desc != "확인", "메시지 자동 응답 날짜 미지정 확인버튼 미노출 테스트 실패"
        
        for index in range(7):
            self.verify_auto_message_update_day_setting(checkbox_list[index])
    
    def verify_auto_message_update_day_setting(self, index_btn, file_name=None):
        index_btn.click()
        if file_name:
            assert self.utils.compare_image(file_name, index_btn, file_name, "home")

    def auto_message_update_time_setting(self, time_btn):
        time_btn[0].click()
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        self.verify_auto_message_update_default_start_time_setting_ui(view_list,btn_list)
        btn_list[0].click()

        time_btn[1].click()
        self.verify_auto_message_update_default_end_time_setting_ui(view_list,btn_list)
        btn_list[0].click()
        
    def verify_auto_message_update_default_start_time_setting_ui(self,view_list,btn_list):
        default_time_popup_ui_compare_result = self.utils.compare_image("default_start_time_popup.png", view_list[4], "default_start_time_popup.png", "home")
        active_am_ui_compare_result = self.utils.compare_image("active_start_am_setting.png", view_list[5], "active_am_setting.png", "home")
        enabled_pm_ui_compare_result = self.utils.compare_image("enabled_start_pm_stting.png", view_list[6], "enabled_pm_stting.png", "home")
        popup_cancle_btn_ui_compare_result = self.utils.compare_image("default_start_time_popup_cancle_btn.png", btn_list[0], "default_start_time_popup_cancle_btn.png", "home")
        popup_save_btn_ui_compare_result = self.utils.compare_image("default_start_time_popup_save_btn.png", btn_list[1], "default_start_time_popup_save_btn.png", "home")
        
        assert default_time_popup_ui_compare_result, "기본 설정 시간 UI 비교 테스트 실패"
        assert active_am_ui_compare_result, "기본설정 AM 값 UI 비교 테스트 실패"
        assert enabled_pm_ui_compare_result, "기본설정 PM 값 UI 비교 테스트 실패"
        assert popup_cancle_btn_ui_compare_result, "팝업 취소 버튼 UI 비교 테스트 실패"
        assert popup_save_btn_ui_compare_result, "팝업 확인 버튼 UI 비교 테스트 실패"
    
    def verify_auto_message_update_default_end_time_setting_ui(self,view_list,btn_list):
        default_time_popup_ui_compare_result = self.utils.compare_image("default_end_time_popup.png", view_list[4], "default_start_time_popup.png", "home")
        active_am_ui_compare_result = self.utils.compare_image("enabled_end_am_setting.png", view_list[5], "enabled_am_setting.png", "home")
        enabled_pm_ui_compare_result = self.utils.compare_image("active_end_pm_stting.png", view_list[6], "active_pm_stting.png", "home")
        popup_cancle_btn_ui_compare_result = self.utils.compare_image("default_end_time_popup_cancle_btn.png", btn_list[0], "default_time_popup_cancle_btn.png", "home")
        popup_save_btn_ui_compare_result = self.utils.compare_image("default_end_time_popup_save_btn.png", btn_list[1], "default_time_popup_save_btn.png", "home")
        
        assert default_time_popup_ui_compare_result, "기본 설정 시간 UI 비교 테스트 실패"
        assert active_am_ui_compare_result, "기본설정 AM 값 UI 비교 테스트 실패"
        assert enabled_pm_ui_compare_result, "기본설정 PM 값 UI 비교 테스트 실패"
        assert popup_cancle_btn_ui_compare_result, "팝업 취소 버튼 UI 비교 테스트 실패"
        assert popup_save_btn_ui_compare_result, "팝업 확인 버튼 UI 비교 테스트 실패"
    
    def set_popup_time(self):
        return
    
    def set_message_auto_resopnse(self, switch_btn):
        switch_btn.click()
    
    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "logout popup description test Fail"
        btn_list[1].click()
    
    

class setting:
    def __init__(self,driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
    
    def test_run(self):
        return
    
    def test_setting_menu_ui_check(self):
        return