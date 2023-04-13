import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class ActivityTaskConfigPage:
    __e_job_task_config_btn_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'configureTask', "'")
    __e_job_task_new_row_class = Locators.JOB['task_new']
    __e_activity_stage_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Stage And Status')
    __e_activity_positive_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Positive Stage - Status')
    __e_activity_negative_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Negative Stage - Status')
    __e_activity_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Activity')
    __e_task_select_xpath = Locators.TITLE['title'].format('Select Tasks')
    __e_activity_save_xpath = Locators.BUTTONS['actionClicked'].format("'", 'saveTaskConfig', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def job_task_configure_button(self):
        try:
            self.scroll.up(0, 250)
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_task_config_btn_xpath, 'job_task_configure_button')
            self.wait.loading()
            print('Job Task Configuration button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def task_new_row(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_job_task_new_row_class, 'task_new_row')
            print('Job Task New Row - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_activity_stage_field(self, stage_status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_activity_stage_xpath, stage_status,
                                                 'job_activity_stage_field')
            self.wait.drop_down_selection()
            print('Job Activity stage/status - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_activity_positive_stage_field(self, positive_stage_status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_activity_positive_xpath, positive_stage_status,
                                                 'job_activity_positive_stage_field')
            self.wait.drop_down_selection()
            print('Job Activity Positive Stage/status - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_activity_negative_stage_field(self, negative_stage_status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_activity_negative_xpath, negative_stage_status,
                                                 'job_activity_negative_stage_field')
            self.wait.drop_down_selection()
            print('Job Activity Negative Stage/status - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_activity_field(self, activity):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_activity_xpath, activity,
                                                 'job_negative_stage_field')
            self.wait.drop_down_selection()
            print('Job Activity - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_task_field(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_task_select_xpath, 'job_task_field')
            print('Job Task Field - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_activity_task_save(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_activity_save_xpath, 'job_activity_task_save')
            print('Job Activity Task - Saved')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_task_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_task_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
