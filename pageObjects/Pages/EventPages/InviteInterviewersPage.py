import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventMangeInterviewersPage:
    __e_add_criteria_xpath = Locators.BUTTONS['add_criteria']
    __e_panel_entry_xpath = Locators.NOMINATIONS['panel_1']
    __e_panel2_entry_xpath = Locators.NOMINATIONS['panel_2']
    __e_skill1_search_xpath = Locators.BUTTONS['nomination_int_search']
    __e_skill2_search_xpath = Locators.NOMINATIONS['search']
    __e_skill1_required_int_xpath = Locators.NOMINATIONS['skill1_int']
    __e_skill2_required_int_xpath = Locators.NOMINATIONS['skill2_int']
    __e_skill1_required_nom_xpath = Locators.NOMINATIONS['skill1_nom']
    __e_skill2_required_nom_xpath = Locators.NOMINATIONS['skill2_nom']
    __e_send_mail_xpath = Locators.BUTTONS['nomination_mail']
    __e_confirm_button_xpath = Locators.BUTTONS['all_buttons'].format('OK')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def add_criteria(self):
        try:
            time.sleep(1.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_add_criteria_xpath, 'add_criteria')
            print('Add new criteria - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def panel_skill1_select(self, panel):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_panel_entry_xpath,
                                                 panel, 'panel_skill1_select')
            self.wait.drop_down_selection()
            print('Skill-1 to panel - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def panel_skill2_select(self, panel):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_panel2_entry_xpath,
                                                 panel, 'panel_skill2_select')
            self.wait.drop_down_selection()
            print('Skill-2 to panel - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_skill1_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_skill1_search_xpath, 'search_skill1_interviewers')
            print('Skill-1 interviewers - Searched')
            return True
        except Exception as error:
            ui_logger.error(error)

    def search_skill2_interviewers(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_skill2_search_xpath, 'search_skill2_interviewers')
            print('Skill-2 interviewers - Searched')
            return True
        except Exception as error:
            ui_logger.error(error)

    def skill1_required_interviewers(self, count):
        try:
            self.wait.clear(By.XPATH, self.__e_skill1_required_int_xpath, 'skill1_required_int')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_skill1_required_int_xpath, count,
                                                 'search_skill2_interviewers')
            print('Skill-1 interviewers count - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def skill2_required_interviewers(self, count):
        try:
            self.wait.clear(By.XPATH, self.__e_skill2_required_int_xpath, 'skill2_required_int')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_skill2_required_int_xpath, count,
                                                 'search_skill2_interviewers')
            print('Skill-2 interviewers count - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def skill1_required_nomination(self, count):
        try:
            self.wait.clear(By.XPATH, self.__e_skill1_required_nom_xpath, 'skill1_required_nomination')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_skill1_required_nom_xpath, count,
                                                 'search_skill2_interviewers')
            print('Skill-1 nominations count - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def skill2_required_nomination(self, count):
        try:
            self.wait.clear(By.XPATH, self.__e_skill2_required_nom_xpath, 'skill2_required_nomination')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_skill2_required_nom_xpath, count,
                                                 'search_skill2_interviewers')
            print('Skill-2 nominations count - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def send_mail_interviewers(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_send_mail_xpath, 'send_mail_interviewers')
            print('Send mail to interviewers - Sent')
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_button(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_confirm_button_xpath, 'send_mail_interviewers')
            print('Ok confirmation - Confirmed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def criteria_notifier(self, message):
        try:
            self.wait.loading()
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def criteria_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            self.wait.loading()
            self.scroll.up(0, 70)
            return True
        except Exception as error:
            ui_logger.error(error)
