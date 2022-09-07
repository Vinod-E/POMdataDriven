from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOEducation:

    def __init__(self, driver, index):
        self.driver = driver
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        education_excel = excelRead.ExcelRead()
        education_excel.read(inputFile.INPUT_PATH['microsite_education'], index=index)
        xl = education_excel.excel_dict
        self.xl_pg_degree = xl['pg_degree'][0]
        self.xl_ug_degree = xl['ug_degree'][0]
        self.xl_tenth_type = xl['tenth_type'][0]

        self.applicant_education_collection = []

    def crpo_applicant_education(self):
        self.applicant_education_collection = []
        __list = [self.candidate.education_details_check(self.xl_pg_degree, 1),
                  self.candidate.education_details_check(self.xl_ug_degree, 2),
                  self.candidate.education_details_check("12th", 3),
                  self.candidate.education_details_check(self.xl_tenth_type, 4),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_education_collection.append(func)
            else:
                self.applicant_education_collection.append(func)
