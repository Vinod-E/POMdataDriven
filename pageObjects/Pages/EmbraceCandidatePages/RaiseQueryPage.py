import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class CandidateQueryPage:
    __e_more_queries_xpath = Locators.QUERY['more_queries']
    __e_category_xpath = Locators.QUERY['category_select']
    __e_subject_name = Locators.QUERY['subject_field']
    __e_message_xpath = Locators.QUERY['message_field']
    __e_raise_button_xpath = Locators.BUTTONS['button'].format('Raise Query')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def more_queries_button(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_more_queries_xpath, 'more_queries')
            print('Clicked - on More queries button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def category_select(self, category):
        try:
            time.sleep(1)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_category_xpath, category,
                                                 'category_select')
            print('category_select - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def subject_entry(self, subject):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_subject_name, subject,
                                                 'subject_entry')
            print('subject_entry - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def message_entry(self, message):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_message_xpath, message,
                                                 'message_entry')
            print('message_entry - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def query_raise_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_raise_button_xpath, 'query_raise_button')
            print('query_raise_button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def query_raise_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def query_raise_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)
