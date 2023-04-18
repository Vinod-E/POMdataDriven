import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose
from utilities.PageScroll import PageScroll


class CustomValuesDetailsPage:
    __e_text_xpath = '(//span[@title="{}"])[{}]'
    __e_textarea_xpath = '(//span[@title="{}"])[{}]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)
        self.scroll = PageScroll(self.driver)

    def text_value_verified(self, value, position):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH, self.__e_text_xpath.format(position), 'text_value_verified')
            if value in self.wait.text_value.strip():
                print(f'Custom Text Property - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def textarea_value_verified(self, value, position):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH, self.__e_textarea_xpath.format(position),
                                            'textarea_value_verified')
            if value in self.wait.text_value.strip():
                print(f'Custom TextArea Property - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)
