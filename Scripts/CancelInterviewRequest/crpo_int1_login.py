from Config import inputFile
from pageObjects.Pages.LoginPages.LoginPage import Login
from pageObjects.Pages.MenuPages.menuPage import Menu
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage


class CrpoInt1Login:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.menu = Menu(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        int_excel = excelRead.ExcelRead()
        int_excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = int_excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_int1 = xl['int1'][0]
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_event = xl['event_name'][0].format(version)
        self.xl_menu = xl['menu'][0]
        self.xl_title = xl['tab_title'][0]

        self.int1_collection = []

    def interviewer1_login(self):
        self.int1_collection = []
        __list = [self.login.login_account_click(self.xl_account_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_int1),
                  self.login.password(self.xl_int1),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_int1_name),
                  self.menu.event_tab(self.xl_menu, self.xl_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event),
                  ]
        for func in __list:
            if func:
                self.int1_collection.append(func)
            else:
                self.int1_collection.append(func)
