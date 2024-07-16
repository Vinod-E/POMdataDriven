from Config import inputFile
from pageObjects.Pages.FeedbackPage.NewFormInterviewFeedbackPage import InterviewFeedback
from utilities import excelRead, SwitchWindow


class CrpoInterviewerFeedback:

    def __init__(self, driver, index):
        self.driver = driver
        self.feedback = InterviewFeedback(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        feed_excel = excelRead.ExcelRead()
        feed_excel.read(inputFile.INPUT_PATH['feedback'], index=index)
        xl = feed_excel.excel_dict
        self.xl_candidate_name = 'Revisefeedback'
        self.xl_shortlist_decision = xl['shortlist'][0]
        self.xl_reject_decision = xl['reject'][0]
        self.xl_rating1 = xl['rating1'][0]
        self.xl_rating = xl['rating'][0]
        self.xl_comment = xl['new_comment'][0]
        self.xl_overall = xl['new_overall'][0]

        self.int_collection = []
        self.int_revise__collection = []

    def interviewer_provide_feedback(self):
        self.int_collection = []
        __list = [self.feedback.feedback_select_drop_down(self.xl_rating1),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.feedback_decision(self.xl_shortlist_decision),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.submit_feedback(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.int_collection.append(func)
            else:
                self.int_collection.append(func)

    def interviewer_revise_provide_feedback(self):
        self.int_revise__collection = []
        __list = [self.feedback.feedback_select_drop_down(self.xl_rating),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.feedback_decision(self.xl_reject_decision),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.update_feedback(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.int_revise__collection.append(func)
            else:
                self.int_revise__collection.append(func)
