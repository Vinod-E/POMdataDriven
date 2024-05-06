import time
from pageObjects import Locators
from selenium.webdriver.common.by import By

from utilities import ReadConfigFile
from utilities.OpenNewTab import NewTab
from utilities.WebDriver_Wait import WebElementWait
from Listeners.logger_settings import ui_logger
from utilities.PageScroll import PageScroll


class CandidateLogin:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_tenant_name = Locators.LOGIN['alias']
    __e_login_name_l = Locators.LOGIN['c_user_name']
    __e_password_xpath = Locators.LOGIN['password']
    __e_login_button_class = Locators.LOGIN['login']
    __e_anchor_tag = Locators.TAG['anchor']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.new_tab = NewTab(self.driver)

    def candidate_login_url(self, server):
        if server == 'amsin':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_qa_candidate_url())
            return True
        elif server == 'ams':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_production_candidate_url())
            return True
        elif server == 'beta':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_beta_candidate_url())
            return True
        elif server == 'stage':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_stage_candidate_url())
            return True
        elif server == 'india':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_indiaams_candidate_url())
            return True

    def login_alias(self, login_alais):
        try:
            time.sleep(3)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_tenant_name, login_alais,
                                                 'login_alais_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_name(self, login_name):
        try:
            time.sleep(3)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_login_name_l, login_name, 'login_name_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def password(self, password):
        try:
            self.wait.web_element_wait_send_keys(By.XPATH, self.__e_password_xpath, password, 'login_password_field')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_button(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_login_button_class, 'login_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_account_name_verification(self, user_name):
        try:
            self.wait.candidate_login_loading()
            time.sleep(2)
            assert self.wait.web_elements_wait_text(By.TAG_NAME, self.__e_anchor_tag, user_name) == user_name, \
                'Logged in different account please check the details'
            print('Login Name verification done: ', user_name)
            return True
        except Exception as error:
            ui_logger.error(error)
