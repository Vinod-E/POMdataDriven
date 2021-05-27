import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll
from utilities.uiNotifier import Notifier


class RequirementHelpDeskConfig:

    __e_default_category_xpath = Locators.TITLE['title'].format('Query Category')
    __e_job_category_xpath = Locators.HELPDESK['job_category']
    __e_event_category_xpath = Locators.HELPDESK['event_category']
    __e_user_xpath = Locators.TITLE['title'].format('Users')
    __e_job_user_xpath = Locators.HELPDESK['job_user']
    __e_event_user_xpath = Locators.HELPDESK['event_user']
    __e_sla_xpath = Locators.PLACEHOLDER['num']
    __e_jobs_xpath = Locators.TITLE['title'].format('Jobs')
    __e_event_job_xpath = Locators.HELPDESK['event_job']
    __e_job_sla_xpath = Locators.HELPDESK['job_sla']
    __e_event_xpath = Locators.TITLE['title'].format('Events')
    __e_event_sla_xpath = Locators.HELPDESK['event_sla']
    __e_save_button_xpath = Locators.BUTTONS['button'].format('Save')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def default_category(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_default_category_xpath, 'default_category')
            print('default_category - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_category(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_category_xpath, 'job_category')
            print('job_category - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_category(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_category_xpath, 'event_category')
            print('event_category - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def category_user_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_user_xpath, 'category_user_selection')
            print('category_user_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_user_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_job_user_xpath, 'job_user_selection')
            print('job_user_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_user_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_user_xpath, 'event_user_selection')
            print('event_user_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def category_sla_hour_selection(self, hours):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_sla_xpath, hours,
                                                 'category_sla_hour_selection')
            print('category_sla_hour_selection - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_sla_hour_selection(self, hours):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_sla_xpath, hours,
                                                 'job_sla_hour_selection')
            print('job_sla_hour_selection - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_sla_hour_selection(self, hours):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_sla_xpath, hours,
                                                 'event_sla_hour_selection')
            print('event_sla_hour_selection - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def category_job_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_jobs_xpath, 'category_job_selection')
            print('category_job_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_job_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_job_xpath, 'event_job_selection')
            print('event_job_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def category_event_selection(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_xpath, 'category_event_selection')
            print('category_event_selection - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_help_desk_config(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_button_xpath, 'save_help_desk_config')
            print('save_help_desk_config - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def config_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def config_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.9)
            return True
        except Exception as error:
            ui_logger.error(error)
