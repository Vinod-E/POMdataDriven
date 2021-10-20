from Config import inputFile
from utilities import excelRead, ReadConfigFile
from pageObjects.Pages.LoginPages.LoginPage import Login
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName


class AdminLogin:
    def __init__(self, driver, index):

        self.driver = driver
        self.login = Login(self.driver)
        self.search = Search(self.driver)
        self.getby = EventGetByName(self.driver)
        self.event_action = Actions(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_tenant = xl['c_tenant'][0]
        self.xl_login = xl['c_login_name'][0]
        self.xl_user = xl['c_user_name'][0]
        self.xl_password = xl['c_password'][0]

        self.admin_login_collection = []

    def admin_login(self, server):
        if 'amsin' in server:
            self.driver.get(ReadConfigFile.ReadConfig.get_qa_url())
            self.index = 0
        elif 'ams' in server:
            self.driver.get(ReadConfigFile.ReadConfig.get_production_url())
            self.index = 1
        elif 'beta' in server:
            self.driver.get(ReadConfigFile.ReadConfig.get_beta_url())
            self.index = 1
        elif 'stage' in server:
            self.driver.get(ReadConfigFile.ReadConfig.get_stage_url())
            self.index = 1
        elif 'india' in server:
            self.driver.get(ReadConfigFile.ReadConfig.get_indiaams_url())
            self.index = 1

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
