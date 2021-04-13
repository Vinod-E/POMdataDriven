from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class Actions:
    __e_test_actions_xpath = Locators.ACTIONS['actions_click']
    __e_clone_test_id = Locators.ACTIONS['clone_assessment']

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def assessment_actions_click(self):
        try:
            self.scroll.up(0, 50)
            self.wait.web_element_wait_click(By.XPATH, self.__e_test_actions_xpath, 'assessment_actions_click')
            print('Assessment Actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def clone_assessment(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_clone_test_id, 'clone_assessment')
            self.wait.loading()
            print('Clone Assessment action - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
