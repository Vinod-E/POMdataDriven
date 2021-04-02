from pageObjects import Locators
from selenium.webdriver.common.by import By
from utilities.WebDriver_Wait import WebElementWait


class Menu:
    __e_menu = Locators.MENU['menu']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebElementWait(self.driver)

    def job_tab(self, job_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(job_menu_name), 'not_in_job_roles')

    def requirement_tab(self, req_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(req_menu_name), 'not_in_Requirements')

    def assessment_tab(self, assess_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(assess_menu_name), 'not_in_assessments')

    def event_tab(self, event_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(event_menu_name), 'not_in_Events')

    def more_tab(self, more_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(more_menu_name), 'not_in_More')

    def embrace_tab(self, embrace_menu_name):
        self.wait.web_element_wait_click(By.XPATH, self.__e_menu.format(embrace_menu_name), 'not_in_Embrace')
