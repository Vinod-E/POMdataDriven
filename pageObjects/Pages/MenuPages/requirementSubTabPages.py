from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll


class RequirementSubTabs:
    __e_req_config_xpath = Locators.SUB_MENU['req_configurations']
    __e_req_duplicity_xpath = Locators.SUB_MENU['req_duplicity']
    __e_req_query_xpath = Locators.SUB_MENU['req_query']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def requirement_configurations(self):
        try:
            self.scroll.up(0, 50)
            self.wait.web_element_wait_click(By.XPATH, self.__e_req_config_xpath, 'job_configuration_tab')
            print('Job Configuration Tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_duplicity(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_req_duplicity_xpath, 'requirement_duplicity')
            print('Requirement Duplicity check - On')
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_query(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_req_query_xpath, 'requirement_query')
            print('Requirement Query Configuration tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
