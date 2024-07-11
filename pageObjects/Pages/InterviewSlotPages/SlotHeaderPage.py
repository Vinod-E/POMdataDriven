import time
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class CaptchaScreenHeader:
    __e_header_class = 'page-heading'
    __e_next_button_class = 'btn-captcha-validation'

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def interview_slot_app_header(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_text(By.CLASS_NAME, self.__e_header_class,
                                            'interview_slot_app_header')
            print('Slot App Name:: ', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)

    def next_button(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_next_button_class,
                                             'next_button')
            time.sleep(1)
            self.wait.refresh_page()
            return True
        except Exception as error:
            ui_logger.error(error)
