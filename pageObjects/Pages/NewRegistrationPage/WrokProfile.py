from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class WorkProfileDetailsData:

    __e_add_profile_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'addProfile', "'")
    __e_company_xpath = '(//select[@ng-model="profile.company.value"])[{}]'
    __e_sector_xpath = '(//select[@ng-model="profile.sector.value"])[{}]'
    __e_designation_xpath = '(//select[@ng-model="profile.designation.value"])[{}]'
    __e_from_month_xpath = '(//select[@ng-model="profile.fromMonth.value"])[{}]'
    __e_to_month_xpath = '(//select[@ng-model="profile.toMonth.value"])[{}]'
    __e_from_year_xpath = '(//select[@ng-model="profile.fromYear.value"])[{}]'
    __e_to_year_xpath = '(//select[@ng-model="profile.toYear.value"])[{}]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def add_more_profile(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_add_profile_xpath, 'add_more_profile')
            return True
        except Exception as error:
            ui_logger.error(error)

    def company(self, company, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_company_xpath.format(wp), company, 'company')
            return True
        except Exception as error:
            ui_logger.error(error)

    def sector(self, sector, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_sector_xpath.format(wp), sector, 'sector')
            return True
        except Exception as error:
            ui_logger.error(error)

    def designation(self, design, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_designation_xpath.format(wp), design, 'designation')
            return True
        except Exception as error:
            ui_logger.error(error)

    def from_month(self, from_month, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_from_month_xpath.format(wp),
                                                 from_month, 'from_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def to_month(self, to_month, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_to_month_xpath.format(wp),
                                                 to_month, 'to_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def from_year(self, from_year, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_from_year_xpath.format(wp),
                                                 from_year, 'from_year')
            return True
        except Exception as error:
            ui_logger.error(error)

    def to_year(self, to_year, wp):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_to_year_xpath.format(wp),
                                                 to_year, 'to_year')
            return True
        except Exception as error:
            ui_logger.error(error)
