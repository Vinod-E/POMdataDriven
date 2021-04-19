import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventOwnersConfigPage:

    __e_owners_update_xpath = Locators.BUTTONS['button'].format('Update')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def event_owners_update(self):
        try:
            self.scroll.down(0, -50)
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_owners_update_xpath, 'event_owners_update')
            print('Event Owners update button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_owners_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_owners_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            self.wait.loading()
            self.scroll.up(0, 70)
            return True
        except Exception as error:
            ui_logger.error(error)
