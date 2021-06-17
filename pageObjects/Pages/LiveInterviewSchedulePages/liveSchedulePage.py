import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose
from utilities.uiNotifier import Notifier


class LiveIntSchedulePage:
    __e_live_stage_xpath = Locators.LIVE_INTERVIEW['stage_selection']
    __e_live_app_xpath = Locators.PLACEHOLDER['text_ph'].format('Candidate Name')
    __e_live_search_app_xpath = Locators.LIVE_INTERVIEW['app_search']
    __e_live_clear_search_app_xpath = Locators.LIVE_INTERVIEW['clear_search']
    __e_check_xpath = Locators.CHECKBOX['type']
    __e_validate_class = Locators.LIVE_INTERVIEW['int_screen']
    __e_select_int_xpath = Locators.LIVE_INTERVIEW['select_int']
    __e_live_schedule_select_xpath = Locators.BUTTONS['button'].format('Schedule Selected')
    __e_live_schedule_xpath = Locators.BUTTONS['button'].format(' Schedule')
    __e_arrow_down_class = Locators.LIVE_INTERVIEW['arrow_down']
    __e_feedback_action_xpath = Locators.LIVE_INTERVIEW['feedback_button']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

    def stage_selection(self, stage_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_live_stage_xpath,
                                                 stage_name, 'job_int_panel')
            print(f'{stage_name} - Selected from available stages')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def applicant_name_filed(self, applicant_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_live_app_xpath,
                                                 applicant_name, 'applicant_name_filed')
            print(f'Applicant name {applicant_name} - Entered')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def schedule_applicant_search(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_live_search_app_xpath, 'schedule_applicant_search')
            print('schedule applicant - searched')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def clear_applicant_search(self):
        try:
            time.sleep(0.7)
            self.wait.web_element_wait_click(By.XPATH, self.__e_live_clear_search_app_xpath, 'clear_applicant_search')
            print('clear applicant - searched')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_live_applicant(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_check_xpath, 'Applicant_check_box')
            print('Applicant got - selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def schedule_select(self):
        try:
            time.sleep(2)
            self.wait.web_element_wait_click(By.XPATH, self.__e_live_schedule_select_xpath, 'schedule_select')
            self.wait.loading()
            print('schedule_select button - selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def validate_interviewers_screen(self, screen_name):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_text(By.CLASS_NAME, self.__e_validate_class, 'validate_interviewers_screen')
            if screen_name in self.wait.text_value.strip():
                print(f'Screen name {screen_name} - validating')
                return True
        except Exception as error:
            ui_logger.error(error)

    def select_interviewers(self):
        try:
            time.sleep(1)
            self.wait.web_elements_wait_click(By.XPATH, self.__e_select_int_xpath, '')
            print('select_interviewers - selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def live_schedule(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.XPATH, self.__e_live_schedule_xpath, 'live_schedule')
            self.wait.loading()
            print('Live schedule - selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def live_schedule_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def live_schedule_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.9)
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def arrow_down_for_feedback(self):
        try:
            time.sleep(0.5)
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_arrow_down_class, 'arrow_down_for_feedback')
            self.wait.loading()
            print('Arrow down for feedback- Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def feedback_provide_action(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_feedback_action_xpath, 'feedback_provide_action')
            print('Provide feedback Action - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)
