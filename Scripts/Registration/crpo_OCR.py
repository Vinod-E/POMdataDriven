from Config import inputFile
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOOCRDetails:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        self.applicant_ocr_collection = []

    def crpo_ocr_applicant_verification(self):
        self.applicant_ocr_collection = []
        __list = [self.candidate.profile_photo_check(),
                  self.candidate.pan_photo_check(),
                  self.candidate.college_id_photo_check(),
                  self.candidate.communication_tab(),
                  self.candidate.arrow_down(),
                  self.candidate.id_card_verified(),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_ocr_collection.append(func)
            else:
                self.applicant_ocr_collection.append(func)
