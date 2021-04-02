from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.LoginPages.LoginPage import Login
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName


class InterviewLogin:
    def __init__(self, driver, index, version):

        self.driver = driver
        self.login = Login(self.driver)
        self.search = Search(self.driver)
        self.getby = EventGetByName(self.driver)
        self.event_action = Actions(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = slot_excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_int1 = xl['int1'][0]
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_event = xl['event_name'][0].format(version)

        self.int_collection = []

    def interviewer_login(self):
        self.int_collection = []
        __list = [self.login.login_account_click(self.xl_account_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_int1),
                  self.login.password(self.xl_int1),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_int1_name),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event),
                  self.event_action.event_actions_click(),
                  self.event_action.interview_lobby_panel()
                  ]
        for func in __list:
            if func:
                self.int_collection.append(func)
            else:
                self.int_collection.append(func)
