import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class Actions:
    __e_job_actions_xpath = Locators.ACTIONS['actions_click']
    __e_job_tag_sp_id = Locators.ACTIONS['selection_process']

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def job_actions_click(self):
        try:
            self.wait.loading()
            self.scroll.up(0, 100)
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_actions_xpath, 'Job_actions_click')
            print('Job Actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def tag_selection_process(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_job_tag_sp_id, 'tag_selection_process')
            self.wait.loading()
            print('Selection Process action - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
