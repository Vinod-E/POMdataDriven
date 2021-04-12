from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class JobSubTabs:
    __e_job_config_xpath = Locators.SUB_MENU['job_configurations']
    __e_job_automations_xpath = Locators.SUB_MENU['automations']
    __e_job_owners_xpath = Locators.SUB_MENU['job_owners']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def job_configurations(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_config_xpath, 'job_configuration_tab')
            print('Job Configuration Tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_automation(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_automations_xpath, 'Job_Automations_tab')
            print('Job Automations Tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_owners(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_owners_xpath, 'job_owners')
            print('Job Owners Tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
