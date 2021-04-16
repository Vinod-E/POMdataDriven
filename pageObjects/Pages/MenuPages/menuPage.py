from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities import appTitle
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class Menu:
    __e_menu = Locators.MENU['menu']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab_title = appTitle.Title(self.driver)
        self.scroll = PageScroll(self.driver)

    def job_tab(self, job_menu_name, tab_title):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(job_menu_name), 'not_in_job_roles')
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True
        except Exception as error:
            ui_logger.error(error)

    def requirement_tab(self, req_menu_name, tab_title):
        try:
            self.scroll.up(0, 50)
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(req_menu_name), 'not_in_Requirements')
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True
        except Exception as error:
            ui_logger.error(error)

    def assessment_tab(self, assess_menu_name, tab_title):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(assess_menu_name), 'not_in_assessments')
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_tab(self, event_menu_name, tab_title):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(event_menu_name), 'not_in_Events')
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True
        except Exception as error:
            ui_logger.error(error)

    def more_tab(self, more_menu_name):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(more_menu_name), 'not_in_More')
            return True
        except Exception as error:
            ui_logger.error(error)

    def embrace_tab(self, embrace_menu_name):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(embrace_menu_name), 'not_in_Embrace')
            return True
        except Exception as error:
            ui_logger.error(error)
