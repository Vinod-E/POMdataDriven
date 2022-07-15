import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class CertificateDetailsData:

    __e_certi_type_xpath = Locators.MICROSITE['certificationType']
    __e_certi_name_xpath = Locators.MICROSITE['certificateName']
    __e_certi_status_xpath = Locators.MICROSITE['certificateStatus']
    __e_institute_xpath = Locators.MICROSITE['institute']
    __e_from_month_xpath = Locators.MICROSITE['from_month']
    __e_to_month_xpath = Locators.MICROSITE['to_month']
    __e_from_year_xpath = Locators.MICROSITE['from_year']
    __e_to_year_xpath = Locators.MICROSITE['to_year']
    __e_attempts_xpath = Locators.MICROSITE['text_ph']
    __e_file_path = Locators.ATTACHMENT['multi_file'].format(1)
    __e_file2_path = Locators.ATTACHMENT['multi_file'].format(1)
    __e_add_certi_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'addCertification', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def certificate_type(self, c_type, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_certi_type_xpath.format(index)
                                                 , c_type, 'certificate_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def certificate_name(self, c_name, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_certi_name_xpath.format(index),
                                                 c_name, 'certificate_name')
            return True
        except Exception as error:
            ui_logger.error(error)

    def certificate_status(self, c_status, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_certi_status_xpath.format(index),
                                                 c_status, 'certificate_status')
            return True
        except Exception as error:
            ui_logger.error(error)

    def certificate_institute(self, c_institute, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_institute_xpath.format(index),
                                                 c_institute, 'certificate_institute')
            return True
        except Exception as error:
            ui_logger.error(error)

    def no_of_attempts(self, attempts, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_attempts_xpath.format(index),
                                                 attempts, 'no_of_attempts')
            return True
        except Exception as error:
            ui_logger.error(error)

    def from_month(self, month, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_from_month_xpath.format(index),
                                                 month, 'from_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def to_month(self, month, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_to_month_xpath.format(index),
                                                 month, 'to_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def from_year(self, year, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_from_year_xpath.format(index),
                                                 year, 'from_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def to_year(self, year, index):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_to_year_xpath.format(index),
                                                 year, 'to_month')
            return True
        except Exception as error:
            ui_logger.error(error)

    def choose_file(self, file_path):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_file_path, file_path, 'Job_attachment')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def choose_file2(self, file_path):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_file2_path, file_path, 'Job_attachment')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def add_certificate(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_add_certi_xpath, 'add_certificate')
            return True
        except Exception as error:
            ui_logger.error(error)
