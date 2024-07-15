from Config import (inputFile)
from pageObjects.Pages.LoginPages.LoginPage import Login
from utilities import excelRead


class AdminLogin:
    def __init__(self, driver, index):

        self.driver = driver
        self.login = Login(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        admin_login_excel = excelRead.ExcelRead()
        admin_login_excel.read(inputFile.INPUT_PATH['admin_login_excel'], index=index)
        xl = admin_login_excel.excel_dict
        self.xl_tenant = xl['c_tenant'][0]
        self.xl_login = xl['c_login_name'][0]
        self.xl_user = xl['c_user_name'][0]
        self.xl_password = xl['c_password'][0]

        int_login_excel = excelRead.ExcelRead()
        int_login_excel.read(inputFile.INPUT_PATH['int_login_excel'], index=index)
        xl = int_login_excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_interviewer = xl['int1'][0]
        self.xl_interviewer_name = xl['int1_name'][0]

        self.admin_login_collection = []
        self.interviewer_collection = []
        self.re_login_collection = []

    def admin_login(self):
        self.admin_login_collection = []
        __list = [self.login.tenant(self.xl_tenant),
                  self.login.next_button(),
                  self.login.login_name(self.xl_login),
                  self.login.password(self.xl_password),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_user)
                  ]
        for func in __list:
            if func:
                self.admin_login_collection.append(func)
            else:
                self.admin_login_collection.append(func)

    def admin_re_login(self):
        self.re_login_collection = []
        __list = [self.login.login_account_click(self.xl_account_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_login),
                  self.login.password(self.xl_password),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_user)
                  ]
        for func in __list:
            if func:
                self.re_login_collection.append(func)
            else:
                self.re_login_collection.append(func)

    def interviewer_login(self):
        self.interviewer_collection = []
        __list = [self.login.login_account_click(self.xl_account_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_interviewer),
                  self.login.password(self.xl_interviewer),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_interviewer_name)
                  ]
        for func in __list:
            if func:
                self.interviewer_collection.append(func)
            else:
                self.interviewer_collection.append(func)
