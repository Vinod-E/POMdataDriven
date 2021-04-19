import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait


class CandidateSearchPage:
    __e_embrace_search_xpath = Locators.TITLE['title'].format('AdvancedSearch')
    __e_candidate_name_field_xpath = Locators.EMBRACE['candidate_name_search_field']
    __e_search_button_xpath = Locators.BUTTONS['button'].format(' Search')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def advance_search(self):
        try:
            self.wait.embrace_loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_embrace_search_xpath, 'embrace_advance_search')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_name_field(self, candidate_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_candidate_name_field_xpath, candidate_name,
                                                 'candidate_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def advance_search_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_button_xpath, 'advance_search_button')
            self.wait.embrace_loading()
            return True
        except Exception as error:
            ui_logger.error(error)
