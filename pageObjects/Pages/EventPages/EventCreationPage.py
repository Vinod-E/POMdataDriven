import time

from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventCreation:

    __e_new_event_xpath = Locators.BUTTONS['create']
    __e_event_name_xpath = Locators.PLACEHOLDER['text_ph'].format('Name')
    __e_event_req_name_xpath = Locators.PLACEHOLDER['text_ph'].format('Requirement')
    __e_event_job_xpath = Locators.TITLE['title'].format('Job Roles')
    __e_event_slot_xpath = Locators.PLACEHOLDER['text_ph'].format('Slot')
    __e_event_from_date_xpath = Locators.PLACEHOLDER['place_holder'].format('From')
    __e_event_to_date_xpath = Locators.PLACEHOLDER['place_holder'].format('To')
    __e_event_report_date_xpath = Locators.PLACEHOLDER['place_holder'].format('Reporting Date')
    __e_event_manager_xpath = Locators.PLACEHOLDER['place_holder'].format('Event Manager')
    __e_event_college_xpath = Locators.PLACEHOLDER['place_holder'].format('College')
    __e_event_ec_css = Locators.BUTTONS['radio']
    __e_event_create_xpath = Locators.BUTTONS['actionClicked'].format("'", 'create', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def new_event_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_new_event_xpath, 'new_event_button')
            print('New event creation button - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_name_field(self, event_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_name_xpath, event_name,
                                                 'event_name_field')
            print(f'New event name - {event_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_req_field(self, req_name):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_req_name_xpath, req_name,
                                                 'event_req_field')
            time.sleep(1)
            self.wait.drop_down_selection()
            self.wait.loading()
            print(f'New event req name - {req_name} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_job_field(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_job_xpath, 'event_job_field')
            print('Event job field - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_slot_field(self, slot):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_slot_xpath, slot,
                                                 'event_slot_field')
            self.wait.drop_down_selection()
            print(f'New event slot - {slot} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_from_date(self, from_date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_from_date_xpath, from_date,
                                                 'event_from_date')
            print(f'New Event from date - {from_date} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_to_date(self, to_date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_to_date_xpath, to_date,
                                                 'event_to_date')
            print(f'New Event to date - {to_date} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_report_date(self, report_date):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_report_date_xpath, report_date,
                                                 'event_to_date')
            print(f'New Event reporting date - {report_date} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_manager_field(self, event_manager):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_manager_xpath, event_manager,
                                                 'event_manager_field')
            self.wait.drop_down_selection()
            print(f'Event manager name - {event_manager} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_college_field(self, college):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_event_college_xpath, college,
                                                 'event_college_field')
            self.wait.drop_down_selection()
            print(f'Event college name - {college} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_ec_enable(self):
        try:
            self.scroll.down(0, -50)
            time.sleep(0.6)
            button = ' Enable'
            self.wait.web_elements_wait_multiple_click(By.CSS_SELECTOR, self.__e_event_ec_css, button)
            print(f'Event Ec - {button} - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_create_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_event_create_xpath, 'event_create_button')
            self.wait.drop_down_selection()
            print('Event Create button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_create_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def event_create_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.9)
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

