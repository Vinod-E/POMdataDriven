from Config import inputFile
from pageObjects.Pages.CandidatePages.customvaluesPage import CustomValuesDetailsPage
from pageObjects.Pages.MenuPages.candidatedetailsSubTabPages import CandidateSubTabs
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOCustomValues:

    def __init__(self, driver, index):
        self.driver = driver
        self.cp = CustomValuesDetailsPage(self.driver)
        self.cda = CandidateSubTabs(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cp_excel = excelRead.ExcelRead()
        cp_excel.read(inputFile.INPUT_PATH['microsite_CP'], index=index)
        xl = cp_excel.excel_dict
        self.xl_text = xl['text'][0]
        self.xl_textarea = xl['textarea'][0]

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cp_excel = excelRead.ExcelRead()
        cp_excel.read(inputFile.INPUT_PATH['microsite_ACP'], index=index)
        xl = cp_excel.excel_dict
        self.xl_ACP1 = xl['Rate'][0]
        self.xl_ACP2 = xl['WriteAbout'][0]
        self.xl_ACP3 = xl['Date'][0]
        self.xl_ACP4 = xl['InstituteName'][0]

        self.applicant_tpv_collection = []
        self.applicant_acp_collection = []

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

    def crpo_applicant_custom_properties(self):
        self.applicant_acp_collection = []
        __list = [self.cda.can_application_tab(),
                  self.cp.applicant_int_verified(self.xl_ACP1),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_acp_collection.append(func)
            else:
                self.applicant_acp_collection.append(func)
