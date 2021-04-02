import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class EventGetByName:

    __e_click_name_xpath = Locators.TITLE['title'].format('Click to view full details')
    __e_event_name_xpath = Locators.TITLE['title']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def event_name_click(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_click_name_xpath, 'Event_name_click')
            time.sleep(1.5)
            self.wait.loading()

            return True
        except Exception as error:
            ui_logger.error(error)

    def event_name_validation(self, event_name):
        try:
            self.wait.web_element_wait_text(By.XPATH,
                                            self.__e_event_name_xpath.format(event_name),
                                            'Event_name_validation')
            print('Event Name -', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)
