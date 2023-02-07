from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class AadharPageDetails:

    __generate_otp_xpath = Locators.BUTTONS['btnActionClicked'].format("'", "requestAadhaarOtp", "'")
    __submit_opt_xpath = Locators.BUTTONS['btnActionClicked'].format("'", "submitAadhaarOtp", "'")
    __proceed_xpath = Locators.BUTTONS['btnActionClicked'].format("'", "proceed", "'")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def generate_aadhar_otp(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__generate_otp_xpath, 'generate_aadhar_otp')
            input('Please Enter OTP, And click Enter Key')
            return True
        except Exception as error:
            ui_logger.error(error)

    def enter_aadhar_otp(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__submit_opt_xpath, 'enter_aadhar_otp')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def proceed_with_aadhar_verify(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__proceed_xpath, 'proceed_with_aadhar_verify')
            return True
        except Exception as error:
            ui_logger.error(error)
