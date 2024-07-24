from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import inputFile
from utilities import excelRead
from Config.LoginAPI import CommonLogin
from pageObjects.Pages.SSOPages import ScheduleAPI
from pageObjects.Pages.SSOPages import CancelAPI


class SAMLLinks:

    def __init__(self, server):
        self.login = CommonLogin()
        self.schedule_call = ScheduleAPI.ScheduleInterview()
        self.cancel_call = CancelAPI.CancelInterview()
        self.login_collection = ''
        self.schedule_collection = ''
        self.cancel_collection = ''
        self.candidate_collection = ''

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

    def access_token(self):
        self.login_collection = []
        __list = [self.login.abacus_access_login(self.xl_client_id, self.xl_client_secret)
                  ]
        for func in __list:
            if func:
                self.login_collection.append(func)
            else:
                self.login_collection.append(func)

    def abacus_interviewer_schedule(self):
        self.schedule_collection = []
        __list = [
            self.schedule_call.schedule_api_call(self.login.headers, self.xl_abacus_id, self.xl_stage, self.xl_time,
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
        __list = [self.driver.get(self.schedule_call.candidate_link)

                  ]
        for func in __list:
            if func:
                self.candidate_collection.append(func)
            else:
                self.candidate_collection.append(func)

    def abacus_cancel_interview(self):
        self.cancel_collection = []
        __list = [self.cancel_call.cancel_api_call(self.login.headers, self.schedule_call.IR)
                  ]
        for func in __list:
            if func:
                self.cancel_collection.append(func)
            else:
                self.cancel_collection.append(func)
