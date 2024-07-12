from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.CandidateChooseSlot import (SlotHeaderPage, ChooseSlotPage)


class ChooseSlotApp:

    def __init__(self, driver, index):
        self.driver = driver
        self.captcha_screen = SlotHeaderPage.CaptchaScreenHeader(driver=driver)
        self.slot = ChooseSlotPage.ChooseSlot(driver=driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel_data = excelRead.ExcelRead()
        excel_data.read(inputFile.INPUT_PATH['choose_slot'], index=index)
        xl = excel_data.excel_dict
        self.xl_slot_one = xl['slot_one'][0]
        self.xl_slot_two = xl['slot_two'][0]

        self.entry_collection = []
        self.choose_collection = []
        self.update_choose_collection = []

    def slot_captcha_page_entry(self):
        self.entry_collection = []
        __list = [self.captcha_screen.next_button()
                  ]
        for func in __list:
            if func:
                self.entry_collection.append(func)
            else:
                self.entry_collection.append(func)

    def slot_selections(self):
        self.choose_collection = []
        __list = [self.slot.choose_one_selection(),
                  self.slot.reset_button(),
                  self.slot.choose_two_selection(),
                  self.slot.submit_button(),
                  self.slot.thank_you_page()
                  ]
        for func in __list:
            if func:
                self.choose_collection.append(func)
            else:
                self.choose_collection.append(func)

    def update_choose_slot_selection(self):
        self.update_choose_collection = []
        __list = [self.slot.update_slot(self.xl_slot_two),
                  self.slot.submit_button(),
                  self.slot.thank_you_page()
                  ]
        for func in __list:
            if func:
                self.update_choose_collection.append(func)
            else:
                self.update_choose_collection.append(func)
