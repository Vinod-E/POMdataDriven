from selenium.webdriver.common.by import By
from pageObjects import Locators
from utilities.WebDriver_Wait import WebElementWait


class Notifier:
    e_notifier = Locators.NOTIFIER['message']
    e_dismiss = Locators.NOTIFIER['dismiss']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def glowing_messages(self, ui_message):
        self.wait.web_element_wait_text(By.CLASS_NAME, self.e_notifier, 'Glowing_message')
        message = self.wait.text_value
        if message == ui_message:
            print('**-------->>> Message/UI notifier validated successfully - {}'.format(message))
        else:
            print('Message/UI notifier validation failed - {} <<<---------**'.format(message))

    def dismiss_message(self):
        self.wait.web_element_wait_click(By.CLASS_NAME, self.e_dismiss, 'Dismiss_message')
        print('***---------->>> Notifier closed')
