import time
from utilities import appTitle
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects import Locators
from utilities.uiNotifier import Notifier
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class JobCreationPage:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_create = Locators.BUTTONS['create']
    __e_job_names = Locators.JOB['job_name']
    __e_anchor_tag = Locators.TAG['anchor']
    __e_file_path = Locators.ATTACHMENT['file']
    __e_description = Locators.JOB['description']
    __e_location = Locators.PLACEHOLDER['text_ph'].format('Location')
    __e_hm = Locators.PLACEHOLDER['text_ph'].format('Hiring Manager')
    __e_bu = Locators.PLACEHOLDER['text_ph'].format('Business Unit')
    __e_openings = Locators.JOB['openings']
    __e_male = Locators.PLACEHOLDER['num_ph'].format('Male')
    __e_female = Locators.PLACEHOLDER['num_ph'].format('Female')
    __e_job_create = Locators.BUTTONS['button'].format('Create')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.notifier = Notifier(self.driver)
        self.tab_title = appTitle.Title(self.driver)

    def job_tab(self, tab_name, tab_title):
        try:
            self.tab.job_tab(tab_name)
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True

        except Exception as error:
            ui_logger.error(error)

    def create_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_create, 'Job Create Button')
            print('***--------->>> Clicked on job created button')
            self.wait.loading()
            return True

        except Exception as error:
            ui_logger.error(error)

    def job_name(self, name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_names, name, 'Job_name_field')
            return True

        except Exception as error:
            ui_logger.error(error)

    def job_attachment(self, file_path):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_file_path, file_path, 'Job_attachment')
            time.sleep(0.5)
            self.wait.uploading()
            return True

        except Exception as error:
            ui_logger.error(error)

    def job_attachment_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            self.notifier.dismiss_message()
            return True

        except Exception as error:
            ui_logger.error(error)

    def job_description(self, description):
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_description, description, 'Job_description')
        self.wait.drop_down_selection()
        return True

    def job_location(self, location):
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_location, location, 'Job_location_field')
        self.wait.drop_down_selection()
        return True

    def job_hiring_manager(self, hm):
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_hm, hm, 'job_hm_field')
        self.wait.drop_down_selection()
        return True

    def job_business_unit(self, bu):
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_bu, bu, 'Job_bu_field')
        self.wait.drop_down_selection()
        return True

    def job_openings(self, openings):
        self.wait.clear(By.NAME, self.__e_openings, 'Job_openings_field')
        self.wait.web_element_wait_send_keys(By.NAME, self.__e_openings, openings, 'Job_openings_field')
        return True

    def job_male_diversity(self, male_diversity):
        self.wait.clear(By.XPATH, self.__e_male, 'Job_male_field')
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_male, male_diversity, 'Job_male_field')
        return True

    def job_female_diversity(self, female_diversity):
        self.wait.clear(By.XPATH, self.__e_female, 'Job_female_field')
        self.wait.web_element_wait_send_keys(By.XPATH, self.__e_female, female_diversity, 'Job_female_field')
        return True

    def job_create(self):
        self.wait.web_element_wait_click(By.XPATH, self.__e_job_create, 'Job_create_button')
        self.wait.loading()
        return True

    def job_create_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_create_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
