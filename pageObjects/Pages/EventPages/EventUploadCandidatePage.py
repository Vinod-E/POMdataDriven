import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait
from utilities.uiNotifier import Notifier
from utilities.PageScroll import PageScroll


class EventUploadCandidate:

    __e_upload_xpath = Locators.ATTACHMENT['file']
    __e_next_button_xpath = Locators.BUTTONS['button'].format('Next')
    __e_declare_xpath = Locators.CHECKBOX['type']
    __e_signature_xpath = Locators.CANDIDATE['upload_signature']
    __e_agree_xpath = Locators.BUTTONS['button'].format('I Agree')
    __e_edit_info_xpath = Locators.TITLE['title'].format('Edit')
    __e_name_xpath = Locators.CANDIDATE['name_field']
    __e_email_xpath = Locators.CANDIDATE['email_field']
    __e_usn_xpath = Locators.CANDIDATE['usn_field']
    __e_save_button_xpath = Locators.CANDIDATE['save_info']
    __e_save_candidate_xpath = Locators.CANDIDATE['save']
    __e_upload_count_css = Locators.CANDIDATE['Upload_count']
    __e_close_button_xpath = Locators.BUTTONS['button'].format('Close')
    __e_close_main_xpath = Locators.BUTTONS['all_buttons'].format('Close')
    __e_confirm_close_main_xpath = Locators.BUTTONS['all_buttons'].format('OK')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.notifier = Notifier(self.driver)
        self.scroll = PageScroll(self.driver)

    def upload_file(self, upload_file):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_upload_xpath, upload_file,
                                                 'upload_file')
            print('Candidate excel sheet - Uploading')
            self.wait.uploading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def next_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_next_button_xpath, 'upload_file')
            print('Candidate scree next button - Clicked')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def declare_check(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_declare_xpath, 'declare_check')
            print('Declare Check - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def signature_entry(self):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_signature_xpath, 'VinodKumar',
                                                 'signature_entry')
            print('Signature Entry - Signed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def agreed_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_agree_xpath, 'agreed_button')
            print('Agreed Button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def edit_excel_information(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_edit_info_xpath, 'edit_excel_information')
            print('Edit Information button - Clicked')
            return True
        except Exception as error:
            ui_logger.error(error)

    def name_edit(self, candidate_name):
        try:
            self.wait.clear(By.XPATH, self.__e_name_xpath, 'Name_field_clear')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_name_xpath, candidate_name,
                                                 'name_edit')
            print('Name information - Changed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def email_edit(self, candidate_email):
        try:
            self.wait.clear(By.XPATH, self.__e_email_xpath, 'Name_field_clear')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_email_xpath, candidate_email,
                                                 'email_edit')
            print('Email information - Changed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def usn_edit(self, usn_email):
        try:
            self.wait.clear(By.XPATH, self.__e_usn_xpath, 'Name_field_clear')
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_usn_xpath, usn_email,
                                                 'email_edit')
            print('Usn information - Changed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_info(self):
        try:
            self.scroll.down(0, -50)
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_button_xpath, 'save_info')
            print('Save information - Saved')
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_candidate(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_click(By.XPATH, self.__e_save_candidate_xpath, 'save_candidate')
            print('Save Candidate - Saved')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def success_upload(self, message):
        try:
            time.sleep(3)
            self.wait.web_element_wait_text(By.CSS_SELECTOR, self.__e_upload_count_css, 'success_upload')
            if self.wait.text_value.strip() == message:
                print(f'Success {self.wait.text_value.strip()} - Count')
                return True
            else:
                print(f'Failed {self.wait.text_value.strip()} - Count')
        except Exception as error:
            ui_logger.error(error)

    def close_candidate_screen(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_close_button_xpath, 'close_candidate_screen')
            print('Close Candidate Screen - Closed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def close_main_screen(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_close_main_xpath, 'close_main_screen')
            print('Close Main Screen - Closed')
            return True
        except Exception as error:
            ui_logger.error(error)

    def confirm_close_main_screen(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_confirm_close_main_xpath, 'confirm_close_main_screen')
            print('Confirm Close Main Screen - Closed')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
