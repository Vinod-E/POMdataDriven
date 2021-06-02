from Config import inputFile
from pageObjects.Pages.LoginPages.CandidateLoginPage import CandidateLogin
from utilities import excelRead
from utilities.OpenNewTab import NewTab


class CrpoCandidateLogin:

    def __init__(self, driver, index, version, server):
        self.driver = driver
        self.server = server
        self.LoginPage = CandidateLogin(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_title = xl['c_p_title'][0]
        self.xl_user = xl['c_p_user'][0].format(version)

        self.login_collection = []

    def candidate_login(self, candidate_email, password):
        self.login_collection = []
        __list = [self.LoginPage.candidate_login_url(self.server),
                  self.LoginPage.login_name(candidate_email),
                  self.LoginPage.password(password),
                  self.LoginPage.login_button(),
                  self.LoginPage.login_account_name_verification(self.xl_user)
                  ]
        for func in __list:
            if func:
                self.login_collection.append(func)
            else:
                self.login_collection.append(func)
