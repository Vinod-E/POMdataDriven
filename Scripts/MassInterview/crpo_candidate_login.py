from Config import inputFile
from pageObjects.Pages.CandidateLobbyLink.CandidateLoginPage import LoginPage
from pageObjects.Pages.EventPages.EventLobbyPage import LobbyPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CandidateLobbyLogin:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.candidate_login = LoginPage(self.driver)
        self.new_tab = SwitchWindowClose(self.driver)
        self.lobby = LobbyPage(self.driver)
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['candidate_lobby'], index=index)
        xl = status_excel.excel_dict
        self.xl_candidate_name = xl['name'][0].format(version)
        self.xl_almost_message = xl['almost_message'][0]
        self.xl_queued_message = xl['queued_message'][0]

        self.candidate_lobby_collection = []

    def candidate_lobby_login(self, candidate_id, candidate_login_link):

        self.candidate_lobby_collection = []
        __list = [self.candidate_login.open_link(candidate_login_link),
                  self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room(),
                  self.candidate_login.candidate_name_validate(self.xl_candidate_name),
                  self.candidate_login.almost_message(self.xl_almost_message),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0),
                  self.lobby.manage_candidates_tab(),
                  self.lobby.un_assign_room(),
                  self.lobby.ok_buttons(),
                  self.lobby.ok_buttons(),
                  self.candidate_login.open_link(candidate_login_link),
                  self.candidate_login.login_screen(candidate_id),
                  self.candidate_login.enter_to_room(),
                  self.candidate_login.candidate_name_validate(self.xl_candidate_name),
                  self.candidate_login.queued_message(self.xl_queued_message),
                  self.new_tab.window_close(),
                  self.new_tab.switch_to_window(0),
                  ]
        for func in __list:
            if func:
                self.candidate_lobby_collection.append(func)
            else:
                self.candidate_lobby_collection.append(func)
