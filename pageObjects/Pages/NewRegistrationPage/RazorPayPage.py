import time

from Listeners.logger_settings import ui_logger
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from utilities.WebDriver_Wait import WebElementWait
from utilities.SwitchWindow import SwitchWindowClose


class RazorPayPageDetails:

    __r_candidate_name_xpath = Locators.TITLE['title']
    __r_qr_code_xpath = Locators.MICROSITE['Qr_code']
    __r_wallet_xpath = '//*[@slot="title"]'
    __r_phonepe_xpath = '//*[@class="title"]'
    __r_payment_id = 'redesign-v15-cta'
    __r_success_class = 'success'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.iframe = SwitchWindowClose(self.driver)

    def merchant_name(self, first_name):
        try:
            time.sleep(5)
            self.iframe.switch_to_iframe('//iframe[@class="razorpay-checkout-frame"]')
            time.sleep(2)
            self.wait.web_element_wait_text(By.XPATH, self.__r_candidate_name_xpath.format(first_name),
                                            'razorpay_candidate_name')
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

    def wallet(self):
        try:
            self.wait.web_elements_wait_click(By.XPATH, self.__r_wallet_xpath, 'Wallet')
            print('Wallet Selected to Complete the Order')
            return True
        except Exception as error:
            ui_logger.error(error)

    def phonepe(self):
        try:
            self.wait.web_elements_wait_click(By.XPATH, self.__r_phonepe_xpath, 'PhonePe')
            print('Paying through PhonePe')
            return True
        except Exception as error:
            ui_logger.error(error)

    def payment(self):
        try:
            self.wait.web_element_wait_click(By.ID, self.__r_payment_id, 'payment')
            print('Paying amount - 1 rupee')
            time.sleep(2)
            return True
        except Exception as error:
            ui_logger.error(error)

    def payment_success(self):
        try:
            self.iframe.switch_to_window(1)
            print('New window for making payment success')
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__r_success_class, 'payment_success')
            self.iframe.switch_to_window(0)
            print('Back to registration form window')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
