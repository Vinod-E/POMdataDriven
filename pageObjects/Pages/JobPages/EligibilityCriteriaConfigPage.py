import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EligibilityCriteriaPage:
    __e_job_config_btn_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'configureEC', "'")
    __e_ec_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Eligibility Criteria')
    __e_positive_stage_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Stage')
    __e_positive_status_xpath = Locators.PLACEHOLDER['text_ph'].format('Select status')
    __e_negative_stage_xpath = Locators.JOB['Ec_negative_stage']
    __e_negative_status_xpath = Locators.JOB['Ec_negative_status']
    __e_ec_save_xpath = Locators.BUTTONS['ec_save']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def job_configure_button(self):
        try:
            self.wait.loading()
            self.scroll.down(0, -200)
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_config_btn_xpath, 'job_configure_button')
            self.wait.loading()
            print('Job Configuration button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_ec_field(self, eligibility_criteria):
        try:
            time.sleep(1)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_ec_xpath, eligibility_criteria,
                                                 'job_ec_field')
            self.wait.drop_down_selection()
            print('Job Eligibility Criteria - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_positive_stage_field(self, stage):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_positive_stage_xpath, stage,
                                                 'job_positive_stage_field')
            self.wait.drop_down_selection()
            print('Job Positive Stage - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_positive_status_field(self, status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_positive_status_xpath, status,
                                                 'job_positive_status_field')
            self.wait.drop_down_selection()
            print('Job Positive Status - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_negative_stage_field(self, stage):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_negative_stage_xpath, stage,
                                                 'job_negative_stage_field')
            self.wait.drop_down_selection()
            print('Job Negative Stage - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_negative_status_field(self, status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_negative_status_xpath, status,
                                                 'job_negative_status_field')
            self.wait.drop_down_selection()
            print('Job Negative Status - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_ec_save(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ec_save_xpath, 'job_ec_save')
            print('Job Eligibility Criteria - Saved')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_ec_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_ec_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
