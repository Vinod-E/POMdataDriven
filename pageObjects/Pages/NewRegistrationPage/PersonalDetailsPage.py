from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class PersonalDetailsData:

    __e_p_d_xpath = Locators.PLACEHOLDER['text_ph']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def full_name(self, full_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('Full Name'),
                                                 full_name, 'full_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def email_id(self, email):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('Email Id'),
                                                 email, 'email_id')
            return True
        except Exception as error:
            ui_logger.error(error)

    def mobile_number(self, mobile_number):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('MobileNumber'),
                                                 mobile_number, 'mobile_number')
            return True
        except Exception as error:
            ui_logger.error(error)
