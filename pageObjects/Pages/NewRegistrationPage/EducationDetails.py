from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait
import time


class EducationalDetailsData:

    __e_pg_type_id = Locators.MICROSITE['pg_type']
    __e_pg_degree_id = Locators.MICROSITE['pg_degree']
    __e_pg_college_id = Locators.MICROSITE['pg_college']
    __e_pg_branch_id = Locators.MICROSITE['pg_branch']
    __e_pg_yop_id = Locators.MICROSITE['pg_yop']
    __e_pg_select_cgpa_id = Locators.MICROSITE['pg_cgpa_radio']
    __e_pg_cgpa_id = Locators.MICROSITE['pg_cgpa']
    __e_pg_cgpa_out_of_id = Locators.MICROSITE['pg_out_of']
    __e_ug_type_id = Locators.MICROSITE['ug_type']
    __e_ug_degree_id = Locators.MICROSITE['ug_degree']
    __e_ug_college_xpath = Locators.MICROSITE['ug_college']
    __e_ug_branch_id = Locators.MICROSITE['ug_branch']
    __e_ug_yop_id = Locators.MICROSITE['ug_yop']
    __e_ug_select_percent_id = Locators.MICROSITE['ug_percent_radio']
    __e_ug_percent_id = Locators.MICROSITE['ug_percent']
    __e_twelfth_type_id = Locators.MICROSITE['12th_type']
    __e_twelfth_yop_id = Locators.MICROSITE['12th_yop']
    __e_twelfth_select_cgpa_id = Locators.MICROSITE['12th_cgpa_radio']
    __e_twelfth_cgpa_id = Locators.MICROSITE['12th_cgpa']
    __e_tenth_type_id = Locators.MICROSITE['10th_type']
    __e_tenth_yop_id = Locators.MICROSITE['10th_yop']
    __e_tenth_select_percent_id = Locators.MICROSITE['10th_percent_radio']
    __e_tenth_percent_id = Locators.MICROSITE['10th_percent']
    __e_add_educ_xpath = Locators.BUTTONS['btnActionClicked'].format("'", 'addProfile', "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def add_more_education(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_add_educ_xpath, 'add_more_education')
            return True
        except Exception as error:
            ui_logger.error(error)

# ---------------------------- PG Details ------------------------------------------------
    def pg_education_type(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_type_id, value, 'pg_education_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_degree(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_degree_id, value, 'pg_degree')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_college(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_college_id, value, 'pg_college')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_branch(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_branch_id, value, 'pg_branch')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_yop(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_yop_id, value, 'pg_yop')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_select_cgpa(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_pg_select_cgpa_id, 'pg_select_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_cgpa(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_cgpa_id, value, 'pg_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pg_cgpa_out_of(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_pg_cgpa_out_of_id, value, 'pg_cgpa_out_of')
            return True
        except Exception as error:
            ui_logger.error(error)

# ---------------------------- UG Details ------------------------------------------------
    def ug_education_type(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_ug_type_id, value, 'ug_education_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_degree(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_ug_degree_id, value, 'ug_degree')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_college(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_ug_college_xpath, value, 'ug_college')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_branch(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_ug_branch_id, value, 'ug_branch')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_yop(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_ug_yop_id, value, 'ug_yop')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_select_percent(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_ug_select_percent_id, 'ug_select_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

    def ug_percent(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_ug_percent_id, value, 'ug_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

# ---------------------------- Twelfth Details ------------------------------------------------
    def twelfth_education_type(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_twelfth_type_id, value, 'twelfth_education_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def twelfth_yop(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_twelfth_yop_id, value, 'twelfth_yop')
            return True
        except Exception as error:
            ui_logger.error(error)

    def twelfth_select_cgpa(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_twelfth_select_cgpa_id, 'twelfth_select_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

    def twelfth_cgpa(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_twelfth_cgpa_id, value, 'twelfth_cgpa')
            return True
        except Exception as error:
            ui_logger.error(error)

# ---------------------------- Tenth Details ------------------------------------------------
    def tenth_education_type(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_tenth_type_id, value, 'tenth_education_type')
            return True
        except Exception as error:
            ui_logger.error(error)

    def tenth_yop(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_tenth_yop_id, value, 'tenth_yop')
            return True
        except Exception as error:
            ui_logger.error(error)

    def tenth_select_percent(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__e_tenth_select_percent_id, 'tenth_select_percent')
            return True
        except Exception as error:
            ui_logger.error(error)

    def tenth_percent(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_tenth_percent_id, value, 'tenth_percent')
            return True
        except Exception as error:
            ui_logger.error(error)
