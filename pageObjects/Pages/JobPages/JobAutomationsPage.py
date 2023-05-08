import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.PageScroll import PageScroll
from utilities.uiNotifier import Notifier


class JobAutomations:
    __e_registration_stage_xpath = Locators.JOB['registration_hop']
    __e_eligibility_stage_xpath = Locators.JOB['eligibility_hop']
    __e_offer_stage_xpath = Locators.JOB['offer_stage']
    __e_hopping_stage_xpath = Locators.JOB['hop_stage_field']
    __e_hopping_status_xpath = Locators.JOB['hop_status_field']
    __e_toggle_buttons_xpath = Locators.JOB['toggle_buttons']
    __e_save_xpath = Locators.BUTTONS['button'].format('Save')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.notifier = Notifier(self.driver)

    def registration_stage(self):
        try:
            time.sleep(0.6)
            self.wait.web_element_wait_click(By.XPATH, self.__e_registration_stage_xpath, 'registration_stage')
            print('Clicked - On registration stage')
            return True
        except Exception as error:
            ui_logger.error(error)

    def eligibility_stage(self):
        try:
            time.sleep(0.6)
            self.wait.web_element_wait_click(By.XPATH, self.__e_eligibility_stage_xpath, 'eligibility_stage')
            print('Clicked - On eligibility stage')
            return True
        except Exception as error:
            ui_logger.error(error)

    def offer_stage(self):
        try:
            time.sleep(0.6)
            self.scroll.down(0, -300)
            self.wait.web_element_wait_click(By.XPATH, self.__e_offer_stage_xpath, 'offer_stage')
            print('Clicked - On offer stage')
            return True
        except Exception as error:
            ui_logger.error(error)

    def hop_stage(self, stage):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_hopping_stage_xpath,
                                                 stage, 'hop_stage')
            print('Select - Hopping stage')
            return True
        except Exception as error:
            ui_logger.error(error)

    def hop_status(self, status):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_hopping_status_xpath,
                                                 status, 'hop_status')
            print('Select - Hopping status')
            return True
        except Exception as error:
            ui_logger.error(error)

    def all_round_button_on(self):
        try:
            time.sleep(0.5)
            self.scroll.up(0, 100)
            a = [25, 30, 31, 32]  # ---25/30/31/32 are amsin toggles remain all are ams
            for i in a:
                self.wait.web_element_wait_click(By.XPATH, self.__e_toggle_buttons_xpath.format(i),
                                                 'all_round_button_on')
                print('Auto Tag to test - ON')
                print('Eligibility Criteria - ON')
                print('Self Schedule - ON')
            return True
        except Exception as error:
            ui_logger.error(error)

    def automation_save(self):
        try:
            time.sleep(0.5)
            self.scroll.down(0, -300)
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_xpath, 'automation_save')
            print('Job Automation Configuration - Save')
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_automation_save_notifier(self, message):
        try:
            time.sleep(0.7)
            self.notifier.glowing_messages(message)
            return True
        except Exception as error:
            ui_logger.error(error)

    def job_automations_notifier_dismiss(self):
        try:
            self.notifier.dismiss_message()
            return True
        except Exception as error:
            ui_logger.error(error)
