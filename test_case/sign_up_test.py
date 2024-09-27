from utils.utils import Utils
from config.selectors import Selectors

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
        self.test_description_check()
 
    def test_description_check(self):
        # view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        # image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        # edit_list = self.utils.get_all_elements(self.selectors.EDIT_CLASS_NAME)
        # btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        self.utils.scroll_action(self.selectors.VIEW_CLASS_NAME, "선택")
        