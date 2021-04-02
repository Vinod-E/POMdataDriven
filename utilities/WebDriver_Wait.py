import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Listeners.logger_settings import ui_logger
from Listeners.screenShot import FailureImage
from pageObjects import Locators


class WebElementWait:
    """
    Generic function will be easy to do script writing.

    """
    load = Locators.LOADING['load']
    load_text = Locators.LOADING['load_text']
    upload = Locators.LOADING['upload']

    def __init__(self, driver):
        self.driver = driver
        self.perform = ''
        self.text_value = ''
        self.element_failure_image = FailureImage(self.driver)

    def __web_element_wait(self, by_locator, element, failure_name):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                self.perform = self.driver.find_element(by_locator, element)
                result = True
                break
            except Exception as error:
                ui_logger.error(error)
                time.sleep(1.5)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        if attempts == 10:
            self.element_failure_image.screen_shot(f'{attempts}_{failure_name}')
        return result

    def web_elements_wait(self, by_locator, element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                self.perform = self.driver.find_elements(by_locator, element)
                result = True
                break
            except Exception as error:
                ui_logger.error(error)
                time.sleep(1.5)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        if attempts == 10:
            self.element_failure_image.screen_shot(f'{attempts}{element}')
        return result

    def loading(self):
        attempts = 1000
        for i in range(0, attempts):
            try:
                if self.driver.find_element(By.CLASS_NAME, self.load):
                    self.perform = self.driver.find_element(By.CLASS_NAME, self.load)
                    if self.perform:
                        # print(f'{self.perform.text}............!!')
                        time.sleep(0.5)
            except Exception as error:
                # ui_logger.error(error)
                break
        print('***--------->>> Page Loading Completed <<<---------***')

    def uploading(self):
        attempts = 150
        for i in range(0, attempts):
            try:
                if self.driver.find_element(By.XPATH, self.upload):
                    self.perform = self.driver.find_element(By.XPATH, self.upload)
                    if self.perform.text == 'Uploading ...':
                        # print(f'{self.perform.text}............!!')
                        time.sleep(0.2)
            except Exception as error:
                # print(error)
                break
        print('***--------->>> Uploading File Completed <<<---------***')

    def web_element_wait_send_keys(self, by_locator, element, keys, failure_name):
        self.__web_element_wait(by_locator, element, failure_name)
        self.perform.send_keys(keys)

    def web_element_wait_click(self, by_locator, element, failure_name):
        self.__web_element_wait(by_locator, element, failure_name)
        self.perform.click()

    def web_element_wait_text(self, by_locator, element, failure_name):
        self.__web_element_wait(by_locator, element, failure_name)
        self.text_value = self.perform.text

    def web_elements_wait_text(self, by_locator, element, value):
        time.sleep(2)
        text = ''
        self.web_elements_wait(by_locator, element)
        for i in self.perform:
            if i.text.strip() == value:
                text = i.text.strip()
                break
        return text

    def web_elements_wait_click(self, by_locator, element, value):
        button_name = ''
        time.sleep(1)
        self.web_elements_wait(by_locator, element)
        for i in self.perform:
            if i.text.strip() == value.strip():
                button_name = i.text.strip()
                i.click()
                break
        return button_name

    def web_elements_wait_multiple_click(self, by_locator, element, value):
        button_name = ''
        self.web_elements_wait(by_locator, element)
        for i in self.perform:
            if i.text.strip() == value.strip():
                button_name = i.text.strip()
                i.click()
                time.sleep(1.5)
        return button_name

    def web_elements_wait_send_keys(self, by_locator, element, keys):
        self.web_elements_wait(by_locator, element)
        for i in self.perform:
            if i:
                i.send_keys(keys)
                time.sleep(1)

    def clear(self, by_locator, element, failure_name):
        self.__web_element_wait(by_locator, element, failure_name)
        self.perform.clear()

    def drop_down_selection(self):
        self.perform.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
