from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Listeners.logger_settings import ui_logger

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })


class BrowserPopUp:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_window(self, window_index):
        try:
            v= self.driver.switch_to.alert()
            v.accept()
            print('Switch to new - window')
            return True
        except Exception as error:
            ui_logger.error(error)
