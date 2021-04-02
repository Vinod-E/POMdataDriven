import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class Actions:
    __e_event_actions_xpath = Locators.ACTIONS['actions_click']
    __e_event_candidates_id = Locators.ACTIONS['view_candidates']
    __e_event_slot_id = Locators.ACTIONS['slot_config']
    __e_event_lobby_id = Locators.ACTIONS['lobby']
    __e_event_interview_lobby = Locators.ACTIONS['panel']

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def event_actions_click(self):
        try:
            self.scroll.up(0, 100)
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_actions_xpath, 'Event_actions_click')
            print('Event Actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_view_candidates(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_event_candidates_id, 'Event_candidates_action')
            self.wait.loading()
            print('Event View Applicant - Screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_slot_configuration(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_event_slot_id, 'Event_slot_config_action')
            self.wait.loading()
            print('Event slot configuration - Screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_lobby(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_event_lobby_id, 'View_Event_Lobby')
            self.wait.loading()
            print('View Event Lobby - Screen')
            return True
        except Exception as error:
            ui_logger.error(error)

    def interview_lobby_panel(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_event_interview_lobby, 'Interviewer_Lobby_panel')
            self.wait.loading()
            print('Event_interviewer_lobby - Screen')
            time.sleep(5)
            print('Event_interviewer_lobby - whiteScreen')
            return True
        except Exception as error:
            ui_logger.error(error)
