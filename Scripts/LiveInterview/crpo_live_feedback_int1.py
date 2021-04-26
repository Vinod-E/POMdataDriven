from Config import inputFile
from pageObjects.Pages.EventPages import EventActionsPage
from pageObjects.Pages.FeedbackPage.InterviewFeedbackPage import InterviewFeedback
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.LiveInterviewSchedulePages.liveSchedulePage import LiveIntSchedulePage


class CrpoInt1Feedback:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.live = LiveIntSchedulePage(self.driver)
        self.feedback = InterviewFeedback(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_event_name = xl['event_name'][0].format(version)
        self.xl_live_stage = xl['live_stage'][0]

        feed_excel = excelRead.ExcelRead()
        feed_excel.read(inputFile.INPUT_PATH['feedback'], index=index)
        xl = feed_excel.excel_dict
        self.xl_candidate_name = xl['event_name'][0].format(version)
        self.xl_shortlist_decision = xl['shortlist'][0]
        self.xl_rating = xl['rating'][0]
        self.xl_comment = xl['live_comment'][0]
        self.xl_overall = xl['live_overall'][0]

        self.int1_feedback_collection = []
        self.pf1_collection = []

    def live_interview1_feedback(self):
        self.int1_feedback_collection = []
        __list = [self.event_action.event_actions_click(),
                  self.event_action.live_interview_schedule(),
                  self.live.stage_selection(self.xl_live_stage),
                  self.live.applicant_name_filed(self.xl_event_name),
                  self.live.schedule_applicant_search(),
                  self.live.arrow_down_for_feedback(),
                  self.live.feedback_provide_action(),
                  self.new_tab.switch_to_window(1)
                  ]
        for func in __list:
            if func:
                self.int1_feedback_collection.append(func)
            else:
                self.int1_feedback_collection.append(func)

    def int1_provide_feedback(self):
        self.pf1_collection = []
        __list = [self.feedback.feedback_decision(self.xl_shortlist_decision),
                  self.feedback.feedback_select_drop_down(self.xl_rating),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.submit_feedback(),
                  self.feedback.agree_and_submit(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.pf1_collection.append(func)
            else:
                self.pf1_collection.append(func)
