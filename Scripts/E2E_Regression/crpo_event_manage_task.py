from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from pageObjects.Pages.ManageTaskPages.ManageTaskPage import ManageTaskScreen


class CRPOEventManageTask:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.applicant = EventApplicant(self.driver)
        self.candidate_details = CandidateDetailsPage(self.driver)
        self.task_screen = ManageTaskScreen(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['manage_task'], index=index)
        xl = status_excel.excel_dict
        self.xl_candidate_status1 = xl['candidate_status1'][0]
        self.xl_candidate_status2 = xl['candidate_status2'][0]
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_stage_status1 = xl['stage_status1'][0]
        self.xl_submit1 = xl['submit1'][0]
        self.xl_pending1 = xl['pending1'][0]
        self.xl_rejected1 = xl['rejected1'][0]
        self.xl_approved1 = xl['Approved1'][0]
        self.xl_total1 = xl['total1'][0]
        self.xl_stage_status2 = xl['stage_status2'][0]
        self.xl_submit2 = xl['submit2'][0]
        self.xl_pending2 = xl['pending2'][0]
        self.xl_rejected2 = xl['rejected2'][0]
        self.xl_approved2 = xl['Approved2'][0]
        self.xl_total2 = xl['total2'][0]

        self.event_app_details_collection = []
        self.event_app_task_submit_collection = []

    def crpo_event_applicant_manage_screen(self):
        self.event_app_details_collection = []

        __list = [self.applicant.applicant_get_name(self.xl_event_name, 1),
                  self.candidate_details.candidate_status(self.xl_candidate_status1),
                  self.candidate_details.candidate_float_actions(),
                  self.candidate_details.candidate_manage_task_action(2),
                  self.task_screen.candidate_name_validate(self.xl_event_name),
                  self.task_screen.submitted_task_validate(self.xl_submit1),
                  self.task_screen.pending_task_validate(self.xl_pending1),
                  self.task_screen.rejected_task_validate(self.xl_rejected1),
                  self.task_screen.approved_task_validate(self.xl_approved1),
                  self.task_screen.total_task_validate(self.xl_total1),
                  self.task_screen.switch_back_to_old_window()
                  ]
        for func in __list:
            if func:
                self.event_app_details_collection.append(func)
            else:
                self.event_app_details_collection.append(func)

    def crpo_event_applicant_manage_screen_submit_after(self):
        self.event_app_task_submit_collection = []

        __list = [self.applicant.applicant_get_name(self.xl_event_name, 1),
                  self.candidate_details.candidate_status(self.xl_candidate_status2),
                  self.candidate_details.candidate_float_actions(),
                  self.candidate_details.candidate_manage_task_action(2),
                  self.task_screen.candidate_name_validate(self.xl_event_name),
                  self.task_screen.submitted_task_validate(self.xl_submit2),
                  self.task_screen.pending_task_validate(self.xl_pending2),
                  self.task_screen.rejected_task_validate(self.xl_rejected2),
                  self.task_screen.approved_task_validate(self.xl_approved2),
                  self.task_screen.total_task_validate(self.xl_total2),
                  self.task_screen.switch_back_to_old_window()
                  ]
        for func in __list:
            if func:
                self.event_app_task_submit_collection.append(func)
            else:
                self.event_app_task_submit_collection.append(func)
