import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class CandidateQueryReplyPage:
    __e_search_xpath = Locators.PLACEHOLDER['place_holder'].format('Find')
    __e_subject_xpath = Locators.TITLE['title']
    __e_reply_message_xpath = Locators.PLACEHOLDER['all_place_holder'].format('Your message here...')
    __e_mark_close_xpath = Locators.BUTTONS['button'].format('Mark as Closed')
    __e_ok_xpath = Locators.BUTTONS['button'].format('OK')
    __e_reply_button_xpath = Locators.TITLE['title'].format('Reply')
    __e_status_bucket_xpath = Locators.QUERY['status_bucket']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def search_candidate_query(self, candidate_name):
        try:
            self.wait.embrace_loading()
            self.wait.clear(By.XPATH, self.__e_search_xpath, 'more_queries')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_search_xpath, candidate_name,
                                                 'more_queries')
            print('Searching for proper record')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_proper_query_based_on_subject(self, subject):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_subject_xpath.format(subject),
                                             'select_proper_query_based_on_subject')
            self.wait.embrace_loading()
            print('Proper block based on proper subject - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def reply_message_entry(self, message):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_reply_message_xpath, message,
                                                 'reply_message_entry')
            print('reply_message_entry - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def reply_to_query(self):
        try:
            self.wait.web_element_wait_click(By.XPATH,self.__e_reply_button_xpath, 'reply_to_query')
            print('reply_to_query - Clicked')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def in_progress_tab(self):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_status_bucket_xpath, 'In Progress',
                                                 'in_progress_tab')
            self.wait.embrace_loading()
            print('in_progress_tab - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def mark_as_closed(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_mark_close_xpath, 'mark_as_closed')
            print('mark_as_closed - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ok_xpath, 'confirm_button')
            print('confirm_button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
