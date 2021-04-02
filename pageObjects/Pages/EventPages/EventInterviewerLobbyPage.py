import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class InterviewerLobbyPage:

    __e_select_candidate_xpath = Locators.BUTTONS['button'].format('Select Candidate')
    __e_provide_feedback_xpath = Locators.BUTTONS['actionClicked'].format("'", 'provideFeedBack', "'")
    __e_invite_video_xpath = Locators.BUTTONS['actionClicked'].format("'", 'markAsCurrentCandidate', "'")
    __e_invite_check_xpath = Locators.CHECK_BOX['check_box']
    __e_proceed_xpath = Locators.BUTTONS['button'].format('Proceed To Interview')
    __e_finish_interview_xpath = Locators.BUTTONS['button'].format('Interview is Finished')
    __e_full_finish_interview_xpath = Locators.INTERVIEWER_LOBBY['finish_interview']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def select_candidate(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_candidate_xpath, 'select_candidate')
            print('Selected New candidate into - Queue')
            return True
        except Exception as error:
            ui_logger.error(error)

    def provide_feedback(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_provide_feedback_xpath, 'provide_feedback')
            return True
        except Exception as error:
            ui_logger.error(error)

    def invite_video_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_invite_video_xpath, 'invite_video_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def check_box(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_invite_check_xpath, 'invite_check_box')
            return True
        except Exception as error:
            ui_logger.error(error)

    def proceed_video_link(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_proceed_xpath, 'proceed_video_link')
            time.sleep(1)
            print('Open Video Interview Link  - screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def finish_interview(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_finish_interview_xpath, 'finish_interview')
            print('Finish Interview - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def full_finish_interview(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_full_finish_interview_xpath, 'full_finish_interview')
            print('Full Finish Interview - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
