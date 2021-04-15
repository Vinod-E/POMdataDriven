import time

from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class EventTestConfigPage:
    __e_event_test_config_btn_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'configure', "'")
    __e_job_name_xpath = Locators.PLACEHOLDER['text_ph'].format('Job Role')
    __e_stage_xpath = Locators.PLACEHOLDER['text_ph'].format('Stage')
    __e_test_xpath = Locators.PLACEHOLDER['text_ph'].format('Test')
    __e_test_active_css = Locators.BUTTONS['radio']
    __e_test_save_xpath = Locators.BUTTONS['button'].format('Save')
    __e_test_config_cancel_xpath = Locators.BUTTONS['all_buttons'].format('CANCEL')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def event_test_configure_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_test_config_btn_xpath,
                                             'event_test_configure_button')
            print('Event Test Configuration button - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_job_name_field(self, job_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_name_xpath, job_name, 'test_job_name_field')
            self.wait.drop_down_selection()
            print(f'Test Configuration Job Name - {job_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_stage_name_field(self, stage_name):
        try:
            time.sleep(0.8)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_stage_xpath, stage_name, 'test_job_name_field')
            self.wait.drop_down_selection()
            print(f'Test Configuration stage Name - {stage_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_test_name_field(self, test_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_test_xpath, test_name, 'test_job_name_field')
            self.wait.drop_down_selection()
            print(f'Test Configuration Assessment Name - {test_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_active_enable(self):
        try:
            time.sleep(0.6)
            button = ' On'
            self.wait.web_elements_wait_multiple_click(By.CSS_SELECTOR, self.__e_test_active_css, button)
            print(f'Event Ec - {button} - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_test_configure_save(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_test_save_xpath, 'event_test_configure_save')
            print('Event Test Configuration Save - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_tag_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_tag_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.7)
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_test_extra_config(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_test_config_cancel_xpath, 'cancel_test_extra_config')
            return True
        except Exception as error:
            ui_logger.error(error)
