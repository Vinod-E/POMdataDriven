import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By

from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class EventSubTabs:
    __e_event_config_xpath = Locators.SUB_MENU['configurations']
    __e_event_owners_xpath = Locators.SUB_MENU['owners']
    __e_event_tracking_xpath = Locators.SUB_MENU['event_tracking']
    __e_cancel_request_xpath = Locators.SUB_MENU['cancel_request']
    __e_manage_candidates = Locators.BUTTONS['all_buttons'].format('Manage Candidates')
    __e_interview_slot_xpath = '//*[@ui-sref="crpo.events.details.tracking.configureInterviewSlots"]'
    __e_assessment_slot_xpath = '//*[@ui-sref="crpo.events.details.tracking.configureAssessmentSlots"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def event_configurations(self):
        try:
            self.scroll.up(0, -100)
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_config_xpath, 'Event_configurations_tab')
            time.sleep(0.5)
            print('Event Configurations Tab - Landed')
            self.scroll.up(0, 200)
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_owners(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_owners_xpath, 'Event_owners_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def manage_candidates(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_manage_candidates, 'Manage_Candidates')
            return True
        except Exception as error:
            ui_logger.error(error)

    def tracking(self):
        try:
            self.scroll.up(0, -60)
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_tracking_xpath, 'event_tracking')
            return True
        except Exception as error:
            ui_logger.error(error)

    def interview_slot_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_interview_slot_xpath, 'interview_slot_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def assessment_slot_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_assessment_slot_xpath, 'assessment_slot_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def cancel_request_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_cancel_request_xpath, 'cancel_request_tab')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)
