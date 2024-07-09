import time
from utilities import PageScroll
from pageObjects import Locators
from selenium.webdriver.common.by import By
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class AssessmentSlot:
    __e_job_filter_xpath = '//input[@placeholder="Event Related Jobs"]'
    __e_stage_filter_xpath = '//input[@placeholder="Status"]'
    __e_go_button_xpath = ('//button[@ng-click="vm.actionClicked({}{}{})"]'
                           .format("'", 'fetchApplicantSlotSummary', "'"))
    __e_check_box_xpath = '//input[@ng-model="vm.isAllSelected"]'
    __e_unassign_slot_xpath = '//span[@title="Unassign Slot"]'
    __e_unassign_slot_name_xpath = '//input[@placeholder="slots"]'
    __e_unassign_button_xpath = ('//button[@ng-click="vm.actionClicked({}{}{},data);"]'
                                 .format("'", "unAssign", "'"))

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.page_scroll = PageScroll.PageScroll(self.driver)

        self.candidate_login_link = ''

    def job_filters(self, job_name):
        try:
            self.wait.loading()
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_job_filter_xpath, job_name,
                                                 'job_filters')
            self.wait.drop_down_selection()
            return True
        except Exception as error:
            ui_logger.error(error)

    def stage_filter(self, stage):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_stage_filter_xpath, stage,
                                                 'stage_filter')
            self.wait.drop_down_selection()
            return True
        except Exception as error:
            ui_logger.error(error)

    def go_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_go_button_xpath, 'go_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)

    def check_box(self):
        try:
            time.sleep(2)
            self.page_scroll.down(0, 200)
            self.wait.web_element_wait_click(By.XPATH, self.__e_check_box_xpath, 'check_box')
            return True
        except Exception as error:
            ui_logger.error(error)

    def un_assign_slot_icon(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_unassign_slot_xpath, 'un_assign_slot')
            return True
        except Exception as error:
            ui_logger.error(error)

    def select_slot_to_unassign(self, slot):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_unassign_slot_name_xpath, slot,
                                                 'select_slot_to_unassign')
            time.sleep(5)
            self.wait.drop_down_selection()
            return True
        except Exception as error:
            ui_logger.error(error)

    def unassign_button(self):
        try:
            self.wait.web_element_wait_click(By.XPATH, self.__e_unassign_button_xpath,
                                             'unassign_button')
            self.wait.loading()
            return True
        except Exception as error:
            ui_logger.error(error)
