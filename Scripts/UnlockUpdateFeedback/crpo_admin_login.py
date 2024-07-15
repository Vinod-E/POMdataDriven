from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.LoginPages.LoginPage import Login
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage, EventActionsPage
from pageObjects.Pages.BucketSelectPages.BucketPage import BucketSelectionPage
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from pageObjects.Pages.FeedbackPage.UnlockFeedbackPage import UnlockFeedback


class CrpoAdminLogin:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.login = Login(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.menu = Menu(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)
        self.bucket = BucketSelectionPage(self.driver)
        self.applicant_grid = EventApplicant(self.driver)
        self.applicant_action = EventApplicantActions(self.driver)
        self.unlock = UnlockFeedback(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['int_login_excel'], index=index)
        xl = excel.excel_dict
        self.xl_account_name = xl['account_name'][0]
        self.xl_int2_name = xl['int2_name'][0]
        self.xl_event = xl['event_name'][0].format(version)
        self.xl_menu = xl['menu'][0]
        self.xl_title = xl['tab_title'][0]

        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['admin_login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_name = xl['c_login_name'][0]
        self.xl_pwd = xl['c_password'][0]

        unlock_excel = excelRead.ExcelRead()
        unlock_excel.read(inputFile.INPUT_PATH['feedback'], index=index)
        xl = unlock_excel.excel_dict
        self.xl_bucket = xl['completed_bucket'][0]
        self.xl_unlock_comment = xl['unlock_comment'][0]
        self.xl_unlock_message = xl['unlock_message'][0]

        self.admin_collection = []
        self.unlock_collection = []

    def admin_login(self):
        self.admin_collection = []
        __list = [self.login.login_account_click(self.xl_int2_name),
                  self.login.login_out(),
                  self.login.click_here_to_login(),
                  self.login.login_name(self.xl_name),
                  self.login.password(self.xl_pwd),
                  self.login.login_button(),
                  self.login.login_account_name_verification(self.xl_account_name),
                  self.menu.event_tab(self.xl_menu, self.xl_title),
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

    def admin_unlock(self):
        self.unlock_collection = []
        __list = [self.event_action.event_actions_click(),
                  self.event_action.event_interviews(),
                  self.bucket.bucket_select(self.xl_bucket),
                  self.applicant_grid.select_applicant(),
                  self.applicant_action.unlock_feedback_action(),
                  self.unlock.select_all_interviewers(),
                  self.unlock.unlock_button(),
                  self.unlock.unlock_request_comment(self.xl_unlock_comment),
                  self.unlock.ok_button(),
                  self.unlock.unlock_status_notifier(self.xl_unlock_message),
                  self.unlock.unlock_status_notifier_dismiss(),
                  self.unlock.close_button()
                  ]
        for func in __list:
            if func:
                self.unlock_collection.append(func)
            else:
                self.unlock_collection.append(func)
