from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventOwnerConfigPage import EventOwnersConfigPage


class CRPOEventOwners:

    def __init__(self, driver, index):
        self.driver = driver
        self.action = Actions(self.driver)
        self.multi_value = MultiSelectValues(self.driver)
        self.owners = EventOwnersConfigPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_excel'], index=index)
        xl = status_excel.excel_dict
        self.xl_owners_message = xl['owners_update_message'][0]

        self.event_owners_collection = []

    def crpo_event_owners_tagging(self):
        self.event_owners_collection = []
        __list = [self.action.event_actions_click(),
                  self.action.manage_event_owners(),
                  self.multi_value.move_all_items(),
                  self.owners.event_owners_update(),
                  self.owners.event_owners_notifier(self.xl_owners_message),
                  self.owners.event_owners_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.event_owners_collection.append(func)
            else:
                self.event_owners_collection.append(func)
