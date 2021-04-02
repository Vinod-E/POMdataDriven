import datetime
from selenium import webdriver
from utilities import ReadConfigFile
from webdriver_manager.chrome import ChromeDriverManager
from Listeners.logger_settings import ui_logger


class EnvironmentSetup:
    def __init__(self):
        self.server = input('Please Enter testing Environment:: ')
        self.sprint_version = input('Please Enter Sprint version:: ')
        self.start_date_time = datetime.datetime.now()
        print("Run started at:: "+str(self.start_date_time))

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

        if self.server == 'amsin':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
            self.index = 0
        elif self.server == 'ams':
            self.driver.get(ReadConfigFile.ReadConfig.get_production_url())
            self.index = 1
        elif self.server == 'beta':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_url())
            self.index = 1
        elif self.server == 'stage':
            self.driver.get(ReadConfigFile.ReadConfig.get_stage_url())
            self.index = 1
        elif self.server == 'india':
            self.driver.get(ReadConfigFile.ReadConfig.get_indiaams_url())
            self.index = 1

    def close(self):
        try:
            print("Run completed at:: " + str(datetime.datetime.now()))
            self.driver.close()
        except Exception as error:
            ui_logger.error(error)
