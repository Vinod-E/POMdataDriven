import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class EventApplicant:

    __e_applicant_check_name = Locators.CHECKBOX['check']
    __e_status_change_id = Locators.ACTIONS['status_change']
    __e_applicant_name_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.message = Notifier(self.driver)

    def select_applicant(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.NAME, self.__e_applicant_check_name, 'Applicant_check_box')
            return True
        except Exception as error:
            ui_logger.error(error)

    def change_status_action(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_status_change_id, 'Applicant_status_change')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def applicant_get_name(self, applicant_name, message):
        try:
            time.sleep(2)
            self.message.glowing_messages(message)
            self.message.dismiss_message()
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_applicant_name_xpath.format(applicant_name),
                                             'Applicant_Get_By_Name')
            print('Clicked on applicant name')
            return True
        except Exception as error:
            ui_logger.error(error)
