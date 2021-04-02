from Config import inputFile
from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.EventPages.EventInterviewerLobbyPage import InterviewerLobbyPage


class SelectCandidate:
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
        self.your_turn = xl['your_turn_message'][0]

        self.select_candidate_collection = []

    def select_candidate(self, candidate_id, candidate_login_link):
        self.select_candidate_collection = []
        __list = [self.int_lobby.select_candidate(),
                  self.candidate_login.open_link(candidate_login_link),
                  self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room(),
                  self.candidate_login.candidate_name_validate(self.xl_candidate_name),
                  self.candidate_login.it_is_your_message(self.your_turn),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.select_candidate_collection.append(func)
            else:
                self.select_candidate_collection.append(func)
