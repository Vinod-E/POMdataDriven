from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.ManageNominationsPage import EventNominationsPage


class CRPORecruiterApproval:

    def __init__(self, driver, index):
        self.driver = driver
        self.nomination_approval = EventNominationsPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['manage_interviewers'], index=index)
        xl = status_excel.excel_dict
        self.xl_skill1 = xl['skill1'][0]
        self.xl_skill2 = xl['skill2'][0]
        self.xl_message = xl['sync_message'][0]

        self.recruiter_acceptance_collection = []
        self.sync_collection = []

    def recruiter_approval_skill(self):
        self.recruiter_acceptance_collection = []
        __list = [self.nomination_approval.refresh_list(),
                  self.nomination_approval.panel_select(self.xl_skill1),
                  self.nomination_approval.select_applicants(),
                  self.nomination_approval.recruiter_actions(),
                  self.nomination_approval.approve_by_recruiter(),
                  self.nomination_approval.refresh_list(),
                  self.nomination_approval.panel_select(self.xl_skill2),
                  self.nomination_approval.select_applicants(),
                  self.nomination_approval.recruiter_actions(),
                  self.nomination_approval.approve_by_recruiter()
                  ]
        for func in __list:
            if func:
                self.recruiter_acceptance_collection.append(func)
            else:
                self.recruiter_acceptance_collection.append(func)

    def sync_interviewers(self):
        self.sync_collection = []
        __list = [self.nomination_approval.sync_interviewers(),
                  self.nomination_approval.sync_notifier(self.xl_message),
                  self.nomination_approval.sync_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.sync_collection.append(func)
            else:
                self.sync_collection.append(func)
