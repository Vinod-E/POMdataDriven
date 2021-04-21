import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class CandidatePage:
    __e_task_behalf_of_xpath = Locators.TITLE['title'].format('Submit Tasks on Behalf of Candidate')
    __e_acceptance_name = Locators.EMBRACE['candidate_acceptance_yes']
    __e_submit_xpath = Locators.BUTTONS['button'].format('Submit')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def behalf_of_submit_task(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_task_behalf_of_xpath, 'behalf_of_submit_task')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_acceptance_yes(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.NAME, self.__e_acceptance_name, 'candidate_acceptance_yes')
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_task(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_submit_xpath, 'submit_task')
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_task_notifier(self, message):
        try:
            self.wait.embrace_loading()
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_task_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
