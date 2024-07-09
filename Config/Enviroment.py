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
            self.index = 0
        else:
            self.index = 1

    def crpo_app(self):
        if self.server == 'amsin':
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
        elif self.server == 'ams':
            self.driver.get(ReadConfigFile.ReadConfig.get_production_url())
        elif self.server == 'beta':
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_url())
        elif self.server == 'stage':
            self.driver.get(ReadConfigFile.ReadConfig.get_stage_url())
        elif self.server == 'india':
            self.driver.get(ReadConfigFile.ReadConfig.get_indiaams_url())

    def registration_app(self, page):
        if self.server == 'amsin':
            if page == 'education':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_educational_url())
            elif page == 'certificate':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_certificate_url())
            elif page == 'applicantCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_acp_url())
            elif page == 'candidateCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_cp_url())
            elif page == 'ocr':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_ocr_url())
            elif page == 'payment':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_razorpay_url())
            elif page == 'workProfile':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_workprofile_url())
            elif page == 'aadhar':
                self.driver.get(ReadConfigFile.ReadConfig.get_qa_aadhar_url())
        elif self.server == 'beta':
            if page == 'education':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_educational_url())
            elif page == 'certificate':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_certificate_url())
            elif page == 'applicantCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_acp_url())
            elif page == 'candidateCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_cp_url())
            elif page == 'ocr':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_ocr_url())
            elif page == 'payment':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_razorpay_url())
            elif page == 'workProfile':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_workprofile_url())
            elif page == 'aadhar':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_aadhar_url())
        elif self.server == 'ams':
            if page == 'education':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_educational_url())
            elif page == 'certificate':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_certificate_url())
            elif page == 'applicantCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_acp_url())
            elif page == 'candidateCustomProperties':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_cp_url())
            elif page == 'ocr':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_ocr_url())
            elif page == 'payment':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_razorpay_url())
            elif page == 'workProfile':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_workprofile_url())
            elif page == 'aadhar':
                self.driver.get(ReadConfigFile.ReadConfig.get_prod_aadhar_url())

    def slot_app(self, app):
        if self.server == 'amsin':
            if app == 'assessment':
                self.driver.get(ReadConfigFile.ReadConfig.get_amsin_assessment_slot())
            elif app == 'interview':
                self.driver.get(ReadConfigFile.ReadConfig.get_amsin_interview_slot())
            elif app == 'Choose':
                self.driver.get(ReadConfigFile.ReadConfig.get_amsin_choose_slot())
        elif self.server == 'beta':
            if app == 'assessment':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_assessment_slot())
            elif app == 'interview':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_interview_slot())
            elif app == 'Choose':
                self.driver.get(ReadConfigFile.ReadConfig.get_beta_choose_slot())
        elif self.server == 'ams':
            if app == 'assessment':
                self.driver.get(ReadConfigFile.ReadConfig.get_ams_assessment_slot())
            elif app == 'interview':
                self.driver.get(ReadConfigFile.ReadConfig.get_ams_interview_slot())
            elif app == 'Choose':
                self.driver.get(ReadConfigFile.ReadConfig.get_ams_choose_slot())

    def close(self):
        try:
            print("Run completed at:: " + str(datetime.datetime.now()))
            self.driver.close()
        except Exception as error:
            ui_logger.error(error)
