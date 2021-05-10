import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class UnlockFeedback:

    __e_select_int_xpath = Locators.CHECKBOX['all']
    __e_unlock_btn_xpath = Locators.BUTTONS['actionClicked'].format("'", 'unlockFeedback', "'")
    __e_unlock_comment_xpath = Locators.EVENT['comment_cancel_request']
    __e_ok_button_xpath = Locators.BUTTONS['all_buttons'].format('OK')
    __e_close_button_xpath = Locators.BUTTONS['button'].format('Close')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def select_all_interviewers(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_int_xpath, 'select_all_interviewers')
            print('Selection Interviewer for - Unlock')
            return True
        except Exception as error:
            ui_logger.error(error)

    def unlock_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_unlock_btn_xpath, 'unlock_button')
            print('Unlocking button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def unlock_request_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_unlock_comment_xpath, comment,
                                                 'unlock_request_comment')
            print('Enter the comment for Unlock request')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ok_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ok_button_xpath, 'ok_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def close_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_close_button_xpath, 'close_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def unlock_status_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def unlock_status_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
