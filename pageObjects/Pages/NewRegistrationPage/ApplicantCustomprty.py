import time

from Listeners.logger_settings import ui_logger
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait


class ApplicantCustomPropertyData:
    __e_rate_id = 'iPython(Rateyourself)'
    __e_textarea_xpath = '//textarea[@placeholder="Write About Your Python Experience"]'
    __e_boolean_xpath = '//label[@for="bExperienceInseleniumtrue"]'
    __e_date_id = 'dDateOfCertification'
    __e_institute_id = 'sInstituteName'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def rating_dropdown(self, text_rating):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_rate_id,
                                                 text_rating, 'rating_dropdown')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def writeabout_field(self, textarea_value):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_textarea_xpath,
                                                 textarea_value, 'writeabout_field')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def selenium_boolean(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_boolean_xpath, 'selenium_boolean')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def date_field(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_date_id, value, 'date_field')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)

    def institute_field(self, value):
        try:
            self.wait.web_element_wait_send_keys(By.ID, self.__e_institute_id, value, 'institute_field')
            time.sleep(0.5)
            return True
        except Exception as error:
            ui_logger.error(error)
