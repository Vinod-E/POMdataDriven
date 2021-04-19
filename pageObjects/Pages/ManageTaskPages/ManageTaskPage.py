import time
from selenium.webdriver.common.by import By
from pageObjects import Locators
from Listeners.logger_settings import ui_logger
from utilities.SwitchWindow import SwitchWindowClose
from utilities.WebDriver_Wait import WebElementWait


class ManageTaskScreen:
    __e_common_css = Locators.MANAGE_TASK['common_label']
    __e_candidate_status_xpath = Locators.MANAGE_TASK['candidate_status']

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
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, submit_task)
            if value == submit_task:
                print(f'Submitted tasks are - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def pending_task_validate(self, pending_task):
        try:
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, pending_task)
            if value == pending_task:
                print(f'Pending tasks are - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def rejected_task_validate(self, rejected_task):
        try:
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, rejected_task)
            if value == rejected_task:
                print(f'Rejected tasks are - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def approved_task_validate(self, approved_task):
        try:
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, approved_task)
            if value == approved_task:
                print(f'Approved tasks are - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def total_task_validate(self, total_task):
        try:
            value = self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, total_task)
            if value == total_task:
                print(f'Total tasks are - {value}')
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
