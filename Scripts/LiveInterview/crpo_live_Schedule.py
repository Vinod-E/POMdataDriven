from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.LiveInterviewSchedulePages.liveSchedulePage import LiveIntSchedulePage


class CrpoLiveSchedule:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.live = LiveIntSchedulePage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_live_stage = xl['live_stage'][0]
        self.xl_screen_validate = xl['live_screen_validate'][0]
        self.xl_live_message = xl['live_message'][0]

        self.event_live_schedule_collection = []

    def live_interview_schedule(self):
        self.event_live_schedule_collection = []
        __list = [self.live.stage_selection(self.xl_live_stage),
                  self.live.applicant_name_filed(self.xl_event_name),
                  self.live.schedule_applicant_search(),
                  self.live.select_live_applicant(),
                  self.live.schedule_select(),
                  self.live.validate_interviewers_screen(self.xl_screen_validate),
                  self.live.select_interviewers(),
                  self.live.live_schedule(),
                  self.live.live_schedule_notifier(self.xl_live_message),
                  self.live.live_schedule_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.event_live_schedule_collection.append(func)
            else:
                self.event_live_schedule_collection.append(func)
