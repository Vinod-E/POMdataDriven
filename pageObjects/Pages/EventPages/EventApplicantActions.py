import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll


class EventApplicantActions:

    __e_status_change_id = Locators.ACTIONS['status_change']
    __e_more_button_xpath = Locators.ACTIONS['app_more']
    __e_app_action_xpath = Locators.BUTTONS['all_buttons']
    __e_provide_feedback_id = Locators.ACTIONS['provide_feedback']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
    """
     ****--------------------- Event Applicant Action Functions ---------------------------------****
    """
    def change_status_action(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_status_change_id, 'Applicant_status_change')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def more_action(self):
        try:
            self.scroll.up(0, 50)
            self.wait.web_element_wait_click(By.XPATH, self.__e_more_button_xpath, 'more_action')
            print('Clicked on - Applicant More actions')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def quick_interview_action(self):
        try:
            self.wait.web_element_wait_click(By.XPATH,
                                             self.__e_app_action_xpath.format('Quick Interview Schedule'),
                                             'quick_interview_action')
            time.sleep(2)
            print('Quick Interview Action - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    """
     ****--------------------- Event Interviews Applicant Action Functions ---------------------------------****
    """
    def provide_feedback_action(self):
        try:
            self.scroll.down(0, -50)
            self.wait.web_element_wait_click(By.ID, self.__e_provide_feedback_id, 'provide_feedback_action')
            time.sleep(2)
            print('Provide Feedback Action - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
