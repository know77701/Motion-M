from utils.utils import Utils
from config.selectors import Selectors
import time
from appium.webdriver.common.appiumby import AppiumBy
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput


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
        # self.test_status_setting()
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
        # self.test_configure_notification_time_delete()
        self.test_auto_message_response()
        
    
    def test_home_page_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        user_name_replace = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        home_title = view_list[5].get_attribute("contentDescription")
        
        assert home_title == "트라이업영문", "병원명 타이틀 텍스트 비교 테스트 실패"
        assert user_name_replace == "이말년의사/대표원장", "홈 유저 이름 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_image.png",view_list[8],"home_user_image.png","home"), "홈 유저 이미지 UI 비교 테스트 실패"
        assert self.utils.compare_image("setting_button.png",image_list[0],"home_setting_button.png","home"), "홈 세팅 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("status_setting.png",image_list[1],"home_status_setting.png","home"), "홈 유저 상태 세팅 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("alert_setting.png",image_list[2],"home_alert_setting.png","home"), "홈 알림 설정 세팅 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_message_chatting_room.png",btn_list[0],"user_message_chatting_room.png","home"), "나와의 메시지 진입 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("home_tap.png",image_list[3],"bottom_home_tap.png","home"),"바텀 네비게이션 홈 컴포넌트 UI 비교 테스트 실패"
        assert self.utils.compare_image("message_tap.png",image_list[4],"bottom_message_tap.png","home"), "바텀 네비게이션 메시지 컴포넌트 UI 비교 테스트 실패"
        assert self.utils.compare_image("organization_chart_enabled.png",image_list[5],"bottom_organization_chart_enabled.png","home"), "바텀 네비게이션 조직도 컴포넌트 UI 비교 테스트 실패"
        
    def test_profile_image_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[8].click()
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        assert self.utils.compare_image("view_user_image.png",image_list[0],"view_user_image.png","home"), "유저 이미지 UI 비교 테스트 실패"
        self.navigate_back_from_menu()
    
    def test_status_bottom_sheet_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[1].click()
        assert self.utils.compare_image("status_bottom_sheet.png",view_list[3],"status_bottom_sheet.png","home"), "상태 설정 바텀시트 UI 비교 테스트 실패"
        assert self.utils.compare_image("status_bottom_sheet_default.png",view_list[8],"status_bottom_sheet_default.png","home"), "상태 바텀시트 기본값 UI 비교 테스트 실패"
        assert self.utils.compare_image("status_bottom_sheet_busy.png",view_list[9],"status_bottom_sheet_busy.png","home"), "상태 바텀시트 바쁨값 UI 비교 테스트 실패"
        assert self.utils.compare_image("status_bottom_sheet_metting.png",view_list[10],"status_bottom_sheet_metting.png","home"), "상태 바텀시트 회의중값 UI 비교 테스트 실패"
        assert self.utils.compare_image("status_bottom_sheet_out_of_office.png",view_list[11],"status_bottom_sheet_out_of_office.png","home"), "상태 바텀시트 자리비움값 UI 비교 테스트 실패"
        
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
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} 상태값 설정 유저 이미지 UI 비교 테스트 실패"
            view_element.click()
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} 상태값 설정 바텀시트 UI 비교 테스트 실패"
            self.utils.bottom_sheet_close()
        else:
            btn_element.click()
            self.status_setting(status)
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} 상태값 설정 유저 이미지 UI 비교 테스트 실패"
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} 상태값 설정 바텀시트 UI 비교 테스트 실패"
            self.utils.bottom_sheet_close()
        
    def test_status_setting(self):
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
        assert self.utils.compare_image("user_card.png", view_list[7], "user_card.png","home"), "유저 바텀시트 UI 비교 테스트 실패" 
        assert self.utils.compare_image("user_card_my_chattingroom_btn.png", image_list[0], "user_card_my_chattingroom_btn.png","home"), "유저 바텀시트 나와의 메시지 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_card_status_btn.png",btn_list[0],"user_card_status_btn.png","home"), "유저 바텀시트 상태값 설정 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_card_org_chart_btn.png",btn_list[1],"user_card_org_chart_btn.png","home"), "유저 바텀시트 조직도 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_card_email_copy_btn.png", image_list[1], "user_card_email_copy_btn.png","home"), "유저 바텀시트 이메일 복사 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("user_card_phone_copy_btn.png", image_list[2], "user_card_phone_copy_btn.png","home"), "유저 바텀시트 핸드폰번호 복사 버튼 UI 비교 테스트 실패"
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
        assert view_list[4].get_attribute("contentDescription") == "조직도", "유저 바텀시트 조직도 진입 동작 실패(상단 조직도 문구 미노출)"
        for index, element in enumerate(view_list):
            replace_desc = self.utils.element_replace(element.get_attribute("contentDescription"))
            if replace_desc == "이말년의사/대표원장":
                assert self.utils.compare_image("org_chart_my_image.png",view_list[index+1],"org_chart_my_image.png","org_chart"), "조직도 유저 설정 이미지 UI 비교 테스트 실패"
                assert replace_desc == "이말년의사/대표원장", "조직도 유저 설정 이름/직책 비교 테스트 실패"
                break
        self.navigate_back_from_menu()
    
    def test_user_card_value_copy(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[1].click()
        mobile_copy = self.utils.return_value_copy()
        image_list[2].click()
        email_copy = self.utils.return_value_copy()
    
    def test_user_card_my_chattroom_open(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        view_list[7].click()
        image_list[0].click()

        assert self.utils.compare_image("my_chatting_room.png",image_list[0], "my_chatting_room.png","home"), "나와의 메시지 진입 UI 비교 테스트 실패"
        self.navigate_back_from_menu()
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
        # 데이터 받아온 뒤 테스트 진행예정
        return
    
    def test_pause_notifications_ui_check(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[2].click()

        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        assert self.utils.element_replace(view_list[8].get_attribute("contentDescription")) == '알림일시정지설정안함', "알림 일시정지 기본값 텍스트 비교 테스트 실패"
        assert self.utils.element_replace(view_list[9].get_attribute("contentDescription")) == '알림수신시간설정꺼짐', "알림 수신시간 설정 기본값 텍스트 비교 테스트 실패"
        assert self.utils.element_replace(view_list[10].get_attribute("contentDescription")) == '메시지자동응답꺼짐', "메시지 자동응답 기본값 텍스트 비교 테스트 실패"
        assert self.utils.compare_image("pause_notifications_image.png", view_list[5], "pause_notifications_image.png", "home"), "알림 바텀시트 UI 비교 테스트 실패"
        assert self.utils.compare_image("is_notifications_paused.png",image_list[0], "is_notifications_paused.png", "home"), "알림 일시정지 아이콘 UI 비교 테스트 실패"
        assert self.utils.compare_image("is_notifications_paused_open.png",image_list[1], "is_notifications_paused_open.png", "home"), "알림 일시정지 진입 아이콘 UI 비교 테스트 실패"
        assert self.utils.compare_image("message_auto_setting.png",image_list[2], "message_auto_setting.png", "home"), "알림 수신 시간 설정 아이콘 UI 비교 테스트 실패"
        assert self.utils.compare_image("message_auto_setting_open.png",image_list[3], "message_auto_setting_open.png", "home"), "알림 수신 시간 설정 진입 아이콘 UI 비교 테스트 실패"
        assert self.utils.compare_image("automatic_message_response.png",image_list[4], "automatic_message_response.png", "home"), "메시지 자동 응답 아이콘 UI 비교 테스트 실패"
        assert self.utils.compare_image("automatic_message_response_open.png",image_list[5], "automatic_message_response_open.png", "home"), "메시지 자동 응답 진입 아이콘 UI 비교 테스트 실패"
        self.utils.bottom_sheet_close()
    
    def open_notifiaction_test_menu(self, list_number, index_number):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[list_number].click()
        image_list[index_number].click()
        
    def test_notifications_paused_list_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        self.open_notifiaction_test_menu(2,0)
        time.sleep(0.5)

        assert view_list[4].get_attribute("contentDescription") == "알림 일시 정지", "알림 일시정지 타이틀 텍스트 비교 테스트 실패"
        assert view_list[17].get_attribute("contentDescription") == "알람을 일시적으로 끕니다.", "알림 일시정지 기본 노출 텍스트 비교 테스트 실패"

        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        assert btn_list[1].get_attribute("contentDescription") == "1시간", "알림 일시정지 1시간 설정 텍스트 비교 테스트 실패"
        assert btn_list[2].get_attribute("contentDescription") == "2시간", "알림 일시정지 2시간 설정 텍스트 비교 테스트 실패"
        assert btn_list[3].get_attribute("contentDescription") == "3시간", "알림 일시정지 3시간 설정 텍스트 비교 테스트 실패"
        assert btn_list[4].get_attribute("contentDescription") == "오전 8시까지", "오전 8시까지 설정 텍스트 비교 테스트 실패"
        assert btn_list[5].get_attribute("contentDescription") == "오전 9시까지", "오전 9시까지 설정 텍스트 비교 테스트 실패"
        assert btn_list[6].get_attribute("contentDescription") == "해제 할 때까지", "해제할 때까지 설정 텍스트 비교 테스트 실패"
        self.navigate_back_from_menu()
        
    def verify_notification_time_settings(self, view_list, switch_list):
        notification_time_title = self.utils.element_replace(view_list[4].get_attribute("contentDescription"))
        notification_time_menu_title = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        notification_time_menu_title2 = self.utils.element_replace(switch_list[1].get_attribute("contentDescription"))

        assert notification_time_title == "알림수신시간", "알림 수신시간 타이틀 텍스트 비교 테스트 실패"
        assert notification_time_menu_title == "알림수신시간설정", "알림 수신시간 설정 메뉴 텍스트 비교 테스트 실패"
        assert notification_time_menu_title2 == "공휴일알림끄기", "공휴일 알림 끄기 설정 메뉴 텍스트 비교 테스트 실패"
        assert self.utils.compare_image("notification_time_setting_switch.png", switch_list[0], "notification_time_setting_switch.png", "home"), "알림 수신 시간 설정 OFF 스위치 버튼 UI 비교 테스트 실패"
        assert self.utils.compare_image("weekendotification_switch.png", switch_list[1], "weekendotification_switch.png", "home"), "공휴일 알림 끄기 메뉴 UI 비교 테스트 실패" 
    
    def toggle_notification_settings(self, switch_list):
        notification_setting_btn = switch_list[0]
        notification_setting_btn.click()
        
    def verify_notification_subtitles(self, view_list, switch_list):
        notification_time_sub_title = self.utils.element_replace(view_list[8].get_attribute("contentDescription"))
        notification_time_standard = self.utils.element_replace(view_list[9].get_attribute("contentDescription"))
        notifiaction_default_time = self.utils.element_replace(view_list[10].get_attribute("contentDescription"))

        assert notification_time_sub_title == "알림수신시간", "알림 수신 시간 메뉴 타이틀 UI 비교 테스트 실패"
        assert notification_time_standard == "GMT+09:00서울", "기준 시간 타이틀 UI 비교 테스트 실패"
        assert notifiaction_default_time == "매일오전07:00~오후10:00", "기본 설정 시간 비교 테스트 실패"
        assert self.utils.compare_image("notification_time_setting_active.png", switch_list[0],"notification_time_setting_active.png", "home"), "알림 수신 시간 설정 ON 상태 UI 비교 테스트 실패"
        
    def verify_notification_menu_modal(self,view_list):
        self.notifiaction_menu_open()
        setting_menu_ui_compare = self.utils.compare_image("notification_time_setting_bottom_sheet.png", view_list[7],"notification_time_setting_bottom_sheet.png","home")
        assert setting_menu_ui_compare,"메뉴 모달 UI 비교 테스트 실패"
        self.utils.bottom_sheet_close()

    def notifiaction_menu_open(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        setting_menu_btn = image_list[0]
        setting_menu_btn.click()
        
    def navigate_back_from_menu(self):
        back_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[0]
        back_btn.click()
    
    def test_configure_notification_time(self):
        self.open_notifiaction_test_menu(2, 2)
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        switch_list = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)

        self.verify_notification_time_settings(view_list, switch_list)
        self.toggle_notification_settings(switch_list)
        self.verify_notification_subtitles(view_list,switch_list)
        self.verify_notification_menu_modal(view_list)
        self.toggle_notification_settings(switch_list)
        self.navigate_back_from_menu()
        
    def test_configure_notification_time_delete(self):
        self.open_notifiaction_test_menu(2,2)
        switch_list = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)
        self.toggle_notification_settings(switch_list)
        self.notifiaction_menu_open()
        self.delete_notification_time_setting()
        self.check_delete_toast_popup()
        self.toggle_notification_settings(switch_list)
        self.navigate_back_from_menu()
    
    def delete_notification_time_setting(self):
        delete_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[1]
        delete_btn.click()
    
    def check_delete_toast_popup(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        toast_popup = view_list[14]
        toast_popup_ui_compare = self.utils.compare_image("default_delete_toast_popup.png", toast_popup, "default_delete_toast_popup.png", "home")
        toast_text = self.utils.element_replace(toast_popup.get_attribute("contentDescription"))

        assert toast_popup_ui_compare, "알림 수신 시간 설정 기본값 삭제 토스트 팝업 UI 비교 테스트 실패"
        assert toast_text == "최소하나의알림시간이설정되어야합니다", "토스트팝업 문구 비교 테스트 실패"
    
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
        self.navigate_back_from_menu()
 
    def notifications_paused_list_ui_check(self, btn_number=None, file_name=None):
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        return_time = ""
        
        if btn_number == 1 or btn_number == 2 or btn_number == 3:
            return_time = self.utils.get_time_with_hour_added(btn_number)
            active_time_list = self.set_notifications_button_check(file_name, btn_list[btn_number], "home")
            assert return_time in view_list[19].get_attribute("contentDescription"), "notifications_paused time text test Fail"
            assert active_time_list, "list setting ui check test Fail"
            self.navigate_back_from_menu()
            
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
            self.navigate_back_from_menu()
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
        # self.open_notifiaction_test_menu(2,4)
        # view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        # switch_btn = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)[0]
        
        # self.verify_auto_message_off_title(view_list)
        # self.verify_auto_message_off_ui(view_list, switch_btn)
        # self.set_auto_message_menu_control(switch_btn)
        
        # active_setting_view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        # self.verify_auto_message_on_title(active_setting_view_list)
        # self.verify_auto_message_on_ui(active_setting_view_list, switch_btn)

        # self.verify_auto_message_list_menu_modal()
        # self.set_auto_message_menu_control(switch_btn)
        
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
        # time.sleep(3)
        # self.open_notifiaction_test_menu(2,4)
        # update_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[0]
        # menu_active_btn = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)[0]
        # self.set_auto_message_menu_control(menu_active_btn)
        # self.auto_message_setting_list_menu_oepn()
        # self.auto_message_time_update_menu_open(update_btn)
        self.verify_auto_message_time_update_page()
        # self.menu_back_btn_click()
        
        # self.setting_back_modal_control()
        
        
    def verify_auto_message_time_update_page(self):
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        checkbox_list = self.utils.get_all_elements(self.selectors.CHECKBOX_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        switch_list = self.utils.get_all_elements(self.selectors.SWITCH_CLASS_NAME)
        
        self.verify_auto_message_update_title(view_list, image_list)
        self.verify_auto_message_update_ui(view_list, image_list, switch_list, checkbox_list)
        day_list = [
            'enabled_mon_day.png',
            'enabled_tue_day.png',
            'enabled_wen_day.png',
            'enabled_thu_day.png',
            'enabled_fri_day.png',
            'enabled_sta_day.png',
            'enabled_sun_day.png',
        ]
        self.auto_message_select_all_day_select(checkbox_list, day_list)
        self.verify_auto_message_none_day_select(checkbox_list)
        self.auto_message_update_time_setting(image_list)
        setting_days = self.random_day_select(checkbox_list)
        
        start_time = self.random_time_setting(image_list, "start")
        end_time = self.random_time_setting(image_list, "end")
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        view_start_time = self.utils.element_replace(image_list[0].get_attribute("contentDescription"))
        view_end_time = self.utils.element_replace(image_list[1].get_attribute("contentDescription"))
        
        self.verify_setting_time(start_time, view_start_time[4:])
        self.verify_setting_time(end_time, view_end_time[4:])
        # self.verify_setting_day(setting_days, )
        print(setting_days)
        print(image_list[0].get_attribute("contentDescription"))
        print(image_list[1].get_attribute("contentDescription"))
        
    def verify_setting_day(self, select_days, compare_day):
        return
    
    def verify_setting_time(self, time_value, compare_time_value):
        assert time_value == compare_time_value, "설정 시간 텍스트 비교 실패"
    
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
        self.verify_auto_message_default_time_setting(time_btn[0], "start")
        self.verify_auto_message_default_time_setting(time_btn[1], "end")
        
    def verify_auto_message_default_time_setting(self, time_ment_open_btn, ui_check_test_case):
        time_ment_open_btn.click()
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        if ui_check_test_case == "start":
            self.verify_auto_message_update_default_start_time_setting_ui(view_list,btn_list)
            self.change_time_value(view_list)
        elif ui_check_test_case == "end":
            self.verify_auto_message_update_default_end_time_setting_ui(view_list,btn_list)
            self.change_time_value(view_list)
            
        cancle_btn =btn_list[0]
        cancle_btn.click()
        
    def verify_auto_message_update_default_start_time_setting_ui(self,view_list,btn_list):
        default_time_popup_ui_compare_result = self.utils.compare_image("default_start_time_popup.png", view_list[4], "default_start_time_popup.png", "home")
        active_am_ui_compare_result = self.utils.compare_image("active_start_am_setting.png", view_list[5], "active_am_setting.png", "home")
        enabled_pm_ui_compare_result = self.utils.compare_image("enabled_start_pm_setting.png", view_list[6], "enabled_pm_setting.png", "home")
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
        enabled_pm_ui_compare_result = self.utils.compare_image("active_end_pm_setting.png", view_list[6], "active_pm_setting.png", "home")
        popup_cancle_btn_ui_compare_result = self.utils.compare_image("default_end_time_popup_cancle_btn.png", btn_list[0], "default_time_popup_cancle_btn.png", "home")
        popup_save_btn_ui_compare_result = self.utils.compare_image("default_end_time_popup_save_btn.png", btn_list[1], "default_time_popup_save_btn.png", "home")
        
        assert default_time_popup_ui_compare_result, "기본 설정 시간 UI 비교 테스트 실패"
        assert active_am_ui_compare_result, "기본설정 AM 값 UI 비교 테스트 실패"
        assert enabled_pm_ui_compare_result, "기본설정 PM 값 UI 비교 테스트 실패"
        assert popup_cancle_btn_ui_compare_result, "팝업 취소 버튼 UI 비교 테스트 실패"
        assert popup_save_btn_ui_compare_result, "팝업 확인 버튼 UI 비교 테스트 실패"
    
    def change_time_value(self, view_list):
        self.verify_change_time_value(view_list,"start")
        self.verify_change_time_value(view_list,"end")

    def verify_change_time_value(self, view_list, compare_value):
        am_time_setting_btn = view_list[5]
        pm_time_setting_btn =  view_list[6]
        
        if compare_value == "start":
            pm_time_setting_btn.click()
            pm_setting_ui_compare = self.utils.compare_image("enable_am_setting.png", am_time_setting_btn, "enabled_am_setting.png", "home")
            am_setting_ui_compare = self.utils.compare_image("active_pm_setting.png", pm_time_setting_btn, "active_pm_setting.png", "home")
            assert pm_setting_ui_compare, "PM 버튼 클릭 활성화 UI 비교 테스트 실패"
            assert am_setting_ui_compare, "AM 버튼 클릭 비활성화 UI 비교 테스트 실패"
            am_time_setting_btn.click()
            
        elif compare_value == "end":
            am_time_setting_btn.click()
            pm_setting_ui_compare = self.utils.compare_image("active_am_setting.png", am_time_setting_btn, "active_am_setting.png", "home")
            am_setting_ui_compare = self.utils.compare_image("enable_pm_setting.png", pm_time_setting_btn, "enabled_pm_setting.png", "home")
            assert am_setting_ui_compare, "AM 버튼 클릭 활성화 UI 비교 테스트 실패"
            assert pm_setting_ui_compare, "PM 버튼 클릭 비활성화 UI 비교 테스트 실패"
            pm_time_setting_btn.click()
    
    def verify_all_time_setting(self):
        return
    
    def verify_select_update_setting_ui(self):
        return
    
    def long_press_drag_action(self, element):
        x = random.randint(0, 25000)
        y = random.randint(0, 25000)
        
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to(element)  
        actions.w3c_actions.pointer_action.pointer_down() 
        actions.w3c_actions.pointer_action.pause(3) 
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()
    
    def random_time_setting(self,image_list, time_value):
        
        if time_value == "start":
            image_list[0].click()
            view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            min_element = view_list[4]
            self.long_press_drag_action(min_element)
            
            start_update_setting_time = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)[4]
            return_time = self.utils.element_replace(start_update_setting_time.get_attribute("contentDescription"))
        elif time_value == "end":
            image_list[1].click()
            view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
            min_element = view_list[4]
            self.long_press_drag_action(min_element)
            
            end_update_setting_time = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)[4]
            return_time = self.utils.element_replace(end_update_setting_time.get_attribute("contentDescription"))
            
        save_btn = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)[1]
        save_btn.click()
        return return_time[:5]
            
    
    def random_day_select(self, check_list):
        random_index_value = random.choice(range(1,6))
        random_value = sorted(random.sample(range(7), k=random_index_value))
        day_list = []
        
        for item in random_value:
            check_list[item].click()
            match item:
                case 0:
                    day_list.append("월")
                case 1:
                    day_list.append("화")
                case 2:
                    day_list.append("수")
                case 3:
                    day_list.append("목")
                case 4:
                    day_list.append("금")
                case 5:
                    day_list.append("토")
                case 6:
                    day_list.append("일")
                    
        return day_list

    # 동작을 가지고 와서 실제로 모달 팝업 동작에 대한 값 비교 필요    
    def setting_back_modal_control(self, action_value):
        modal_popup = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)[0]
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        self.utils.screenshot_image("setting_update_back_modal.png", modal_popup)
        cancel_btn = btn_list[0]
        save_btn = btn_list[1]
        
        if action_value == "취소":
            cancel_btn.click()
        else:
            save_btn.click()
        
    def set_auto_message_menu_control(self, switch_btn):
        switch_btn.click()

    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "로그아웃 팝업 텍스트 비교 테스트 실패"
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