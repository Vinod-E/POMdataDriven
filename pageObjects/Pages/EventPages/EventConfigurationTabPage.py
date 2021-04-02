import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll
from utilities.uiNotifier import Notifier
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs


class EventConfiguration:

    __e_click_radio_css = Locators.BUTTONS['radio']
    __e_user_id_xpath = Locators.TITLE['title'].format('Current Status')
    __e_search_user_xpath = Locators.TITLE['title'].format('Type here to search')
    __e_select_search_item_xpath = Locators.MULTI_SELECTIONS['moveAllItemsRight']
    __e_done_button_xpath = Locators.BUTTONS['done']
    __e_save_button_xpath = Locators.BUTTONS['button'].format('save')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.event_tab = EventSubTabs(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def configurations_tab(self):
        try:
            self.scroll.up(0, -100)
            self.event_tab.event_configurations()
            time.sleep(0.5)
            print('Event Configurations Tab - Landed')
            self.scroll.up(0, 200)
            return True
        except Exception as error:
            ui_logger.error(error)

    def on_off_buttons(self, button_name):
        try:
            time.sleep(1)
            self.wait.web_elements_wait_multiple_click(By.CSS_SELECTOR, self.__e_click_radio_css, button_name)
            return True
        except Exception as error:
            ui_logger.error(error)

    def user_id_chat(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_user_id_xpath, 'chat_user_filed_click')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_user_chat(self, user_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_search_user_xpath, user_name, 'search_chat_user')
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_search_item_xpath, 'Move_all_items')
            self.wait.web_element_wait_click(By.XPATH, self.__e_done_button_xpath, 'Done_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def enable_disable_button(self, button_name):
        try:
            self.wait.web_elements_wait_click(By.CSS_SELECTOR, self.__e_click_radio_css, button_name)
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_buttons(self, button_name, message):
        try:
            self.wait.web_elements_wait_multiple_click(By.XPATH, self.__e_save_button_xpath, button_name)
            self.notifier.glowing_messages(message)
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)
