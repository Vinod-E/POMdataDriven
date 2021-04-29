import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class SelectionProcessPage:
    __e_job_sp_xpath = Locators.PLACEHOLDER['place_holder'].format('Selection Process')
    __e_job_sp_save_xpath = Locators.BUTTONS['button'].format('Save')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def job_sp(self, selection_process):
        try:
            time.sleep(2)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_sp_xpath,
                                                 selection_process, 'Send_Selection_Process')
            self.wait.drop_down_selection()
            print(f'selected - {selection_process} selection process')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_sp_save(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_sp_save_xpath, 'Saved_Selection_Process')
            print('saved - selection process')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_sp_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

    def page_refresh(self):
        try:
            self.wait.refresh_page()
            print('Page - Refreshed')
            self.wait.loading()
            time.sleep(2)
            return True
        except Exception as error:
            ui_logger.error(error)
