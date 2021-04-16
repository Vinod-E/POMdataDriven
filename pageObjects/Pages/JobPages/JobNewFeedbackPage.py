import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class NewFeedbackConfigPage:
    __e_new_form_stage_xpath = Locators.PLACEHOLDER['text_ph'].format('Interview Stages')
    __e_new_form_field_xpath = Locators.PLACEHOLDER['text_ph'].format('Name like.')
    __e_new_form_search_css = Locators.BUTTONS['new_form_search']
    __e_new_use_form_xpath = Locators.BUTTONS['all_buttons'].format('Use')
    __e_new_for_edit_xpath = Locators.TITLE['title'].format('Edit Confiiguration')
    __e_overall_mandatory_xpath = Locators.JOB['feedback_overall_mandatory']
    __e_reject_overall_xpath = Locators.JOB['reject_overall_mandatory']
    __e_update_form_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'update', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def stage_selection(self, stage):
        try:
            time.sleep(1.5)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_new_form_stage_xpath, stage,
                                                 'Send_Selection_Process')
            self.wait.drop_down_selection()
            print(f'selected - New - {stage}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def form_search_filed_enter(self, form):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_new_form_field_xpath, form, 'form_search')
            print(f'Entered - New {form}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def form_search(self):
        try:
            self.wait.web_element_wait_click(By.CSS_SELECTOR, self.__e_new_form_search_css, 'form_search')
            print('Feedback Form - Search')
            return True
        except Exception as error:
            ui_logger.error(error)

    def use_form(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_new_use_form_xpath, 'use_form')
            print('Feedback Form - Use')
            return True
        except Exception as error:
            ui_logger.error(error)

    def edit_form(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_new_for_edit_xpath, 'edit_form')
            print('Feedback Form - Edit')
            return True
        except Exception as error:
            ui_logger.error(error)

    def overall_mandatory(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_overall_mandatory_xpath, 'overall_mandatory')
            print('Overall feedback mandatory - On')
            return True
        except Exception as error:
            ui_logger.error(error)

    def reject_overall_mandatory(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_reject_overall_xpath, 'reject_overall_mandatory')
            print('Reject Overall feedback mandatory - On')
            return True
        except Exception as error:
            ui_logger.error(error)

    def update_feedback_form(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_update_form_xpath, 'update_feedback_form')
            print('Feedback Form - Save')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_new_form_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_new_form_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
