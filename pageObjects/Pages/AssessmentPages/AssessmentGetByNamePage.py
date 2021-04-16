import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class AssessmentGetByName:

    __e_test_name_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def test_name_click(self, test_name):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_test_name_xpath.format(test_name),
                                             'test_name_click')
            print(f'Clicked on - {test_name}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def assessment_name_validation(self, assessment_name):
        try:
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_test_name_xpath.format(assessment_name),
                                            'Assessment_name_validation')
            print(f'Assessment Name - {self.wait.text_value}')
            self.wait.loading()
            time.sleep(0.3)
            return True
        except Exception as error:
            ui_logger.error(error)
