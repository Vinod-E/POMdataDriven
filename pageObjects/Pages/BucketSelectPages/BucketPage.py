import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.OpenNewTab import NewTab


class BucketSelectionPage:

    __e_bucket_xpath = Locators.BUCKET['event_interviews']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.new_tab = NewTab(self.driver)

    def bucket_select(self, bucket_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_bucket_xpath, bucket_name, 'bucket_select')
            print(f'Chosen bucket is - {bucket_name}')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
