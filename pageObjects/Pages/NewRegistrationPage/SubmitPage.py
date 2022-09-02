import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class SubmitData:

    __e_check_box_xpath = Locators.CHECK_BOX['check_box']
    __e_submit_xpath = Locators.BUTTONS['button'].format('Submit')
    __e_confirm_xpath = Locators.BUTTONS['button'].format('Confirm & Submit')
    __e_header_tag = Locators.TAG['h2']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def job_selection(self):
        try:
            self.wait.web_elements_wait_multiple_click(By.XPATH, self.__e_check_box_xpath, '')
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_registration(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_submit_xpath, 'submit_registration')
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_registration(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_confirm_xpath, 'confirm_registration')
            time.sleep(2)
            return True
        except Exception as error:
            ui_logger.error(error)

    def registration_successful(self, message):
        try:
            self.wait.loading()
            self.wait.web_element_wait_text(By.TAG_NAME, self.__e_header_tag, 'registration_successful')
            if self.wait.text_value.strip() == message:
                print(f'***--------->>> {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)
