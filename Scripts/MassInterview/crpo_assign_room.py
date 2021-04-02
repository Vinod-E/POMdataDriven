from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.EventLobbyPage import LobbyPage
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search


class AssignRoom:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.lobby = LobbyPage(self.driver)
        self.search = Search(self.driver)
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_room'], index=index)
        xl = status_excel.excel_dict
        self.xl_room_name = xl['room_name'][0].format(version)
        self.xl_tag_room_message = xl['no_candidate_tagged'][0]

        self.assign_room_collection = []

    def assign_room(self):

        self.assign_room_collection = []
        __list = [self.search.manage_candidate_search(),
                  self.lobby.room_search_filed(),
                  self.lobby.search(self.xl_room_name),
                  self.lobby.move_all(),
                  self.lobby.done(),
                  self.lobby.search_button(),
                  self.lobby.no_candidate_message(self.xl_tag_room_message),
                  self.lobby.assign_room_action(),
                  self.lobby.room_name_field(self.xl_room_name),
                  self.lobby.room_assigning_action(),
                  self.lobby.ok_buttons(),
                  self.search.manage_candidate_search(),
                  self.lobby.room_search_filed(),
                  self.lobby.search(self.xl_room_name),
                  self.lobby.move_all(),
                  self.lobby.done(),
                  self.lobby.search_button(),
                  self.lobby.candidate_info(self.xl_room_name)
                  ]
        for func in __list:
            if func:
                self.assign_room_collection.append(func)
            else:
                self.assign_room_collection.append(func)
