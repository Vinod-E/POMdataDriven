import time

from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll


class AccountName:
    __e_account_name_settings_xpath = Locators.ACCOUNT['account_icon']
    __e_settings_id = Locators.ACCOUNT['settings']
    __e_anchor_tag = Locators.TAG['anchor']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def account_name_click(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_account_name_settings_xpath, 'account_name_click')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_account_name_verification(self, user_name):
        try:
            self.wait.loading()
            assert self.wait.web_elements_wait_text(By.TAG_NAME, self.__e_anchor_tag, user_name) == user_name, \
                'Logged in different account please check the details'
            return True
        except Exception as error:
            ui_logger.error(error)

    def account_settings(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_settings_id, 'account_settings')
            return True
        except Exception as error:
            ui_logger.error(error)
