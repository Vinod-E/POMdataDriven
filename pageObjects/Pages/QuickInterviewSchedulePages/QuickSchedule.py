import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier


class QuickIntSchedulePage:
    __e_live_stage_xpath = Locators.LIVE_INTERVIEW['stage_selection']
    __e_interviewer_select_xpath = Locators.TITLE['title'].format('Interviewers')
    __e_interview_round_xpath = Locators.PLACEHOLDER['text_ph'].format('Select Interview Round')
    __e_comment_xpath = Locators.PLACEHOLDER['place_holder'].format('Your Comments')
    __e_schedule_xpath = Locators.BUTTONS['actionClicked'].format("'", 'scheduleInterview', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)

    def select_interviewers_field(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_interviewer_select_xpath, 'select_interviewers')
            print('Select interviewers - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_interviewer_round(self, stage_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_interview_round_xpath, stage_name,
                                                 'select_interviewers')
            self.wait.drop_down_selection()
            print(f'Select stage {stage_name} - Selected')
            return True
        except Exception as error:
            ui_logger.error(error)

    def quick_comment(self, comment):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_comment_xpath, comment,
                                                 'quick_comment')
            self.wait.drop_down_selection()
            print(f'Quick interview {comment} - Entered')
            return True
        except Exception as error:
            ui_logger.error(error)

    def schedule_quick_interview(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_schedule_xpath, 'Quick_schedule_interview')
            print('Quick interview - Scheduled')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def quick_schedule_notifier(self, message):
        try:
            time.sleep(0.5)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def quick_schedule_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            time.sleep(0.9)
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
