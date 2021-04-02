from Config import inputFile
from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.EventPages.EventInterviewerLobbyPage import InterviewerLobbyPage


class InviteCandidate:
    def __init__(self, driver, index, version):

        self.driver = driver
        self.int_lobby = InterviewerLobbyPage(self.driver)
        self.new_tab = SwitchWindow.SwitchWindowClose(self.driver)
        self.candidate_login = LoginPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['candidate_lobby'], index=index)
        xl = slot_excel.excel_dict
        self.xl_candidate_name = xl['name'][0].format(version)
        self.xl_finished_message = xl['finished_message'][0]

        self.invite_candidate_collection = []

    def invite_candidate(self, candidate_id, candidate_login_link):
        self.invite_candidate_collection = []
        __list = [self.int_lobby.invite_video_button(),
                  self.int_lobby.check_box(),
                  self.int_lobby.proceed_video_link(),
                  self.new_tab.switch_to_window(1),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0),
                  self.int_lobby.finish_interview(),
                  self.int_lobby.full_finish_interview(),
                  self.candidate_login.open_link(candidate_login_link),
                  self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room(),
                  self.candidate_login.candidate_name_validate(self.xl_candidate_name),
                  self.candidate_login.finish_interview_message(self.xl_finished_message),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.invite_candidate_collection.append(func)
            else:
                self.invite_candidate_collection.append(func)
