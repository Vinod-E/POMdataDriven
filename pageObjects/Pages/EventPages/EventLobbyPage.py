import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs


class LobbyPage:
    __e_create_button_xpath = Locators.BUTTONS['button'].format('Create Room')
    __e_room_name_xpath = Locators.PLACEHOLDER['text_ph'].format('Room Name')
    __e_interviewers_xpath = Locators.TITLE['title'].format('Select Interviewers')
    __e_participants_xpath = Locators.TITLE['title'].format('Select Participants')
    __e_search_xpath = Locators.TITLE['title'].format('Type here to search')
    __e_select_all_xpath = Locators.MULTI_SELECTIONS['moveAllItemsRight']
    __e_done_button = Locators.BUTTONS['all_buttons'].format('Done')
    __e_created_room_xpath = Locators.BUTTONS['actionClicked'].format("'", 'createRoom', "'")
    __e_active_room_xpath = Locators.EVENT_LOBBY['active']
    __e_ok_button_xpath = Locators.BUTTONS['all_buttons'].format('OK')
    __e_un_assign_xpath = Locators.EVENT_LOBBY['un_assign']
    __e_assign_room_xpath = Locators.EVENT_LOBBY['assign_room']
    __e_room_name_field_xpath = Locators.PLACEHOLDER['text_ph'].format('Room Name')
    __e_room_search_filed_xpath = Locators.TITLE['title'].format('Select Room')
    __e_search_button_xpath = Locators.BUTTONS['button'].format('Search')
    __e_room_search_class = Locators.EVENT_LOBBY['room_search']
    __e_assigning_room_xpath = Locators.BUTTONS['actionClicked'].format("'", 'assignCandidateToRoom', "'")
    __e_candidate_info_xpath = Locators.TITLE['title'].format('View Candidate Info')

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.message = Notifier(self.driver)
        self.sub_tab = EventSubTabs(self.driver)

    def create_room_button(self):
        try:
            self.scroll.up(0, 100)
            self.wait.web_element_wait_click(By.XPATH, self.__e_create_button_xpath, 'room_create_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def room_name(self, room_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_room_name_xpath, room_name, 'room_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_interviewers_xpath, 'Interviewers_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_participants(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_participants_xpath, 'Participants_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search(self, key):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_search_xpath, key, 'Search_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def move_all(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_select_all_xpath, 'Move_all_items')
            return True
        except Exception as error:
            ui_logger.error(error)

    def done(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_done_button, 'Done_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def created_button(self, message):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_created_room_xpath, 'room_created_button')
            self.wait.loading()
            self.message.glowing_messages(message)
            self.message.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

    def active_room(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_active_room_xpath, 'room_created_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ok_button(self, message):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ok_button_xpath, 'room_created_button')
            time.sleep(0.5)
            self.message.glowing_messages(message)
            self.message.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)

    def manage_candidates_tab(self):
        try:
            self.sub_tab.manage_candidates()
            return True
        except Exception as error:
            ui_logger.error(error)

    def un_assign_room(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_un_assign_xpath, 'Un_assign_from_room')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ok_buttons(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_ok_button_xpath, 'un_assign_ok_buttons')
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def assign_room_action(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_assign_room_xpath, 'assign_room_action')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def room_name_field(self, room_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH,
                                                 self.__e_room_name_field_xpath, room_name, 'room_name_field')
            self.wait.drop_down_selection()
            return True
        except Exception as error:
            ui_logger.error(error)

    def room_assigning_action(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_assigning_room_xpath, 'room_assign')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def room_search_filed(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_room_search_filed_xpath, 'room_search_filed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_search_button_xpath, 'search_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def no_candidate_message(self, message):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.CLASS_NAME, self.__e_room_search_class, 'tag_room_search_candidate')
            if self.wait.text_value.strip() == message:
                print(f'No candidate tagged to room message - {self.wait.text_value}')
                self.driver.refresh()
                self.wait.loading()
                return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_info(self, candidate_name):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_candidate_info_xpath, 'candidate_info')
            if self.wait.text_value == candidate_name:
                print(f'Candidate name - {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)
