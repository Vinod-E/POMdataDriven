from Config import inputFile
from utilities import excelRead, appTitle
from pageObjects.Pages.LoginPages.LoginPage import Login


class CRPOLogin:
    def __init__(self, driver, index):
        self.driver = driver

        self.LoginPage = Login(self.driver)
        self.title = appTitle.Title(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_title = xl['c_title'][0]
        self.xl_tenant = xl['c_tenant'][0]
        self.xl_login = xl['c_login_name'][0]
        self.xl_user = xl['c_user_name'][0]
        self.xl_password = xl['c_password'][0]
        self.xl_logged_in_title = xl['c_logged_in_title'][0]

    def crpo_login(self):
        assert self.title.tab_title(self.xl_title) == self.xl_title
        self.LoginPage.tenant(self.xl_tenant)
        self.LoginPage.next_button()
        self.LoginPage.login_name(self.xl_login)
        self.LoginPage.password(self.xl_password)
        self.LoginPage.login_button()

        self.LoginPage.login_account_name_verification(self.xl_user)
        print(f'{self.xl_user} logged in successfully')
        self.title.tab_title(self.xl_title)
