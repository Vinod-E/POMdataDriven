from Config import inputFile
from pageObjects.Pages.LoginPages.LoginPage import Login
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage


class CrpoInt2Login:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        int_excel = excelRead.ExcelRead()
        int_excel.read(inputFile.INPUT_PATH['int_login_excel'], index=index)
        xl = int_excel.excel_dict
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_int2 = xl['int2'][0]
        self.xl_int2_name = xl['int2_name'][0]
        self.xl_event = xl['event_name'][0].format(version)

        self.int2_collection = []

    def interviewer2_login(self):
        self.int2_collection = []
        __list = [self.login.login_account_click(self.xl_int1_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_int2),
                  self.login.password(self.xl_int2),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_int2_name),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event)
                  ]
        for func in __list:
            if func:
                self.int2_collection.append(func)
            else:
                self.int2_collection.append(func)
