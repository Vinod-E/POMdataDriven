from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.AssessementSlotPages import (SlotHeaderPage, ChooseSlotPage)


class AssessmentSlotApp:

    def __init__(self, driver, index):
        self.driver = driver
        self.captcha_screen = SlotHeaderPage.CaptchaScreenHeader(driver=driver)
        self.slot = ChooseSlotPage.ChooseSlot(driver=driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel_data = excelRead.ExcelRead()
        excel_data.read(inputFile.INPUT_PATH['assessment_slot'], index=index)
        xl = excel_data.excel_dict
        self.xl_slot = xl['slot'][0]
        self.xl_update_slot = xl['update_slot'][0]
        self.xl_message = xl['message'][0]

        self.entry_collection = []
        self.selection_collection = []
        self.update_selection_collection = []

    def slot_captcha_page_entry(self):
        self.entry_collection = []
        __list = [self.captcha_screen.assessment_slot_app_header(),
                  self.captcha_screen.next_button()
                  ]
        for func in __list:
            if func:
                self.entry_collection.append(func)
            else:
                self.entry_collection.append(func)

    def slot_selections(self):
        self.selection_collection = []
        __list = [self.slot.slot_selection(self.xl_slot),
                  self.slot.save_button(),
                  self.slot.success_message(self.xl_message)
                  ]
        for func in __list:
            if func:
                self.selection_collection.append(func)
            else:
                self.selection_collection.append(func)

    def update_slot_selections(self):
        self.update_selection_collection = []
        __list = [self.slot.update_slot(self.xl_update_slot),
                  self.slot.save_button(),
                  self.slot.success_message(self.xl_message)
                  ]
        for func in __list:
            if func:
                self.update_selection_collection.append(func)
            else:
                self.update_selection_collection.append(func)
