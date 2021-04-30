from Config import inputFile
from pageObjects.Pages.EventPages import EventActionsPage
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from pageObjects.Pages.FeedbackPage.CancelInterview import CancelInterview


class CrpoInt2CancelRequest:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)
        self.search = Search(self.driver)
        self.applicant_grid = EventApplicant(self.driver)
        self.applicant_action = EventApplicantActions(self.driver)
        self.cancel_request = CancelInterview(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cancel_excel = excelRead.ExcelRead()
        cancel_excel.read(inputFile.INPUT_PATH['cancel_interview'], index=index)
        xl = cancel_excel.excel_dict
        self.xl_event_name = xl['name'][0].format(version)
        self.xl_comment = xl['comment'][0]
        self.xl_message = xl['cancel_interview'][0]

        self.int2_cancel_collection = []

    def cancel_interview(self):
        self.int2_cancel_collection = []
        __list = [self.event_action.event_actions_click(),
                  self.event_action.event_interviews(),
                  self.search.advance_search(),
                  self.search.candidate_name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.applicant_grid.select_applicant(),
                  self.applicant_action.cancel_interview_action(),
                  self.cancel_request.cancel_interview_request_comment(self.xl_comment),
                  self.cancel_request.cancel_interview_request_confirm(),
                  self.cancel_request.change_status_notifier(self.xl_message),
                  self.cancel_request.change_status_notifier_dismiss(),
                  ]
        for func in __list:
            if func:
                self.int2_cancel_collection.append(func)
            else:
                self.int2_cancel_collection.append(func)
