import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class CancelInterview:

    __e_select_reason_xpath = Locators.PLACEHOLDER['place_holder'].format('Reason')
    __e_reason_comment_xpath = Locators.PLACEHOLDER['all_place_holder'].format('Please provide the '
                                                                               'reason for cancellation')
    __e_save_reason_xpath = Locators.BUTTONS['button'].format('Save')
    __e_confirm_button_xpath = Locators.BUTTONS['button'].format('Confirm')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def cancel_interview_request_reason(self, reason):
        try:
            time.sleep(1.5)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_select_reason_xpath, reason,
                                                 'cancel_interview_request')
            self.wait.drop_down_selection()
            print(f'Reason selected - {reason}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_interview_request_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_reason_comment_xpath, comment,
                                                 'cancel_interview_request')
            print('Enter the comment for cancel request')
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_interview_request_save(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_reason_xpath, 'cancel_interview_request_save')
            print('Cancel Request - Save')
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_interview_request_confirm(self):
        try:
            time.sleep(5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_confirm_button_xpath,
                                             'cancel_interview_request_confirm')
            print('Cancel Interview - Confirm')
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
