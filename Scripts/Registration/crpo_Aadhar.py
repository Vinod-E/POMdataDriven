from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOAadhar:

    def __init__(self, driver, index):
        self.driver = driver
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        aadhar_excel = excelRead.ExcelRead()
        aadhar_excel.read(inputFile.INPUT_PATH['microsite_Aadhar'], index=index)
        xl = aadhar_excel.excel_dict
        self.xl_aadhar_num = xl['AadharNumber'][0]

        self.applicant_aadhar_collection = []

    def crpo_applicant_aadhar(self):
        self.applicant_aadhar_collection = []
        __list = [self.candidate.aadhar_numbers(self.xl_aadhar_num),
                  self.candidate.communication_tab(),
                  self.candidate.arrow_down(),
                  self.candidate.aadhar_verified(),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_aadhar_collection.append(func)
            else:
                self.applicant_aadhar_collection.append(func)
