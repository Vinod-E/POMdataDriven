import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class ChangeStatus:

    __e_stage_field_xpath = Locators.CHANGE_STATUS['stage']
    __e_status_field_xpath = Locators.CHANGE_STATUS['status']
    __e_comment_xpath = Locators.CHANGE_STATUS['comment']
    __e_button_xpath = Locators.BUTTONS['button'].format('Change')
    __e_select_int_xpath = Locators.TITLE['title'].format('Select Interviewers')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def applicant_stage(self, stage):
        try:
            time.sleep(2)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_stage_field_xpath, stage,
                                                 'Applicant_stage_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def applicant_status(self, status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_status_field_xpath, status,
                                                 'Applicant_status_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_int_xpath, 'select_interviewers')
            print('Select Interviewers - Selected')
            time.sleep(2)
            return True
        except Exception as error:
            ui_logger.error(error)

    def comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_comment_xpath, comment,
                                                 'Applicant_comment_box')
            return True
        except Exception as error:
            ui_logger.error(error)

    def change_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_button_xpath, 'Change_Button')
            print('MassInterview applicant status - Changed')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def change_status_notifier(self, message):
        try:
            time.sleep(1)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def change_status_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            self.wait.loading()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
