import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class CandidateDetailsPage:
    __e_title_xpath = Locators.TITLE['title']
    __e_id_xpath = Locators.CANDIDATE['id']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

        self.candidate_id = ''

    def candidate_status(self, changed_status):
        try:
            time.sleep(2)
            self.wait.loading()
            self.wait.web_element_wait_text(By.XPATH, self.__e_title_xpath.format(changed_status),
                                            f'Candidate_status_{changed_status}')
            if self.wait.text_value == changed_status:
                print(f'Candidate status changed - {self.wait.text_value}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_id_copy(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_id_xpath, 'candidate_id')
            self.candidate_id = self.wait.text_value
            print(f'candidate id - {self.candidate_id}')
            return True
        except Exception as error:
            ui_logger.error(error)
