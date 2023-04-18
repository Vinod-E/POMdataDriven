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

        opt = webdriver.ChromeOptions()
        # opt.add_argument("--ignore-certificate-errors")
        opt.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=opt)

        if self.server == 'amsin':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
            self.index = 0
        elif self.server == 'amsinc':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_certificate_url())
            self.index = 0
        elif self.server == 'amsine':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_educational_url())
            self.index = 0
        elif self.server == 'amsino':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_ocr_url())
            self.index = 0
        elif self.server == 'amsinr':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_razorpay_url())
            self.index = 0
        elif self.server == 'amsina':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_aadhar_url())
            self.index = 0
        elif self.server == 'amsinw':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_workprofile_url())
            self.index = 0
        elif self.server == 'amsincp':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_cp_url())
            self.index = 0
        elif self.server == 'amsc':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_certificate_url())
            self.index = 1
        elif self.server == 'amse':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_educational_url())
            self.index = 1
        elif self.server == 'amso':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_ocr_url())
            self.index = 1
        elif self.server == 'amsr':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_razorpay_url())
            self.index = 1
        elif self.server == 'amsa':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_aadhar_url())
            self.index = 1
        elif self.server == 'amsw':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_workprofile_url())
            self.index = 1
        elif self.server == 'amscp':
            self.driver.get(ReadConfigFile.ReadConfig.get_prod_cp_url())
            self.index = 1
        elif self.server == 'betac':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_certificate_url())
            self.index = 1
        elif self.server == 'betae':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_educational_url())
            self.index = 1
        elif self.server == 'betao':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_ocr_url())
            self.index = 1
        elif self.server == 'betar':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_razorpay_url())
            self.index = 1
        elif self.server == 'betaa':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_aadhar_url())
            self.index = 1
        elif self.server == 'betaw':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_workprofile_url())
            self.index = 1
        elif self.server == 'betacp':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_cp_url())
            self.index = 1
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
