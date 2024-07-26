import time
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll


class VideoInterviewPage:
    __e_h4 = 'h4'
    __e_got_to_interview_xpath = '//*[@ng-click="vm.isLinkOpened=true"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def page_validation(self, page_header):
        try:
            time.sleep(3)
            self.wait.web_element_wait_text(By.TAG_NAME, self.__e_h4, 'page_validation')
            if self.wait.text_value == page_header:
                print("On page is:: ", self.wait.text_value)
                return True
        except Exception as error:
            ui_logger.error(error)

    def go_to_interview(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_got_to_interview_xpath, 'account_name_click')
            return True
        except Exception as error:
            ui_logger.error(error)
