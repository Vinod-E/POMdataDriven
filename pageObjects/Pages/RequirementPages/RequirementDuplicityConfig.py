from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class DuplicityCheck:

    __e_click_radio_css = Locators.BUTTONS['radio']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def do_not_allow_duplicates(self, button_name):
        try:
            self.wait.web_elements_wait_click(By.CSS_SELECTOR, self.__e_click_radio_css, button_name)
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def req_duplicity_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def req_duplicity_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

