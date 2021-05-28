from Config import inputFile
from pageObjects.Pages.LoginPages.LoginPage import Login
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage


class CrpoCandidateLogin:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['help_desk'], index=index)
        xl = excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_int1 = xl['int1'][0]
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_event = xl['event_name'][0].format(version)

        self.candidate_login_collection = []

    def candidate_login(self):
        self.candidate_login_collection = []
        __list = [
                  ]
        for func in __list:
            if func:
                self.candidate_login_collection.append(func)
            else:
                self.candidate_login_collection.append(func)
