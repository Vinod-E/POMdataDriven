from Config import inputFile
from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.EventPages.EventInterviewerLobbyPage import InterviewerLobbyPage
from pageObjects.Pages.FeedbackPage.InterviewFeedbackPage import InterviewFeedback


class ProvideFeedback:
    def __init__(self, driver, index, version):

        self.driver = driver
        self.int_lobby = InterviewerLobbyPage(self.driver)
        self.feedback = InterviewFeedback(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)
        self.candidate_login = LoginPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['feedback'], index=index)
        xl = slot_excel.excel_dict
        self.xl_candidate_name = xl['event_name'][0].format(version)
        self.xl_shortlist_decision = xl['shortlist'][0]
        self.xl_rating = xl['rating'][0]
        self.xl_comment = xl['comment'][0]
        self.xl_overall = xl['overall'][0]

        self.pf_collection = []

    def provide_feedback(self):

        self.pf_collection = []
        __list = [self.int_lobby.provide_feedback(),
                  self.new_tab.switch_to_window(1),
                  self.feedback.feedback_decision(self.xl_shortlist_decision),
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
                self.pf_collection.append(func)
            else:
                self.pf_collection.append(func)
