import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class Actions:
    __e_job_actions_xpath = Locators.ACTIONS['actions_click']
    __e_job_tag_sp_id = Locators.ACTIONS['selection_process']
    __e_job_feed_id = Locators.ACTIONS['feedback_form']
    __e_job_int_id = Locators.ACTIONS['tag_interviewers']

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

    def job_feedback_form(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_job_feed_id, 'job_feedback_form')
            self.wait.loading()
            print('Configured Feedback Form - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_tag_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_job_int_id, 'job_tag_interviewers')
            print('Tag Interviewers to Job - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
