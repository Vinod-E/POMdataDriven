import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class PersonalDetailsData:

    __e_p_d_xpath = Locators.PLACEHOLDER['text_ph']
    __aadhar_id = Locators.MICROSITE['aadhar']
    __e_p_d_whatsapp_xpath = Locators.MICROSITE['whatsapp_consent']
    __first_name_id = Locators.MICROSITE['first_name']
    __middle_name_id = Locators.MICROSITE['middle_name']
    __last_name_id = Locators.MICROSITE['last_name']
    __photo_xpath = Locators.ATTACHMENT['multi_file'].format(1)
    __resume_xpath = Locators.ATTACHMENT['multi_file'].format(1)
    __pan_card_xpath = Locators.ATTACHMENT['multi_file'].format(1)
    __collegeId_xpath = Locators.ATTACHMENT['multi_file'].format(1)
    __Idcard_type_id = Locators.MICROSITE['card_type']
    __pan_number_id = Locators.MICROSITE['pan_number_filed']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def full_name(self, full_name):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('Full Name'),
                                                 full_name, 'full_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def first_name(self, first_name):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__first_name_id, first_name, 'first_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def middle_name(self, middle_name):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__middle_name_id, middle_name, 'middle_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def last_name(self, last_name):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__last_name_id, last_name, 'last_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def email_id(self, email):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('Email Id'),
                                                 email, 'email_id')
            return True
        except Exception as error:
            ui_logger.error(error)

    def mobile_number(self, mobile_number):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('MobileNumber'),
                                                 mobile_number, 'mobile_number')
            return True
        except Exception as error:
            ui_logger.error(error)

    def aadhar_number(self, aadhar_number):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__aadhar_id, aadhar_number, 'aadhar_number')
            return True
        except Exception as error:
            ui_logger.error(error)

    def usn_number(self, usn_number):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_xpath.format('USN'), usn_number, 'usn_number')
            return True
        except Exception as error:
            ui_logger.error(error)

    def whatsapp_consent(self, whatsapp_consent):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_p_d_whatsapp_xpath,
                                                 whatsapp_consent, 'whatsapp_consent')
            return True
        except Exception as error:
            ui_logger.error(error)

    def photo_upload(self, photo_upload):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__photo_xpath, photo_upload, 'photo_upload')
            self.wait.loading()
            time.sleep(1)
            return True
        except Exception as error:
            ui_logger.error(error)

    def resume_upload(self, resume_upload):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__resume_xpath, resume_upload, 'resume_upload')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def idcard_type(self, idcard_type):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__Idcard_type_id, idcard_type, 'idcard_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def idcard_upload(self, idcard_upload):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__pan_card_xpath, idcard_upload, 'idcard_upload')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def idcard_number(self, idcard_number):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__pan_number_id, idcard_number, 'idcard_number')
            return True
        except Exception as error:
            ui_logger.error(error)

    def college_id_upload(self, college_id_upload):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__collegeId_xpath,
                                                 college_id_upload, 'college_id_upload')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
