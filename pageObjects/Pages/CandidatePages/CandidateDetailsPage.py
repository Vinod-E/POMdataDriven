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
    __e_aadhar_number_xpath = Locators.CANDIDATE['aadhar_number']
    __e_certificate_xpath = Locators.CANDIDATE['certificates']
    __e_education_xpath = Locators.CANDIDATE['education']
    __e_candidate_float_action_class = Locators.ACTIONS['float_click_class']
    __e_manage_task_xpath = Locators.TITLE['title'].format('Manage Task')
    __e_photo_title_xpath = Locators.TITLE['title'].format('Edit photo')
    __e_pan_xpath = Locators.CANDIDATE['other_attachments'].format(1)
    __e_college_xpath = Locators.CANDIDATE['other_attachments'].format(2)
    __e_communication_xpath = Locators.SUB_MENU['candidate_communication']
    __e_payment_xpath = Locators.SUB_MENU['candidate_payment']
    __e_arrow_xpath = Locators.CANDIDATE['down_arrow']
    __e_id_card_xpath = Locators.CANDIDATE['id_card_verified']
    __e_aadhar_xpath = Locators.CANDIDATE['aadhar_verified']
    __e_order_id_xpath = Locators.CANDIDATE['payment_details_by_index'].format(2)
    __e_pay_id_xpath = Locators.CANDIDATE['payment_details_by_index'].format(3)
    __e_pay_completed_xpath = Locators.CANDIDATE['payment_details_by_index'].format(4)
    __e_pay_capture_xpath = Locators.CANDIDATE['payment_details_by_index'].format(5)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.window = SwitchWindowClose(self.driver)
        self.scroll = PageScroll(self.driver)

        self.candidate_id = ''
        self.aadhar_number = ''

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
            time.sleep(1)
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

    def aadhar_numbers(self, aadhar):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_aadhar_number_xpath, 'aadhar_number')
            self.aadhar_number = self.wait.text_value
            print(f'Candidate Aadhar Number - {self.aadhar_number}')
            if int(self.aadhar_number) == int(aadhar):
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

    def profile_photo_check(self):
        try:
            time.sleep(2)
            self.wait.loading()
            self.wait.web_element_wait(By.XPATH, self.__e_photo_title_xpath, 'profile_photo_check')
            photo = self.wait.perform.get_attribute("src")
            print(f'Photo s3 url:: {photo}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def pan_photo_check(self):
        try:
            time.sleep(1)
            self.scroll.up(0, 200)
            self.wait.web_element_wait(By.XPATH, self.__e_pan_xpath, 'pan_photo_check')
            pan = self.wait.perform.get_attribute("href")
            print(f'PAN s3 url:: {pan}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def college_id_photo_check(self):
        try:
            self.wait.web_element_wait(By.XPATH, self.__e_college_xpath, 'college_id_photo_check')
            college = self.wait.perform.get_attribute("href")
            print(f'College Id s3 url:: {college}')
            return True
        except Exception as error:
            ui_logger.error(error)

    def communication_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_communication_xpath, 'communication_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def payment_tab(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_payment_xpath, 'payment_tab')
            return True
        except Exception as error:
            ui_logger.error(error)

    def arrow_down(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_arrow_xpath, 'arrow_down')
            return True
        except Exception as error:
            ui_logger.error(error)

    def aadhar_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_aadhar_xpath, 'aadhar_verified')
            if self.wait.text_value.strip() == 'Aadhaar Verification':
                print(f'Communication status - {self.wait.text_value.strip()} ::  Aadhaar validated')
                return True
        except Exception as error:
            ui_logger.error(error)

    def id_card_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_id_card_xpath, 'id_card_verified')
            if self.wait.text_value.strip() == 'Id-Card Verified':
                print(f'Communication status - {self.wait.text_value.strip()} ::  True')
                return True
        except Exception as error:
            ui_logger.error(error)

    def order_id_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_order_id_xpath, 'order_id_verified')
            if "order" in self.wait.text_value.strip():
                print(f'Order Id - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def payment_id_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_pay_id_xpath, 'payment_id_verified')
            if "pay" in self.wait.text_value.strip():
                print(f'Payment Id - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def payment_completed_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_pay_completed_xpath, 'payment_completed_verified')
            if self.wait.text_value.strip() == "Yes":
                print(f'Payment Completed - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)

    def payment_captured_verified(self):
        try:
            self.wait.web_element_wait_text(By.XPATH, self.__e_pay_capture_xpath, 'payment_captured_verified')
            if self.wait.text_value.strip() == "Yes":
                print(f'Payment Captured - {self.wait.text_value.strip()}')
                return True
        except Exception as error:
            ui_logger.error(error)
