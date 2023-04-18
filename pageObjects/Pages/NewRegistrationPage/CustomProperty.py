import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class CustomPropertyData:
    __e_text_id = 'text{}'
    __e_textarea_xpath = '//textarea[@placeholder="TextArea{}"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def text_field(self, text_value, text_field_id):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_text_id.format(text_field_id),
                                                 text_value, 'text_field')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def textarea_field(self, textarea_value, textarea_field_id):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_textarea_xpath.format(textarea_field_id),
                                                 textarea_value, 'textarea_field')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
