import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventNominationTabPage:
    __e_arrow_down_class = Locators.NOMINATIONS['dropdown']
    __e_header_tag = Locators.TAG['h6']
    __e_button_xpath = Locators.BUTTONS['button'].format('Confirm')
    __e_ok_xpath = Locators.BUTTONS['all_buttons'].format('OK')
    __e_draw_xpath = Locators.BUTTONS['button'].format('Withdraw nomination')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

        self.button = 'Withdraw nomination'

    def event_row_arrow_down(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_arrow_down_class, 'nomination_tab')
            print('Interviewers nomination_tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def nomination_job_validation(self, job_name):
        try:
            assert self.wait.web_elements_wait_text(By.TAG_NAME, self.__e_header_tag, job_name) == job_name, \
                'Arrow down for wrong job role'
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_interviewer_nomination(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_button_xpath, 'confirm_interviewer_nomination')
            print('confirm_interviewer_nomination - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ok_confirm(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ok_xpath, 'ok_confirm')
            print('ok_confirm - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def nomination_accept_validation(self):
        try:
            assert self.wait.web_elements_wait_text(By.XPATH, self.__e_draw_xpath,
                                                    self.button) == self.button, \
                'Not confirmed YET'
            return True
        except Exception as error:
            ui_logger.error(error)
