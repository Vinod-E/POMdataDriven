import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.BrowserBackwardForward import ForwardBackward


class EventCancelRequest:
    __e_approve_xpath = Locators.TITLE['title'].format('Approve Request')
    __e_approve_tool_xpath = Locators.TITLE['tooltip'].format("'", 'Approve Request', "'")
    __e_comment_xpath = Locators.EVENT['comment_cancel_request']
    __e_confirm_xpath = Locators.BUTTONS['all_buttons'].format('OK')
    __e_ahead_xpath = Locators.BUTTONS['all_buttons'].format('GO AHED')
    __e_notifier = Locators.NOTIFIER['message']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.for_back = ForwardBackward(self.driver)

    def accept_cancellation(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_approve_xpath, 'accept_cancellation')
            print('Approved - Cancel request from interviewer')
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_request_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_comment_xpath, comment, 'cancel_request_comment')
            print(f'Entered - {comment}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_request(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_confirm_xpath, 'confirm_request')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def go_ahead_with_lobby_screen(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ahead_xpath, 'go_ahead_with_lobby_screen')
            print('Continue with Lobby -Screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def lobby_confirm_request(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ahead_xpath, 'go_ahead_with_lobby_screen')
            print('Confirm Lobby - Cancel request by administrator')
            return True
        except Exception as error:
            ui_logger.error(error)

    def lobby_accept_cancellation(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_approve_xpath, 'accept_cancellation')
            print('Approved - Cancel request from interviewer')
            return True
        except Exception as error:
            ui_logger.error(error)

    def acceptance_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def acceptance_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(1)
            self.for_back.browser_backward()
            self.wait.loading()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
