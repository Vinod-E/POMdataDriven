import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll
from utilities.SwitchWindow import SwitchWindowClose


class EventApplicantActions:

    __e_status_change_id = Locators.ACTIONS['status_change']
    __e_more_button_xpath = Locators.ACTIONS['app_more']
    __e_app_action_xpath = Locators.BUTTONS['all_buttons']
    __e_provide_feedback_id = Locators.ACTIONS['provide_feedback']
    __e_cancel_request_id = Locators.ACTIONS['cancel_request']
    __e_cancel_interview_id = Locators.ACTIONS['cancel_interview']
    __e_unlock_feedback_id = Locators.ACTIONS['unlock_feedback']
    __e_revise_feedback_xpath = '//*[@id="mainBodyElement"]//div[22]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)
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
            self.scroll.right(300, 0)
            return True
        except Exception as error:
            ui_logger.error(error)

    def quick_interview_action(self, index_window):
        try:
            self.wait.web_element_wait_click(By.XPATH,
                                             self.__e_app_action_xpath.format('Quick Interview Schedule'),
                                             'quick_interview_action')
            time.sleep(2)
            self.switch_window.switch_to_window(index_window)
            print('Quick Interview Action - Clicked')
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

    def cancel_interview_request_action(self):
        try:
            self.scroll.down(0, -50)
            self.wait.web_element_wait_click(By.ID, self.__e_cancel_request_id, 'cancel_interview_request_action')
            time.sleep(2)
            print('Cancel Request Action - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_interview_action(self):
        try:
            self.scroll.down(0, -50)
            self.wait.web_element_wait_click(By.ID, self.__e_cancel_interview_id, 'cancel_interview_action')
            time.sleep(2)
            print('Cancel Interview Action - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def unlock_feedback_action(self):
        try:
            self.scroll.down(0, -50)
            self.wait.web_element_wait_click(By.ID, self.__e_unlock_feedback_id, 'unlock_feedback_action')
            print('Unlock Feedback Action - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def applicant_revise_feedback(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_revise_feedback_xpath,
                                             'applicant_revise_feedback')
            print('Revised Feedback Action')
            return True
        except Exception as error:
            ui_logger.error(error)
