import time

from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.appTitle import Title
from utilities.SwitchWindow import SwitchWindowClose


class JobGetByName:

    __e_job_name_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Title(self.driver)
        self.window = SwitchWindowClose(self.driver)

    def job_tab_title(self, tab_title):
        try:
            self.tab.tab_title(tab_title)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_name_click(self, job_name):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_name_xpath.format(job_name), 'job_name_click')
            time.sleep(0.5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1.5)
            self.wait.loading()

            return True
        except Exception as error:
            ui_logger.error(error)

    def job_name_validation(self, job_name):
        try:
            self.wait.loading()
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_job_name_xpath.format(job_name),
                                            'Job_name_validation')
            print('Job Name -', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)
