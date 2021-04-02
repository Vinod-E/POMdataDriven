from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class EventSubTabs:
    __e_event_config_xpath = Locators.EVENT['configurations']
    __e_event_owners_xpath = Locators.EVENT['owners']
    __e_manage_candidates = Locators.BUTTONS['all_buttons'].format('Manage Candidates')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def event_configurations(self):
        self.wait.web_element_wait_click(By.XPATH, self.__e_event_config_xpath, 'Event_configurations_tab')

    def event_owners(self):
        self.wait.web_element_wait_click(By.XPATH, self.__e_event_owners_xpath, 'Event_owners_tab')

    def manage_candidates(self):
        self.wait.web_element_wait_click(By.XPATH, self.__e_manage_candidates, 'Manage_Candidates')
