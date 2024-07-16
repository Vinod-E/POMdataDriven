import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class InterviewFeedback:

    __e_provide_select_drop_css = Locators.FEEDBACK['new_form_drop_down']
    __e_provide_comment_xpath = Locators.PLACEHOLDER['all_place_holder'].format('Enter text here')
    __e_provide_overall_xpath = Locators.FEEDBACK['overall']
    __e_decision_button_xpath = Locators.BUTTONS['all_buttons']
    __e_feedback_submit_xpath = Locators.BUTTONS['button'].format('Submit Feedback')
    __e_agree_xpath = Locators.BUTTONS['button'].format('Agree and Submit')
    __e_save_draft_xpath = Locators.BUTTONS['button'].format('Save as Draft')
    __e_update_feedback_xpath = "//button[text()='{}']".format('Update Feedback')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def feedback_select_drop_down(self, value):
        try:
            time.sleep(5)
            self.wait.loading()
            self.wait.web_elements_wait_send_keys(By.XPATH, self.__e_provide_select_drop_css, value)
            print(f'Selected Rating - {value}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_comments(self, comment):
        try:
            time.sleep(0.5)
            self.wait.web_elements_wait_send_keys(By.XPATH, self.__e_provide_comment_xpath, comment)
            print(f'Given Comment - {comment}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_decision(self, decision):
        try:
            self.wait.web_elements_wait_click(By.XPATH, self.__e_decision_button_xpath.format(decision), decision)
            print(f'Selected Decision - {decision}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def overall_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH,
                                                 self.__e_provide_overall_xpath, comment, 'overall_comment')
            print(f'Given Overall Comment - {comment}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_draft_new_feedback(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_draft_xpath, 'submit_feedback_button')
            print('Save Draft - Submitted')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_feedback(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_feedback_submit_xpath, 'submit_feedback_button')
            print('Feedback - Submitted')
            return True
        except Exception as error:
            ui_logger.error(error)

    def agree_and_submit(self):
        try:
            time.sleep(0.7)
            self.wait.web_element_wait_click(By.XPATH, self.__e_agree_xpath, 'feedback_form_validation')
            print('Agree and submit - Submitted')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_draft_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_draft_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

    def update_feedback(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_update_feedback_xpath, 'update_feedback')
            print('Feedback - Updated')
            return True
        except Exception as error:
            ui_logger.error(error)
