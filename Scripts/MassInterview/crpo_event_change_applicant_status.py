from Config import inputFile
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.StatusChangePage.StatusChange import ChangeStatus
from pageObjects.Pages.CandidatePages import CandidateDetailsPage
from pageObjects.Pages.EventPages import EventGetByNamePage, EventApplicantPage, EventActionsPage


class EventApplicant:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)
        self.applicant_grid = EventApplicantPage.EventApplicant(self.driver)
        self.candidate_details = CandidateDetailsPage.CandidateDetailsPage(self.driver)
        self.status_change = ChangeStatus(self.driver)
        self.window_switch = SwitchWindow.SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_stage = xl['stage'][0]
        self.xl_status = xl['status'][0]
        self.xl_comment = xl['comment'][0]
        self.xl_message = xl['message'][0]

        self.event_collection = []
        self.applicant_collection = []

    def event(self):
        self.event_collection = []
        __list = [self.search.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event_name)
                  ]
        for func in __list:
            if func:
                self.event_collection.append(func)
            else:
                self.event_collection.append(func)

    def event_applicant_grid(self):
        __list = [self.event_action.event_actions_click(),
                  self.event_action.event_view_candidates(),
                  self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_event_name),
                  self.search.search_button(),
                  self.applicant_grid.select_applicant(),
                  self.applicant_grid.change_status_action(),
                  self.status_change.applicant_stage(self.xl_stage),
                  self.status_change.applicant_status(self.xl_status),
                  self.status_change.comment(self.xl_comment),
                  self.status_change.change_button(),
                  self.applicant_grid.applicant_get_name(self.xl_event_name, self.xl_message),
                  self.window_switch.switch_to_window(1),
                  self.candidate_details.candidate_status(self.xl_status),
                  self.candidate_details.candidate_id_copy(),
                  self.window_switch.window_close(),
                  self.window_switch.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_collection.append(func)
            else:
                self.applicant_collection.append(func)
