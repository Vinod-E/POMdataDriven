from Config import inputFile
from pageObjects.Pages.BucketSelectPages.BucketPage import BucketSelectionPage
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from pageObjects.Pages.FeedbackPage.InterviewFeedbackPage import InterviewFeedback


class CrpoInt1Feedback:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.feedback = InterviewFeedback(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)
        self.search = Search(self.driver)
        self.applicant_grid = EventApplicant(self.driver)
        self.applicant_action = EventApplicantActions(self.driver)
        self.bucket = BucketSelectionPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        feed_excel = excelRead.ExcelRead()
        feed_excel.read(inputFile.INPUT_PATH['feedback'], index=index)
        xl = feed_excel.excel_dict
        self.xl_bucket = xl['completed_bucket'][0]
        self.xl_candidate_name = xl['event_name'][0].format(version)
        self.xl_pending_decision = xl['pending'][0]
        self.xl_shortlist_decision = xl['shortlist'][0]
        self.xl_rating = xl['rating'][0]
        self.xl_rating1 = xl['rating1'][0]
        self.xl_comment = xl['unlock_comment'][0]
        self.xl_overall = xl['unlock_overall'][0]

        self.int1_feedback_collection = []
        self.pf1_collection = []
        self.update_f_d_collection = []
        self.completed_bucket_collection = []

    def completed_bucket(self):
        self.completed_bucket_collection = []
        __list = [self.bucket.bucket_select(self.xl_bucket)
                  ]
        for func in __list:
            if func:
                self.completed_bucket_collection.append(func)
            else:
                self.completed_bucket_collection.append(func)

    def interview1_feedback(self):
        self.int1_feedback_collection = []
        __list = [self.search.advance_search(),
                  self.search.candidate_name_field(self.xl_candidate_name),
                  self.search.search_button(),
                  self.applicant_grid.select_applicant(),
                  self.applicant_action.provide_feedback_action(),
                  self.new_tab.switch_to_window(1)
                  ]
        for func in __list:
            if func:
                self.int1_feedback_collection.append(func)
            else:
                self.int1_feedback_collection.append(func)

    def int1_provide_feedback(self):
        self.pf1_collection = []
        __list = [self.feedback.feedback_decision(self.xl_pending_decision),
                  self.feedback.feedback_select_drop_down(self.xl_rating),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.submit_feedback(),
                  self.feedback.agree_and_submit(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.pf1_collection.append(func)
            else:
                self.pf1_collection.append(func)

    def int1_update_feedback_decision(self):
        self.update_f_d_collection = []
        __list = [self.feedback.feedback_decision(self.xl_shortlist_decision),
                  self.feedback.feedback_select_drop_down(self.xl_rating1),
                  self.feedback.feedback_comments(self.xl_comment),
                  self.feedback.overall_comment(self.xl_overall),
                  self.feedback.update_feedback(),
                  self.feedback.agree_and_submit(),
                  self.feedback.agree_and_submit(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.update_f_d_collection.append(func)
            else:
                self.update_f_d_collection.append(func)
