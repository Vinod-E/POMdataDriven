import time
from utilities import appTitle
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects import Locators
from utilities.uiNotifier import Notifier
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class RequirementCreationPage:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_create = Locators.BUTTONS['create']
    __e_req_name_xpath = Locators.PLACEHOLDER['place_holder'].format('Name')
    __e_req_job_xpath = Locators.TITLE['title'].format('Job Roles')
    __e_req_track_xpath = Locators.PLACEHOLDER['text_ph'].format('Hiring Type')
    __e_req_type_xpath = Locators.PLACEHOLDER['text_ph'].format('College Type')
    __e_req_create_xpath = Locators.BUTTONS['actionClicked'].format("'", 'create', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.notifier = Notifier(self.driver)
        self.tab_title = appTitle.Title(self.driver)

    def requirement_tab(self, tab_name, tab_title):
        try:
            self.tab.requirement_tab(tab_name)
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

    def requirement_name(self, name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_req_name_xpath, name, 'requirement_name')
            print(f'Requirement name entered - {name}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_job(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.XPATH, self.__e_req_job_xpath, 'requirement_job')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_hiring(self, track):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_req_track_xpath, track,
                                                 'requirement_hiring')
            self.wait.drop_down_selection()
            print(f'Requirement hiring track - {track}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_type(self, college_type):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_req_type_xpath, college_type,
                                                 'requirement_type')
            self.wait.drop_down_selection()
            print(f'Requirement college type - {college_type}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_create(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_req_create_xpath, 'req_create_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def req_creation_notifier(self, message):
        try:
            time.sleep(0.4)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def req_creation_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
