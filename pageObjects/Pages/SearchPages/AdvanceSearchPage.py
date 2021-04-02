import time
from utilities import appTitle, PageScroll
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class Search:
    __e_search_id = Locators.SEARCH['advance_search']
    __e_Name_name = Locators.SEARCH['Name']
    __e_name_name = Locators.SEARCH['name']
    __e_search_btn_xpath = Locators.BUTTONS['button'].format('Search')
    __e_manage_search_css = Locators.SEARCH['manage_candidate_search']
    __e_clear_id = Locators.SEARCH['clear']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.tab_title = appTitle.Title(self.driver)
        self.page_scroll = PageScroll.PageScroll(self.driver)

    def event_tab(self, tab_name, tab_title):
        try:
            self.tab.event_tab(tab_name)
            self.wait.loading()
            assert self.tab_title.tab_title(tab_title) == tab_title, 'Webdriver is in wrong tab'
            return True
        except Exception as error:
            ui_logger.error(error)

    def advance_search(self):
        try:
            self.page_scroll.down(0, -200)
            self.wait.web_element_wait_click(By.ID, self.__e_search_id, 'advance_search')
            return True
        except Exception as error:
            ui_logger.error(error)

    def name_field(self, search_key):
        try:
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_Name_name, search_key, 'search_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def name_field_applicant(self, search_key):
        try:
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_name_name, search_key, 'search_applicant_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_button(self):
        try:
            time.sleep(1)
            self.page_scroll.up(0, 300)
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_btn_xpath, 'search_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def manage_candidate_search(self):
        try:
            self.wait.web_element_wait_click(By.CSS_SELECTOR, self.__e_manage_search_css, 'advance_search')
            return True
        except Exception as error:
            ui_logger.error(error)

    def clear_search(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.ID, self.__e_clear_id, 'advance_search')
            return True
        except Exception as error:
            ui_logger.error(error)
