import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By

from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class CandidateSubTabs:
    __e_event_config_xpath = Locators.SUB_MENU['configurations']
    __e_event_can_applications_xpath = Locators.SUB_MENU['candidate_applications']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def can_application_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_can_applications_xpath,
                                             'can_application_tab')
            time.sleep(0.5)
            print('candidate Applications Tab - Landed')
            return True
        except Exception as error:
            ui_logger.error(error)
