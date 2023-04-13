from Config import inputFile
from pageObjects.Pages.CandidatePages.WorkProfilePage import WorkProfileDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOWorkProfile:

    def __init__(self, driver, index):
        self.driver = driver
        self.wp = WorkProfileDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        wf_excel = excelRead.ExcelRead()
        wf_excel.read(inputFile.INPUT_PATH['microsite_WorkProfile'], index=index)
        xl = wf_excel.excel_dict
        self.xl_wp1_company = xl['wp1_company'][0]
        self.xl_wp1_designation = xl['wp1_designation'][0]
        self.xl_wp2_company = xl['wp2_company'][0]
        self.xl_wp2_designation = xl['wp2_designation'][0]

        self.applicant_wp_collection = []

    def crpo_applicant_workprofile(self):
        self.applicant_wp_collection = []
        __list = [self.wp.wp1_company_verified(self.xl_wp2_company),
                  self.wp.wp1_design_verified(self.xl_wp2_designation),
                  self.wp.wp2_company_verified(self.xl_wp1_company),
                  self.wp.wp2_design_verified(self.xl_wp1_designation),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_wp_collection.append(func)
            else:
                self.applicant_wp_collection.append(func)
