import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class CandidateQueryPage:
    __e_more_queries_xpath = Locators.QUERY['more_queries']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def more_queries_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_more_queries_xpath, 'more_queries')
            print('Clicked - on More queries button')
            return True
        except Exception as error:
            ui_logger.error(error)
