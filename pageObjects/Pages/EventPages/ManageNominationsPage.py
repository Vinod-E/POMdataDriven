import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventNominationsPage:
    __e_nomination_tab_xpath = Locators.SUB_MENU['nominations']
    __e_header_tag = Locators.TAG['h5']
    __e_panel_xpath = Locators.NOMINATIONS['panel_select']
    __e_check_xpath = Locators.CHECK_BOX['check_box']
    __e_action_class = Locators.NOMINATIONS['actions']
    __e_approve_xpath = Locators.NOMINATIONS['approve']
    __e_sync_xpath = Locators.TITLE['title'].format('This will sync interviewers for whom you'
                                                    ' have accepted nomination with the event owners')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def nomination_tab(self):
        try:
            self.wait.loading()
            self.wait.web_element_wait_click(By.XPATH, self.__e_nomination_tab_xpath, 'nomination_tab')
            print('Interviewers nomination_tab - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def header_check(self, header):
        try:
            self.wait.loading()
            assert self.wait.web_elements_wait_text(By.TAG_NAME, self.__e_header_tag, header) == header, \
                'no header found'
            return True
        except Exception as error:
            ui_logger.error(error)

    def panel_select(self, skill):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_panel_xpath, skill, 'panel_select')
            self.wait.loading()
            print(f'{skill} - skill selected to panel')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_applicants(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_check_xpath, 'select_applicants')
            print('select_applicants - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def recruiter_actions(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_action_class, 'recruiter_actions')
            print('recruiter_actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def approve_by_recruiter(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_approve_xpath, 'recruiter_actions')
            self.wait.loading()
            print('recruiter_actions - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def sync_interviewers(self):
        try:
            self.scroll.up(0, 90)
            self.wait.web_element_wait_click(By.XPATH, self.__e_sync_xpath, 'sync_interviewers')
            print('sync_interviewers - Synced')
            return True
        except Exception as error:
            ui_logger.error(error)

    def sync_notifier(self, message):
        try:
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def sync_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)
