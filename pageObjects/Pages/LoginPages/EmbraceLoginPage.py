import time
from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities import ReadConfigFile
from utilities.OpenNewTab import NewTab
from utilities.WebDriver_Wait import WebElementWait
from Listeners.logger_settings import ui_logger
from utilities.PageScroll import PageScroll


class EmbraceLogin:
    """
    ----------------- WEB ELEMENT REFERENCE CLASS PRIVATE VARIABLES TO EASY ACCESS ------>>>>
    """
    __e_login_name = Locators.LOGIN['c_user_name']
    __e_password_xpath = Locators.LOGIN['password']
    __e_login_button_xpath = Locators.LOGIN['e_login']
    __e_login_verify_name = 'headerNameText'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)
        self.new_tab = NewTab(self.driver)

    def embrace_url(self, server):
        if server == 'amsin':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_qa_embrace_url())
            return True
        elif server == 'ams':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_production_embrace_url())
            return True
        elif server == 'beta':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_beta_embrace_url())
            return True
        elif server == 'stage':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_stage_embrace_url())
            return True
        elif server == 'india':
            self.new_tab.open_in_same_tab(0, ReadConfigFile.ReadConfig.get_indiaams_embrace_url())
            return True

    def login_name(self, login_name):
        try:
            time.sleep(3)
            self.wait.web_element_wait_send_keys(By.NAME, self.__e_login_name, login_name, 'login_name_field')
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
            self.wait.web_element_wait_click(By.XPATH, self.__e_login_button_xpath, 'login_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def login_account_name_verification(self, user_name):
        try:
            self.wait.embrace_loading()
            assert self.wait.web_elements_wait_text(By.CLASS_NAME, self.__e_login_verify_name, user_name) == \
                   user_name, 'Logged in different account please check the details'
            print(f'{user_name} logged in successfully')
            return True
        except Exception as error:
            ui_logger.error(error)
