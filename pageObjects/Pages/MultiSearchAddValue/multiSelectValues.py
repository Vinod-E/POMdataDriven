from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class MultiSelectValues:

    __e_search_xpath = Locators.TITLE['title'].format('Type here to search')
    __e_select_search_item_xpath = Locators.MULTI_SELECTIONS['moveAllItemsRight']
    __e_done_button_xpath = Locators.BUTTONS['done']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def search(self, search_value):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_search_xpath, search_value, 'Multi_value_search')
            return True
        except Exception as error:
            ui_logger.error(error)

    def move_all_items(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_search_item_xpath, 'Move_all_items')
            return True
        except Exception as error:
            ui_logger.error(error)

    def done(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_done_button_xpath, 'Done_button')
            return True
        except Exception as error:
            ui_logger.error(error)
