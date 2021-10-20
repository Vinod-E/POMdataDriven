from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class EntryButton:

    __e_next_button_xpath = Locators.BUTTONS['button'].format('Next')
    __e_para_text_tag = Locators.TAG['p']

    para = ''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def page_validation(self):
        try:
            self.wait.web_element_wait_text(By.TAG_NAME, self.__e_para_text_tag, 'page_validation')
            self.para = self.wait.text_value
            print('Entry Page Validation By name:: ', self.para)
            return True
        except Exception as error:
            ui_logger.error(error)

    def entry_next(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_next_button_xpath, 'entry_next')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
