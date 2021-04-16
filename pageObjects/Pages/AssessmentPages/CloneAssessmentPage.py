import time
from pageObjects import Locators
from utilities.uiNotifier import Notifier
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class CloneAssessmentPage:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_new_test_field_name = Locators.SEARCH['test_name']
    __e_test_from_date_xpath = Locators.PLACEHOLDER['place_holder'].format('From')
    __e_test_to_date_xpath = Locators.PLACEHOLDER['place_holder'].format('To')
    __e_clone_button_xpath = Locators.BUTTONS['button'].format('Clone')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def new_test_name(self, new_test_name):
        try:
            time.sleep(0.7)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_new_test_field_name, new_test_name,
                                                 'new_test_name')
            print(f'New test name {new_test_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_from_date(self, from_date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_test_from_date_xpath, from_date,
                                                 'new_test_name')
            print(f'New test from {from_date} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_to_date(self, to_date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_test_to_date_xpath, to_date,
                                                 'new_test_name')
            print(f'New test from {to_date} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def clone_test_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_clone_button_xpath, 'requirement_name')
            print('Clone Assessment Button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def clone_assessment_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def clone_assessment_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
