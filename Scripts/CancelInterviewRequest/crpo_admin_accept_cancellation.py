from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs
from pageObjects.Pages.EventPages.EventCancelRequestPage import EventCancelRequest


class CrpoAdminAccept:

    def __init__(self, driver, index):
        self.driver = driver
        self.event_tab = EventSubTabs(self.driver)
        self.admin_approve = EventCancelRequest(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cancel_excel = excelRead.ExcelRead()
        cancel_excel.read(inputFile.INPUT_PATH['cancel_interview'], index=index)
        xl = cancel_excel.excel_dict
        self.xl_comment = xl['comment'][0]
        self.xl_message = xl['approve_request_message'][0]

        self.admin_accept_collection = []

    def admin_accept_cancellation(self):
        self.admin_accept_collection = []
        __list = [self.event_tab.tracking(),
                  self.event_tab.cancel_request_tab(),
                  self.admin_approve.accept_cancellation(),
                  self.admin_approve.cancel_request_comment(self.xl_comment),
                  self.admin_approve.confirm_request(),
                  self.admin_approve.go_ahead_with_lobby_screen(),
                  self.admin_approve.lobby_accept_cancellation(),
                  self.admin_approve.cancel_request_comment(self.xl_comment),
                  self.admin_approve.lobby_confirm_request(),
                  self.admin_approve.acceptance_notifier(self.xl_message),
                  self.admin_approve.acceptance_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.admin_accept_collection.append(func)
            else:
                self.admin_accept_collection.append(func)
