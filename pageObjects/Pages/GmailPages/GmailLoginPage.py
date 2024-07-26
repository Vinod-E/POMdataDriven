import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class LoginPageGmail:

    __e_email_field_id = 'identifierId'
    __e_email_next_css = '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe'
    __e_password_name = 'Passwd'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def email_field(self, email):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_email_field_id, email,
                                                 'email_field')
            print('------->> Google Email Id Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def next_button(self):
        try:
            self.wait.web_element_wait_click(By.CSS_SELECTOR, self.__e_email_next_css, 'next_button')
            print('Google Email Next button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def password_field(self, password):
        try:

            self.wait.web_element_wait_send_keys(By.NAME, self.__e_password_name, password,
                                                 'password_field')
            print('------->> Google Email Password Entered')
            return True
        except Exception as error:
            ui_logger.error(error)
