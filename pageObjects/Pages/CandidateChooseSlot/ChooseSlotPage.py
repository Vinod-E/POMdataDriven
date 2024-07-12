import time
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class ChooseSlot:
    __e_choose_one_name = 'Cognitive and Technical Assessment'
    __e_choose_two_name = 'Cognitive Assessment'
    __e_reset_button_class = '//button[@ng-click="vm.actionClicked({}{}{})"]'.format("'", "reset", "'")
    __e_submit_button_xpath = '//button[@ng-click="vm.actionClicked({}{}{})"]'.format("'", "submit", "'")
    __e_thank_you_page_xpath = '//*[@class="ng-binding"]'

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def choose_one_selection(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.NAME, self.__e_choose_one_name, 'choose_one_selection')
            return True
        except Exception as error:
            ui_logger.error(error)

    def choose_two_selection(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.NAME, self.__e_choose_two_name, 'choose_two_selection')
            return True
        except Exception as error:
            ui_logger.error(error)

    def reset_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_reset_button_class,
                                             'reset_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def submit_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_submit_button_xpath,
                                             'reset_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def thank_you_page(self):
        try:
            a = self.wait.web_element_wait_text(By.XPATH, self.__e_thank_you_page_xpath, 'thank_you_page')
            print('Display message:: ', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)

    def update_slot(self, slot_name):
        try:
            self.driver.back()
            self.wait.refresh_page()
            time.sleep(3)
            a = self.wait.web_elements_wait_click(By.CLASS_NAME, self.__e_choose_one_name, slot_name)
            print('Update Slot Name:: ', a)
            return True
        except Exception as error:
            ui_logger.error(error)
