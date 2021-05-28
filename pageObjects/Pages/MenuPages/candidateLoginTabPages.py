from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities import appTitle
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class CandidateLoginMenus:
    __e_menu = Locators.MENU['menu']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.tab_title = appTitle.Title(self.driver)
        self.scroll = PageScroll(self.driver)

    def help_tab(self, menu_name):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(menu_name), 'help_tab')
            print(f'Clicked on - {menu_name}')
            self.wait.candidate_login_loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def my_task_tab(self, menu_name):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(menu_name), 'my_task_tab')
            print(f'Clicked on - {menu_name}')
            return True
        except Exception as error:
            ui_logger.error(error)
