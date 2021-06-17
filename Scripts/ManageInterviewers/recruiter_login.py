from Config import inputFile
from pageObjects.Pages.LoginPages.LoginPage import Login
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage


class CrpoRecruiterLogin:

    def __init__(self, driver, index):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_login = xl['c_login_name'][0]
        self.xl_user = xl['c_user_name'][0]
        self.xl_password = xl['c_password'][0]
        self.xl_logged_in_title = xl['c_logged_in_title'][0]

        int_excel = excelRead.ExcelRead()
        int_excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = int_excel.excel_dict
        self.xl_int2_name = xl['int2_name'][0]

        self.rec_collection = []

    def recruiter_login(self):
        self.rec_collection = []
        __list = [self.login.login_account_click(self.xl_int2_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_login),
                  self.login.password(self.xl_password),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_user)
                  ]
        for func in __list:
            if func:
                self.rec_collection.append(func)
            else:
                self.rec_collection.append(func)
