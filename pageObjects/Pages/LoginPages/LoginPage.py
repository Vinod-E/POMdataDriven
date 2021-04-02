import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait
from Listeners.logger_settings import ui_logger


class Login:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_tenant_name = Locators.LOGIN['alias']
    __e_next_button_css = Locators.LOGIN['next']
    __e_login_name_l = Locators.LOGIN['login_name']
    __e_password_xpath = Locators.LOGIN['password']
    __e_login_button_css = Locators.LOGIN['login']
    __e_anchor_tag = Locators.TAG['anchor']
    __e_logout_id = Locators.LOGIN['logout']
    __e_click_xpath = Locators.LOGIN['click_to_login']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def tenant(self, tenant_name):
        self.wait.web_element_wait_send_keys(By.NAME, self.__e_tenant_name, tenant_name, 'login_tenant_field')

    def next_button(self):
        self.wait.web_element_wait_click(By.CSS_SELECTOR, self.__e_next_button_css, 'login_next_button')

    def login_name(self, login_name):
        try:
            time.sleep(1.5)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_login_name_l, login_name, 'login_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def password(self, password):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_password_xpath, password, 'login_password_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_button(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_login_button_css, 'login_button')
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

    def login_account_click(self, user_name):
        try:
            self.wait.web_elements_wait_click(By.TAG_NAME, self.__e_anchor_tag, user_name)
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_out(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.ID, self.__e_logout_id, 'Logout from account')
            return True
        except Exception as error:
            ui_logger.error(error)

    def click_here_to_login(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.XPATH, self.__e_click_xpath, 'Logout from account')
            return True
        except Exception as error:
            ui_logger.error(error)
