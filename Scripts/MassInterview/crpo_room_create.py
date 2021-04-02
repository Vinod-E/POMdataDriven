from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventLobbyPage import LobbyPage


class Room:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.action = Actions(self.driver)
        self.lobby = LobbyPage(self.driver)
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_room'], index=index)
        xl = status_excel.excel_dict
        self.xl_room_name = xl['room_name'][0].format(version)
        self.xl_int1 = xl['int1'][0]
        self.xl_int2 = xl['int2'][0]
        self.xl_message = xl['message'][0]
        self.xl_active_message = xl['active_message'][0]

        self.room_collection = []

    def create_room(self):

        self.room_collection = []
        __list = [self.action.event_actions_click(),
                  self.action.event_lobby(),
                  self.lobby.create_room_button(),
                  self.lobby.room_name(self.xl_room_name),
                  self.lobby.select_interviewers(),
                  self.lobby.search(self.xl_int1),
                  self.lobby.move_all(),
                  self.lobby.done(),
                  self.lobby.select_participants(),
                  self.lobby.search(self.xl_int2),
                  self.lobby.move_all(),
                  self.lobby.done(),
                  self.lobby.created_button(self.xl_message),
                  self.lobby.active_room(),
                  self.lobby.ok_button(self.xl_active_message)
                  ]
        for func in __list:
            if func:
                self.room_collection.append(func)
            else:
                self.room_collection.append(func)
