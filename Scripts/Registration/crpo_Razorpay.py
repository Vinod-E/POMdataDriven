from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPORazorPay:

    def __init__(self, driver, index):
        self.driver = driver
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        razorpay_excel = excelRead.ExcelRead()
        razorpay_excel.read(inputFile.INPUT_PATH['microsite_razorpay'], index=index)
        xl = razorpay_excel.excel_dict
        self.xl_payment_status = xl['payment_status'][0]

        self.applicant_payment_collection = []

    def crpo_applicant_payment(self):
        self.applicant_payment_collection = []
        __list = [self.candidate.candidate_status(self.xl_payment_status),
                  self.candidate.payment_tab(),
                  self.candidate.arrow_down(),
                  self.candidate.order_id_verified(),
                  self.candidate.payment_id_verified(),
                  self.candidate.payment_completed_verified(),
                  self.candidate.payment_captured_verified(),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_payment_collection.append(func)
            else:
                self.applicant_payment_collection.append(func)
