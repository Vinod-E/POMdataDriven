from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.LoginPages.EmbraceLoginPage import EmbraceLogin


class CrpoEmbraceLogin:

    def __init__(self, driver, index, server):
        self.driver = driver
        self.server = server
        self.embrace_login = EmbraceLogin(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['help_desk'], index=index)
        xl = excel.excel_dict
        self.xl_login_1_name = xl['default_user'][0]
        self.xl_login_2_name = xl['job_user'][0]
        self.xl_login_3_name = xl['event_user'][0]
        self.xl_login_1 = xl['default_user_loginname'][0]
        self.xl_login_2 = xl['job_user_loginname'][0]
        self.xl_login_3 = xl['event_user_loginname'][0]
        self.xl_password = xl['Password'][0]
        self.xl_tab_title = xl['tab'][0]
        self.xl_tenant = xl['tenant'][0]

        self.login_1_collection = []
        self.login_2_collection = []
        self.login_3_collection = []

    def embrace_user_1_login(self):
        self.login_1_collection = []
        __list = [self.embrace_login.embrace_url(self.server),
                  # self.embrace_login.next_button(),
                  self.embrace_login.login_alias(self.xl_tenant),
                  self.embrace_login.login_name(self.xl_login_1),
                  self.embrace_login.password(self.xl_password),
                  self.embrace_login.login_button(),
                  self.embrace_login.login_account_name_verification(self.xl_login_1_name)
                  ]
        for func in __list:
            if func:
                self.login_1_collection.append(func)
            else:
                self.login_1_collection.append(func)

    def embrace_user_2_login(self):
        self.login_2_collection = []
        __list = [self.embrace_login.embrace_url(self.server),
                  self.embrace_login.login_name(self.xl_login_2),
                  self.embrace_login.password(self.xl_password),
                  self.embrace_login.login_button(),
                  self.embrace_login.login_account_name_verification(self.xl_login_2_name)]
        for func in __list:
            if func:
                self.login_2_collection.append(func)
            else:
                self.login_2_collection.append(func)

    def embrace_user_3_login(self):
        self.login_3_collection = []
        __list = [self.embrace_login.embrace_url(self.server),
                  self.embrace_login.login_name(self.xl_login_3),
                  self.embrace_login.password(self.xl_password),
                  self.embrace_login.login_button(),
                  self.embrace_login.login_account_name_verification(self.xl_login_3_name)]
        for func in __list:
            if func:
                self.login_3_collection.append(func)
            else:
                self.login_3_collection.append(func)
