from Config import inputFile
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose
from utilities.uiNotifier import Notifier
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from pageObjects.Pages.StatusChangePage.StatusChange import ChangeStatus
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from pageObjects.Pages.EventPages.eventrevisefeedbackPage import EventReviseFeedbackPage


class CRPOEventApplicant:

    def __init__(self, driver, index):
        self.driver = driver
        self.notifier = Notifier(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)
        self.applicant = EventApplicant(self.driver)
        self.event_applicant_action = EventApplicantActions(self.driver)
        self.change_status = ChangeStatus(self.driver)
        self.multi_select = MultiSelectValues(self.driver)
        self.candidate_details = CandidateDetailsPage(self.driver)
        self.revise = EventReviseFeedbackPage(self.driver)

        self.change_applicant_collection = []
        self.candidate_verification_collection = []
        self.revise_feedback_collection = []

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['revise_feedback'], index=index)
        xl = excel.excel_dict
        self.xl_applicant_name = xl['applicant_name'][0]
        self.xl_stage = xl['stage'][0]
        self.xl_status = xl['status'][0]
        self.xl_interviewer = xl['int1'][0]
        self.xl_comment = xl['comment'][0]
        self.xl_message = xl['message'][0]
        self.xl_revise_comment = xl['Revise_comment'][0]

    def crpo_change_applicant_status(self):
        self.change_applicant_collection = []
        __list = [self.applicant.select_applicant(),
                  self.applicant.change_status_action(),
                  self.change_status.applicant_stage(self.xl_stage),
                  self.change_status.applicant_status(self.xl_status),
                  self.change_status.select_interviewers(),
                  self.multi_select.search(self.xl_interviewer),
                  self.multi_select.move_all_items(),
                  self.multi_select.done(),
                  self.change_status.comment(self.xl_comment),
                  self.change_status.change_button(),
                  self.change_status.change_status_notifier(self.xl_message),
                  ]
        for func in __list:
            if func:
                self.change_applicant_collection.append(func)
            else:
                self.change_applicant_collection.append(func)

    def crpo_revise_feedback(self):
        self.revise_feedback_collection = []
        __list = [self.applicant.select_applicant(),
                  self.event_applicant_action.more_action(),
                  self.event_applicant_action.applicant_revise_feedback(),
                  self.revise.revise_comment(self.xl_revise_comment),
                  self.revise.revise_submit_button()
                  ]
        for func in __list:
            if func:
                self.revise_feedback_collection.append(func)
            else:
                self.revise_feedback_collection.append(func)

    def crpo_candidate_verification(self):
        self.candidate_verification_collection = []
        __list = [self.applicant.applicant_get_name(self.xl_applicant_name, 1),
                  self.candidate_details.candidate_status(self.xl_status),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.candidate_verification_collection.append(func)
            else:
                self.candidate_verification_collection.append(func)
