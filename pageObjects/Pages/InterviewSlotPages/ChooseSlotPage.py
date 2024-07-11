import time
from selenium.webdriver.common.by import By
from utilities.PageScroll import PageScroll
from Listeners.logger_settings import ui_logger
from utilities.WebDriver_Wait import WebElementWait


class ChooseSlot:
    __e_slot_class = 'slotButton'
    __e_save_button_class = 'btn-save'
    __e_success_h = 'h2'
    __e_thank_you_screen_xpath = '/html/body/hp-root/div/div[2]/hp-slots/div/div/section[2]/div/div/div/div/span'

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebElementWait(self.driver)
        self.scroll = PageScroll(self.driver)

    def slot_selection(self, slot):
        try:
            time.sleep(2)
            a = self.wait.web_elements_wait_click(By.CLASS_NAME, self.__e_slot_class, slot)
            print('Slot Time selected:: ', a)
            return True
        except Exception as error:
            ui_logger.error(error)

    def save_button(self):
        try:
            self.wait.web_element_wait_click(By.CLASS_NAME, self.__e_save_button_class,
                                             'next_button')
            return True
        except Exception as error:
            ui_logger.error(error)

    def success_message(self):
        try:
            time.sleep(1)
            self.wait.web_element_wait_text(By.TAG_NAME, self.__e_success_h, 'success_message')
            print("Selection::", self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)

    def update_slot_confirmation(self):
        try:
            self.driver.back()
            self.wait.refresh_page()
            time.sleep(3)
            self.wait.web_element_wait_text(By.XPATH, self.__e_thank_you_screen_xpath,
                                            'update_slot_confirmation')
            print('Update Slot:: ', self.wait.text_value)
            return True
        except Exception as error:
            ui_logger.error(error)
