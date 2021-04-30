from Config import inputFile
from pageObjects.Pages.LiveInterviewSchedulePages.liveSchedulePage import LiveIntSchedulePage
from pageObjects.Pages.FeedbackPage.InterviewFeedbackPage import InterviewFeedback
from utilities import excelRead, SwitchWindow


class CrpoBehalfOfFeedback:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.live = LiveIntSchedulePage(self.driver)
        self.feedback = InterviewFeedback(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)

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
        self.xl_comment = xl['behalf_comment'][0]
        self.xl_overall = xl['behalf_overall'][0]

        self.behalf_of_collection = []

    def live_behalf_of_feedback(self):
        self.behalf_of_collection = []
        __list = [self.live.arrow_down_for_feedback(),
                  self.live.feedback_provide_action(),
                  self.new_tab.switch_to_window(1),
                  self.feedback.feedback_decision(self.xl_shortlist_decision),
                  self.feedback.feedback_select_drop_down(self.xl_rating),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.behalf_select_interviewers(),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.submit_feedback(),
                  self.feedback.agree_and_submit(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0),
                  self.live.clear_applicant_search()
                  ]
        for func in __list:
            if func:
                self.behalf_of_collection.append(func)
            else:
                self.behalf_of_collection.append(func)
