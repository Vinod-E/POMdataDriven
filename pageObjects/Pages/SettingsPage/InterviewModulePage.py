import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll
from utilities.uiNotifier import Notifier


class InterviewModulePage:
    __e_interview_module_xpath = Locators.TITLE['title'].format('Interview Module')
    __e_new_form_xpath = Locators.ACCOUNT['new_form']
    __e_click_radio_css = Locators.BUTTONS['radio']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def interview_module(self):
        try:
            self.scroll.down(0, -100)
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_interview_module_xpath, 'interview_module')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def new_form_setting(self):
        try:
            self.scroll.down(0, -100)
            self.wait.web_element_wait_click(By.XPATH, self.__e_new_form_xpath, 'new_form_setting')
            return True
        except Exception as error:
            ui_logger.error(error)

    def enable_new_form(self):
        try:
            time.sleep(1)
            self.wait.web_elements_wait_multiple_click(By.CSS_SELECTOR, self.__e_click_radio_css, 'On')
            return True
        except Exception as error:
            ui_logger.error(error)

    def disable_new_form(self):
        try:
            time.sleep(1)
            self.wait.web_elements_wait_multiple_click(By.CSS_SELECTOR, self.__e_click_radio_css, 'Off')
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
