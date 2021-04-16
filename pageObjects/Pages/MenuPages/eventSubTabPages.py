import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By

from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class EventSubTabs:
    __e_event_config_xpath = Locators.SUB_MENU['configurations']
    __e_event_owners_xpath = Locators.SUB_MENU['owners']
    __e_manage_candidates = Locators.BUTTONS['all_buttons'].format('Manage Candidates')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def event_configurations(self):
        try:
            self.scroll.up(0, -100)
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_config_xpath, 'Event_configurations_tab')
            time.sleep(0.5)
            print('Event Configurations Tab - Landed')
            self.scroll.up(0, 200)
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_owners(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_owners_xpath, 'Event_owners_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def manage_candidates(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_manage_candidates, 'Manage_Candidates')
            return True
        except Exception as error:
            ui_logger.error(error)
