import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose
from utilities.PageScroll import PageScroll


class WorkProfileDetailsPage:
    __e_company_wf1_xpath = Locators.MICROSITE['Wf1_company']
    __e_company_wf2_xpath = Locators.MICROSITE['Wf2_company']
    __e_wf1_design_xpath = Locators.MICROSITE['wf1_designation']
    __e_wf2_design_xpath = Locators.MICROSITE['wf2_designation']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)
        self.scroll = PageScroll(self.driver)

    def wp1_company_verified(self, company):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH, self.__e_company_wf1_xpath, 'wf1_verified')
            if company in self.wait.text_value.strip():
                print(f'Work Profile Company 1 - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def wp2_company_verified(self, company):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_company_wf2_xpath, 'wf2_verified')
            if company in self.wait.text_value.strip():
                print(f'Work Profile Company 2 - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def wp1_design_verified(self, design):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_wf1_design_xpath, 'wf1_design_verified')
            if design in self.wait.text_value.strip():
                print(f'Work Profile Designation 1 - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def wp2_design_verified(self, design):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_wf2_design_xpath, 'wf2_design_verified')
            if design in self.wait.text_value.strip():
                print(f'Work Profile Designation 2 - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)
