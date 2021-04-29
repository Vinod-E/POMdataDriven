from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.LoginPages.LoginPage import Login
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs
from pageObjects.Pages.EventPages.EventCancelRequestPage import EventCancelRequest


class CrpoAdminLogin:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.event_tab = EventSubTabs(self.driver)
        self.admin_approve = EventCancelRequest(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_event = xl['event_name'][0].format(version)

        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_name = xl['c_login_name'][0]
        self.xl_pwd = xl['c_password'][0]

        cancel_excel = excelRead.ExcelRead()
        cancel_excel.read(inputFile.INPUT_PATH['cancel_interview'], index=index)
        xl = cancel_excel.excel_dict
        self.xl_comment = xl['comment'][0]
        self.xl_message = xl['approve_request_message'][0]

        self.admin_collection = []
        self.admin_accept_collection = []

    def admin_login(self):
        self.admin_collection = []
        __list = [self.login.login_account_click(self.xl_int1_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_name),
                  self.login.password(self.xl_pwd),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_account_name),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event),
                  ]
        for func in __list:
            if func:
                self.admin_collection.append(func)
            else:
                self.admin_collection.append(func)

    def admin_accept_cancellation(self):
        self.admin_accept_collection = []
        __list = [self.event_tab.tracking(),
                  self.event_tab.cancel_request_tab(),
                  self.admin_approve.accept_cancellation(),
                  self.admin_approve.cancel_request_comment(self.xl_comment),
                  self.admin_approve.confirm_request(),
                  self.admin_approve.go_ahead_with_lobby_screen(),
                  self.admin_approve.accept_cancellation(),
                  self.admin_approve.cancel_request_comment(self.xl_comment),
                  self.admin_approve.lobby_confirm_request(),
                  self.admin_approve.acceptance_notifier(self.xl_message),
                  self.admin_approve.acceptance_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.admin_accept_collection.append(func)
            else:
                self.admin_accept_collection.append(func)
