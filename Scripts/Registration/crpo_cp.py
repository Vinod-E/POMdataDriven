from Config import inputFile
from pageObjects.Pages.CandidatePages.customvaluesPage import CustomValuesDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOCustomValues:

    def __init__(self, driver, index):
        self.driver = driver
        self.cp = CustomValuesDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cp_excel = excelRead.ExcelRead()
        cp_excel.read(inputFile.INPUT_PATH['microsite_CP'], index=index)
        xl = cp_excel.excel_dict
        self.xl_text = xl['text'][0]
        self.xl_textarea = xl['textarea'][0]

        self.applicant_tpv_collection = []

    def crpo_applicant_text_textarea_values(self):
        self.applicant_tpv_collection = []
        __list = [self.cp.text_value_verified(self.xl_text, 1),
                  self.cp.text_value_verified(self.xl_text, 5),
                  self.cp.text_value_verified(self.xl_text, 12),
                  self.cp.text_value_verified(self.xl_text, 16),
                  self.cp.text_value_verified(self.xl_text, 22),
                  self.cp.textarea_value_verified(self.xl_textarea, 1),
                  self.cp.textarea_value_verified(self.xl_textarea, 3),
                  self.cp.textarea_value_verified(self.xl_textarea, 4),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_tpv_collection.append(func)
            else:
                self.applicant_tpv_collection.append(func)
