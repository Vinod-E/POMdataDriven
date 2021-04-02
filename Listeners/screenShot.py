from Config import CongfigFile
from Listeners.logger_settings import ui_logger


class FailureImage:

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, image_name):
        try:
            self.driver.save_screenshot(CongfigFile.IMAGE.format(image_name))
        except Exception as image_error:
            ui_logger.error(image_error)
