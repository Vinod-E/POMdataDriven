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
    __e_test_name = Locators.SEARCH['test_name']
    __e_candidate_name = Locators.SEARCH['candidate_name']
    __e_search_btn_xpath = Locators.BUTTONS['button'].format('Search')
    __e_manage_search_css = Locators.SEARCH['manage_candidate_search']
    __e_clear_id = Locators.SEARCH['clear']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab = Menu(self.driver)
        self.tab_title = appTitle.Title(self.driver)
        self.page_scroll = PageScroll.PageScroll(self.driver)

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

    def candidate_name_field(self, search_key):
        try:
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_candidate_name, search_key,
                                                 'search_applicant_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def test_name_search_field(self, search_key):
        try:
            time.sleep(1)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_test_name, search_key, 'test_name_search_field')
            print('Test name - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_button(self):
        try:
            time.sleep(1)
            self.page_scroll.up(0, 170)
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_btn_xpath, 'search_button')
            self.wait.loading()
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

    def job_search_button(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_btn_xpath, 'search_button')
            print('Job name - Searched')
            return True
        except Exception as error:
            ui_logger.error(error)
