from Config import inputFile
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.StatusChangePage.StatusChange import ChangeStatus
from pageObjects.Pages.CandidatePages import CandidateDetailsPage
from pageObjects.Pages.EventPages import EventApplicantPage
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues


class EventApplicant:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.applicant_grid = EventApplicantPage.EventApplicant(self.driver)
        self.candidate_details = CandidateDetailsPage.CandidateDetailsPage(self.driver)
        self.status_change = ChangeStatus(self.driver)
        self.window_switch = SwitchWindow.SwitchWindowClose(self.driver)
        self.multi_select = MultiSelectValues(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_stage = xl['new_stage'][0]
        self.xl_status = xl['schedule'][0]
        self.xl_comment = xl['new_comment'][0]
        self.xl_message = xl['live_message'][0]

        self.applicant_status_collection = []

    def event_change_applicant_status(self):
        self.applicant_status_collection = []

        __list = [self.applicant_grid.select_applicant(),
                  self.applicant_grid.change_status_action(),
                  self.status_change.applicant_stage(self.xl_stage),
                  self.status_change.applicant_status(self.xl_status),
                  self.status_change.select_interviewers(),
                  self.multi_select.move_all_items(),
                  self.multi_select.done(),
                  self.status_change.comment(self.xl_comment),
                  self.status_change.change_button(),
                  self.status_change.change_status_notifier(self.xl_message),
                  self.status_change.change_status_notifier_dismiss(),
                  self.applicant_grid.applicant_get_name(self.xl_event_name, 1),
                  self.candidate_details.candidate_status(self.xl_status),
                  self.window_switch.window_close(),
                  self.window_switch.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_status_collection.append(func)
            else:
                self.applicant_status_collection.append(func)
