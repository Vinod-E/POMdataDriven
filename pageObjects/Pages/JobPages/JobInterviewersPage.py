import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class TagInterviewersPage:
    __e_job_interviewers_xpath = Locators.JOB['int_panel']
    __e_job_int_add_class = Locators.JOB['panel_int_add']
    __e_job_int_save_xpath = Locators.BUTTONS['button'].format('Save')
    __e_job_tag_total_int_css = Locators.JOB['total_owners']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def job_int_panel(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_interviewers_xpath,
                                                 value, 'job_int_panel')
            print(f'{value} - Selected from job interviewers panel')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_int_add(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_job_int_add_class, 'job_int_add')
            print('saved - selection process')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_int_save(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_int_save_xpath, 'job_int_save')
            print('saved - job interviewers')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_tag_int_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_tag_int_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

    def total_tag_interviewers(self, number_of_tag_ints):
        try:
            self.wait.loading()
            self.wait.web_element_wait_text(By.CSS_SELECTOR, self.__e_job_tag_total_int_css, 'total_tag_interviewers')
            if str(number_of_tag_ints) in self.wait.text_value:
                print(f'Total tagged Interviewers - {number_of_tag_ints}')
                return True
        except Exception as error:
            ui_logger.error(error)
