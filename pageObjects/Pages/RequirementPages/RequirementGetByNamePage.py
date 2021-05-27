from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class RequirementGetByName:

    __e_name_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def req_name_click(self, req_name):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_name_xpath.format(req_name), 'req_name_click')
            print('Requirement name - Clicked to open details screen')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def req_name_validation(self, req_name):
        try:
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_name_xpath.format(req_name),
                                            'req_name_validation')
            print('Event Name -', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)
