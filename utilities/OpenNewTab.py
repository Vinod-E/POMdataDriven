from Listeners.logger_settings import ui_logger


class NewTab:
    def __init__(self, driver):
        self.driver = driver

    def open_new_tab(self, tab_index, url_link):
        try:
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[tab_index])
            self.driver.get(url_link)
        except Exception as error:
            ui_logger.error(error)
