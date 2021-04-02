import time
from Listeners.logger_settings import ui_logger


class SwitchWindowClose:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_window(self, window_index):
        try:
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            print('Switch to new - window')
            return True
        except Exception as error:
            ui_logger.error(error)

    def window_close(self):
        try:
            self.driver.close()
            print('Window - close')
            return True
        except Exception as error:
            ui_logger.error(error)
