from Config import inputFile
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from pageObjects.Pages.QuickInterviewSchedulePages.QuickSchedule import QuickIntSchedulePage
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage


class CRPOQuickInterviewSchedule:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.applicant_grid = EventApplicant(self.driver)
        self.getby = CandidateDetailsPage(self.driver)
        self.applicant_action = EventApplicantActions(self.driver)
        self.quick_schedule = QuickIntSchedulePage(self.driver)
        self.multi_select = MultiSelectValues(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        int_excel = excelRead.ExcelRead()
        int_excel.read(inputFile.INPUT_PATH['interview_lobby'], index=index)
        xl = int_excel.excel_dict
        self.xl_int1_name = xl['int1_name'][0]
        self.xl_int2_name = xl['int2_name'][0]

        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_quick_stage = xl['live_stage'][0]
        self.xl_quick_comment = xl['quick_comment'][0]
        self.xl_quick_message = xl['live_message'][0]
        self.xl_app_name = xl['event_name'][0].format(version)
        self.xl_schedule_status = xl['schedule'][0]

        self.quick_config_collection = []
        self.quick_schedule_collection = []

    def quick_interview_config(self):
        self.quick_config_collection = []
        __list = [self.applicant_grid.select_applicant(),
                  self.applicant_action.more_action(),
                  self.applicant_action.quick_interview_action(),
                  self.quick_schedule.select_interviewers_field(),
                  self.multi_select.search(self.xl_int1_name),
                  self.multi_select.move_all_items(),
                  self.multi_select.search_clear(),
                  self.multi_select.search(self.xl_int2_name),
                  self.multi_select.move_all_items(),
                  self.multi_select.done()
                  ]
        for func in __list:
            if func:
                self.quick_config_collection.append(func)
            else:
                self.quick_config_collection.append(func)

    def quick_interview_schedule(self):
        self.quick_schedule_collection = []
        __list = [self.quick_schedule.select_interviewer_round(self.xl_quick_stage),
                  self.quick_schedule.quick_comment(self.xl_quick_comment),
                  self.quick_schedule.schedule_quick_interview(),
                  self.quick_schedule.quick_schedule_notifier(self.xl_quick_message),
                  self.quick_schedule.quick_schedule_notifier_dismiss(),
                  self.applicant_grid.applicant_get_name(self.xl_app_name, 1),
                  self.getby.candidate_status(self.xl_schedule_status),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.quick_schedule_collection.append(func)
            else:
                self.quick_schedule_collection.append(func)
