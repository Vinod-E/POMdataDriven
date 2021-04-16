import time
from selenium.webdriver.common.by import By
from pageObjects import Locators
from Listeners.logger_settings import ui_logger
from utilities.SwitchWindow import SwitchWindowClose
from utilities.WebDriver_Wait import WebElementWait


class ManageTaskScreen:
    __e_common_css = '.ng-binding'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)

    def __common(self, value):
        try:
            if self.wait.web_elements_wait_text(By.CSS_SELECTOR, self.__e_common_css, value) == value:
                print(f'Manage Screen Validate with - {value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_name_validate(self, candidate_name):
        self.wait.loading()
        self.__common(candidate_name)

    def candidate_stage_status_validate(self, stage_status):
        self.__common(stage_status)

    def submitted_task_validate(self, submit_task):
        self.__common(submit_task)

    def pending_task_validate(self, pending_task):
        self.__common(pending_task)

    def rejected_task_validate(self, rejected_task):
        self.__common(rejected_task)

    def approved_task_validate(self, approved_task):
        self.__common(approved_task)

    def total_task_validate(self, total_task):
        self.__common(total_task)

        time.sleep(1)
        self.window.window_close()
        time.sleep(1)
        self.window.switch_to_window(1)
        time.sleep(1)
        self.window.window_close()
        time.sleep(1)
        self.window.switch_to_window(0)
