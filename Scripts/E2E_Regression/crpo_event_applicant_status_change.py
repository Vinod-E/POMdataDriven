from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.StatusChangePage.StatusChange import ChangeStatus


class CRPOEventApplicantStatusChange:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = Search(self.driver)
        self.get_by = EventGetByName(self.driver)
        self.action = Actions(self.driver)
        self.applicant = EventApplicant(self.driver)
        self.status = ChangeStatus(self.driver)
        self.candidate_details = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_hop_status = xl['hop_status'][0]
        self.xl_stage = xl['e2e_stage'][0]
        self.xl_status = xl['e2e_status'][0]
        self.xl_comment = xl['e2e_comment'][0]
        self.xl_message = xl['message'][0]

        self.event_app_status_collection = []
        self.event_change_status_collection = []

    def crpo_event_applicant(self):
        self.event_app_status_collection = []
        __list = [self.menu.event_tab(self.xl_menu, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.get_by.event_name_click(),
                  self.get_by.event_name_validation(self.xl_event_name),
                  self.action.event_actions_click(),
                  self.action.event_view_candidates(),
                  self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_event_name),
                  self.search.search_button(),
                  self.applicant.applicant_get_name(self.xl_event_name, 1),
                  self.candidate_details.candidate_status(self.xl_hop_status),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.event_app_status_collection.append(func)
            else:
                self.event_app_status_collection.append(func)

    def crpo_event_status_change(self):
        self.event_change_status_collection = []
        __list = [self.applicant.select_applicant(),
                  self.applicant.change_status_action(),
                  self.status.applicant_stage(self.xl_stage),
                  self.status.applicant_status(self.xl_status),
                  self.status.comment(self.xl_comment),
                  self.status.change_button(),
                  self.status.change_status_notifier(self.xl_message),
                  self.status.change_status_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.event_change_status_collection.append(func)
            else:
                self.event_change_status_collection.append(func)
