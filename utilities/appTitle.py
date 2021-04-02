from Listeners.logger_settings import ui_logger


class Title:
    def __init__(self, driver):
        self.driver = driver

    def tab_title(self, tab_title):
        title = self.driver.title
        try:
            if tab_title in title:
                print(f'{title} is the current tab')
            else:
                print(f'{title} is the current tab and validation failed with {tab_title} tab')
        except Exception as error:
            ui_logger.error(error)
        return title
