from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import inputFile
from utilities import excelRead, SwitchWindow, ReadConfigFile
from Config.LoginAPI import CommonLogin
from pageObjects.Pages.SSOPages import ScheduleAPI
from pageObjects.Pages.SSOPages import CancelAPI
from pageObjects.Pages.VideoInterviewPages.video_interview import VideoInterviewPage
from pageObjects.Pages.GmailPages.GmailLoginPage import LoginPageGmail


class SAMLLinks:

    def __init__(self, server):

        opt = webdriver.ChromeOptions()
        # opt.add_argument("--ignore-certificate-errors")
        opt.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=opt)
        if server == 'amsin':
            self.index = 0
        else:
            self.index = 1

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        aadhar_excel = excelRead.ExcelRead()
        aadhar_excel.read(inputFile.INPUT_PATH['sso'], index=self.index)
        xl = aadhar_excel.excel_dict
        self.xl_client_id = xl['id'][0]
        self.xl_client_secret = xl['secret'][0]
        self.xl_abacus_id = xl['abacus_id'][0]
        self.xl_stage = xl['stage'][0]
        self.xl_time = xl['time'][0]
        self.xl_int_first_name = xl['int_firstname'][0]
        self.xl_int_middle_name = xl['int_middlename'][0]
        self.xl_int_last_name = xl['int_lastname'][0]
        self.xl_int_email = xl['int_email'][0]
        self.xl_page_header1 = 'Please click below to go to the interview.'
        self.xl_page_header2 = 'You have already clicked the link to open interview.'
        self.xl_page_header3 = 'Online Proctoring Setup'
        # ---------------- Class Object ------------------------------------------
        self.login = CommonLogin()
        self.schedule_call = ScheduleAPI.ScheduleInterview()
        self.cancel_call = CancelAPI.CancelInterview()
        self.video = VideoInterviewPage(self.driver)
        self.window = SwitchWindow.SwitchWindowClose(self.driver)
        self.google = LoginPageGmail(self.driver)

        # ------------------ Collections ------------------------------------------
        self.login_collection = ''
        self.schedule_collection = ''
        self.cancel_collection = ''
        self.candidate_collection = ''
        self.video_collection = ''
        self.gmail_collection = ''
        self.proctoring_collection = ''

    def driver_chrome(self, link):
        try:
            self.driver.get(link)
            return True
        except ValueError as driver_chrome:
            print(driver_chrome)

    def access_token(self, server):
        self.login_collection = []
        __list = [self.login.abacus_access_login(server, self.xl_client_id, self.xl_client_secret)
                  ]
        for func in __list:
            if func:
                self.login_collection.append(func)
            else:
                self.login_collection.append(func)

    def abacus_interviewer_schedule(self, server):
        self.schedule_collection = []
        __list = [
            self.schedule_call.schedule_api_call(server, self.login.headers, self.xl_abacus_id, self.xl_stage, self.xl_time,
                                                 self.xl_int_first_name, self.xl_int_middle_name,
                                                 self.xl_int_last_name, self.xl_int_email)
            ]
        for func in __list:
            if func:
                self.schedule_collection.append(func)
            else:
                self.schedule_collection.append(func)

    def candidate_video_link(self):
        self.candidate_collection = []
        __list = [self.driver_chrome(self.schedule_call.candidate_link)
                  ]
        for func in __list:
            if func:
                self.candidate_collection.append(func)
            else:
                self.candidate_collection.append(func)

    def interviewer_video_link(self):
        self.candidate_collection = []
        __list = [self.driver_chrome(self.schedule_call.interview_link)
                  ]
        for func in __list:
            if func:
                self.candidate_collection.append(func)
            else:
                self.candidate_collection.append(func)

    def abacus_cancel_interview(self, server):
        self.cancel_collection = []
        __list = [self.cancel_call.cancel_api_call(server, self.login.headers, self.schedule_call.IR)
                  ]
        for func in __list:
            if func:
                self.cancel_collection.append(func)
            else:
                self.cancel_collection.append(func)

    def on_video_interview_screen(self):
        self.video_collection = []
        __list = [self.video.page_validation(self.xl_page_header1),
                  self.video.go_to_interview(),
                  self.video.page_validation(self.xl_page_header2),
                  self.window.switch_to_window(1)
                  ]
        for func in __list:
            if func:
                self.video_collection.append(func)
            else:
                self.video_collection.append(func)

    def gmail_login(self, key):

        if key == 'candidate':
            email = ReadConfigFile.ReadConfig.get_candidate_google_email()
            pwd = ReadConfigFile.ReadConfig.get_candidate_google_password()
        else:
            email = ReadConfigFile.ReadConfig.get_interviewer_google_email()
            pwd = ReadConfigFile.ReadConfig.get_interviewer_google_password()

        self.gmail_collection = []
        __list = [self.google.email_field(email),
                  self.google.next_button(),
                  self.google.password_field(pwd),
                  self.google.next_button()
                  ]
        for func in __list:
            if func:
                self.gmail_collection.append(func)
            else:
                self.gmail_collection.append(func)

    def on_proctoring_screen(self):

        self.proctoring_collection = []
        __list = [self.video.page_validation(self.xl_page_header3),
                  self.window.window_close(),
                  self.window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.proctoring_collection.append(func)
            else:
                self.proctoring_collection.append(func)
