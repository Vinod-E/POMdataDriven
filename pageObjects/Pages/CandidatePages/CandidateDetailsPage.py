import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose
from utilities.PageScroll import PageScroll


class CandidateDetailsPage:
    __e_title_xpath = Locators.TITLE['title']
    __e_id_xpath = Locators.CANDIDATE['id']
    __e_certificate_xpath = Locators.CANDIDATE['certificates']
    __e_education_xpath = Locators.CANDIDATE['education']
    __e_candidate_float_action_class = Locators.ACTIONS['float_click_class']
    __e_manage_task_xpath = Locators.TITLE['title'].format('Manage Task')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)
        self.scroll = PageScroll(self.driver)

        self.candidate_id = ''

    def candidate_float_actions(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_candidate_float_action_class,
                                             'candidate_float_actions')
            print('Candidate details screen - floating action clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_manage_task_action(self, window_index):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_manage_task_xpath,
                                             'candidate_manage_task_action')
            print('Candidate details screen - floating action - Manage Task')
            time.sleep(1)
            self.window.switch_to_window(window_index)
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_status(self, changed_status):
        try:
            time.sleep(2)
            self.wait.loading()
            self.wait.web_element_wait_text(By.XPATH, self.__e_title_xpath.format(changed_status),
                                            f'Candidate_status_{changed_status}')
            if self.wait.text_value == changed_status:
                print(f'Candidate status changed - {self.wait.text_value}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def candidate_id_copy(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_id_xpath, 'candidate_id')
            self.candidate_id = self.wait.text_value
            print(f'candidate id - {self.candidate_id}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def certificates_details_check(self, certificate_name, index):
        try:
            time.sleep(2)
            self.wait.loading()
            self.scroll.down(0, 300)
            time.sleep(2)
            self.wait.web_element_wait_text(By.XPATH, self.__e_certificate_xpath.format(index),
                                            certificate_name)
            if certificate_name in self.wait.text_value.strip():
                print(f'Certificate name:: {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def education_details_check(self, education_type, index):
        try:
            time.sleep(1)
            self.wait.loading()
            self.scroll.down(0, 300)
            time.sleep(1)
            self.wait.web_element_wait_text(By.XPATH, self.__e_education_xpath.format(index),
                                            education_type)
            if education_type in self.wait.text_value.strip():
                print(f'Certificate name:: {self.wait.text_value}')
                return True
        except Exception as error:
            ui_logger.error(error)
