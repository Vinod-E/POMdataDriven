import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose


class RazorPayPageDetails:

    __r_candidate_name_id = Locators.MICROSITE['razorpay_c_name']
    __r_qr_code_xpath = Locators.MICROSITE['Qr_code']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.iframe = SwitchWindowClose(self.driver)

    def merchant_name(self, first_name):
        try:
            time.sleep(5)
            self.iframe.switch_to_iframe('//iframe[@class="razorpay-checkout-frame"]')
            self.wait.web_element_wait_text(By.ID, self.__r_candidate_name_id, 'razorpay_candidate_name')
            if self.wait.text_value.strip() == first_name:
                print(f'Razorpay Merchant Name:: {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def qrcode(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__r_qr_code_xpath, 'qrcode')
            time.sleep(3)
            return True
        except Exception as error:
            ui_logger.error(error)
