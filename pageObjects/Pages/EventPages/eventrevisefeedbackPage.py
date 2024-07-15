import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class EventReviseFeedbackPage:

    __e_revise_comment_xpath = '//textarea[@ng-model="vm.data.comments"]'
    __e_revise_button_xpath = '//button[@ng-click="vm.actionClicked({}{}{})"]'.format("'", 'revise', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.message = Notifier(self.driver)

    def revise_comment(self, comment):
        try:
            time.sleep(1)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_revise_comment_xpath, comment,
                                                 'revise_comment')
            return True
        except Exception as error:
            ui_logger.error(error)

    def revise_submit_button(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_revise_button_xpath, 'revise_submit_button')
            return True
        except Exception as error:
            ui_logger.error(error)
