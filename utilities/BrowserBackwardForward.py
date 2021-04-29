from Listeners.logger_settings import ui_logger


class ForwardBackward:
    def __init__(self, driver):
        self.driver = driver

    def browser_forward(self):
        try:
            self.driver.forward()
        except Exception as error:
            ui_logger.error(error)

    def browser_backward(self):
        try:
            self.driver.back()
        except Exception as error:
            ui_logger.error(error)
