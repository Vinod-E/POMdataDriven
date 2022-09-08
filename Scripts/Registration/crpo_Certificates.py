from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOCertificate:

    def __init__(self, driver, index):
        self.driver = driver
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite_certificate'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_c1_name = xl['c1_name'][0]
        self.xl_c2_name = xl['c2_name'][0]

        self.applicant_certificate_collection = []

    def crpo_applicant_certificate(self):
        self.applicant_certificate_collection = []
        __list = [self.candidate.certificates_details_check(self.xl_c1_name, 1),
                  self.candidate.certificates_details_check(self.xl_c2_name, 2),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_certificate_collection.append(func)
            else:
                self.applicant_certificate_collection.append(func)
