import time
from selenium.webdriver.common.by import By
from pageObjects import Locators
from Listeners.logger_settings import ui_logger
from utilities.SwitchWindow import SwitchWindowClose
from utilities.WebDriver_Wait import WebElementWait


class ManageTaskScreen:
    __e_common_css = Locators.MANAGE_TASK['common_label']
    __e_candidate_status_xpath = Locators.MANAGE_TASK['candidate_status']
    __e_submit_xpath = Locators.TITLE['tooltip'].format("'", 'Candidate has submitted but not approved.', "'")
    __e_pending_xpath = Locators.TITLE['tooltip'].format("'", 'Candidate has not submitted.', "'")
    __e_reject_xpath = Locators.TITLE['tooltip'].format("'", 'Candidate has not corrected the details after the '
                                                             'task(s) got rejected.', "'")
    __e_approved_xpath = Locators.TITLE['tooltip'].format("'", 'Task(s) are approved.', "'")
    __e_total_xpath = Locators.MANAGE_TASK['total']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)

    def candidate_name_validate(self, candidate_name):
        try:
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, candidate_name)
            if candidate_name in value:
                print(f'Candidate Name is - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_stage_status_validate(self, stage_status):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_candidate_status_xpath, stage_status)
            if self.wait.text_value.strip() == stage_status:
                print(f'Manage candidate screen verified - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def submitted_task_validate(self, submit_task):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_submit_xpath, 'submitted_task_validate')
            if self.wait.text_value == submit_task:
                print(f'Submitted tasks are - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def pending_task_validate(self, pending_task):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_pending_xpath, 'pending_task_validate')
            if self.wait.text_value == pending_task:
                print(f'Pending tasks are - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def rejected_task_validate(self, rejected_task):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_reject_xpath, 'rejected_task_validate')
            if self.wait.text_value == rejected_task:
                print(f'Rejected tasks are - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def approved_task_validate(self, approved_task):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_approved_xpath, 'approved_task_validate')
            if self.wait.text_value == approved_task:
                print(f'Approved tasks are - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def total_task_validate(self, total_task):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_total_xpath, 'total_task_validate')
            if self.wait.text_value == total_task:
                print(f'Total tasks are - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def switch_back_to_old_window(self):
        try:
            self.window.window_close()
            time.sleep(0.5)
            self.window.switch_to_window(1)
            time.sleep(0.5)
            self.window.window_close()
            time.sleep(0.5)
            self.window.switch_to_window(0)
            return True
        except Exception as error:
            ui_logger.error(error)
