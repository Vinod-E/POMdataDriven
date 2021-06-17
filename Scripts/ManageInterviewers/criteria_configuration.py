from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.InviteInterviewersPage import EventMangeInterviewersPage
from pageObjects.Pages.EventPages.ManageNominationsPage import EventNominationsPage


class CRPOCriteriaConfig:

    def __init__(self, driver, index):
        self.driver = driver
        self.interviewers = EventMangeInterviewersPage(self.driver)
        self.nomination = EventNominationsPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['manage_interviewers'], index=index)
        xl = status_excel.excel_dict
        self.xl_skill1 = xl['skill1'][0]
        self.xl_skill2 = xl['skill2'][0]
        self.xl_int_count = xl['int_count'][0]
        self.xl_nom_count = xl['nom_count'][0]
        self.xl_message = xl['message'][0]
        self.xl_header = xl['header'][0]

        self.skill1_criteria_collection = []
        self.skill2_criteria_collection = []
        self.send_criteria_collection = []

    def criteria_config_skill1(self):
        self.skill1_criteria_collection = []
        __list = [self.interviewers.add_criteria(),
                  self.interviewers.panel_skill1_select(self.xl_skill1),
                  self.interviewers.search_skill1_interviewers(),
                  self.interviewers.skill1_required_interviewers(self.xl_int_count),
                  self.interviewers.skill1_required_nomination(self.xl_nom_count)
                  ]
        for func in __list:
            if func:
                self.skill1_criteria_collection.append(func)
            else:
                self.skill1_criteria_collection.append(func)

    def criteria_config_skill2(self):
        self.skill2_criteria_collection = []
        __list = [self.interviewers.panel_skill2_select(self.xl_skill2),
                  self.interviewers.search_skill2_interviewers(),
                  self.interviewers.skill2_required_interviewers(self.xl_int_count),
                  self.interviewers.skill2_required_nomination(self.xl_nom_count)
                  ]
        for func in __list:
            if func:
                self.skill2_criteria_collection.append(func)
            else:
                self.skill2_criteria_collection.append(func)

    def send_nomination_mail(self):
        self.send_criteria_collection = []
        __list = [self.interviewers.send_mail_interviewers(),
                  self.interviewers.confirm_button(),
                  self.interviewers.confirm_button(),
                  self.interviewers.confirm_button(),
                  self.interviewers.criteria_notifier(self.xl_message),
                  self.interviewers.criteria_notifier_dismiss(),
                  self.nomination.nomination_tab(),
                  self.nomination.header_check(self.xl_header)
                  ]
        for func in __list:
            if func:
                self.send_criteria_collection.append(func)
            else:
                self.send_criteria_collection.append(func)
