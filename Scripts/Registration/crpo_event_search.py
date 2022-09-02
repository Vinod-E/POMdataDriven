from Config import inputFile
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from pageObjects.Pages.MenuPages.menuPage import Menu
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CRPOEventSearch:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = Search(self.driver)
        self.get_by = EventGetByName(self.driver)
        self.action = Actions(self.driver)
        self.applicant = EventApplicant(self.driver)
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_excel'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]

    # ---------------------- Certificate Excel data Read ---------------------------------------
        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite_certificate'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_event_name = xl['event_name'][0]
        self.xl_c1_name = xl['c1_name'][0]
        self.xl_c2_name = xl['c2_name'][0]

    # ---------------------- Education Excel data Read ---------------------------------------
        education_excel = excelRead.ExcelRead()
        education_excel.read(inputFile.INPUT_PATH['microsite_education'], index=index)
        xl = education_excel.excel_dict
        self.xl_pg_degree = xl['pg_degree'][0]
        self.xl_ug_degree = xl['ug_degree'][0]
        self.xl_twelfth_type = xl['twelfth_type'][0]
        self.xl_tenth_type = xl['tenth_type'][0]

    # ---------------------- OCR Excel data Read ---------------------------------------
        education_excel = excelRead.ExcelRead()
        education_excel.read(inputFile.INPUT_PATH['microsite_OCR'], index=index)
        xl = education_excel.excel_dict
        self.xl_first = xl['first_name'][0].format(version)
        self.xl_middle = xl['middle_name'][0]
        self.xl_last = xl['last_name'][0]
        self.full_name = self.xl_first + ' ' + self.xl_middle + ' ' + self.xl_last
        print(self.full_name)

        self.event_search_collection = []
        self.applicant_search_collection = []
        self.applicant_full_search_collection = []
        self.applicant_education_collection = []
        self.applicant_certificate_collection = []
        self.applicant_ocr_collection = []

    def crpo_search_event(self):
        self.event_search_collection = []
        __list = [self.menu.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.get_by.event_name_click(),
                  self.get_by.event_name_validation(self.xl_event_name),
                  self.action.event_actions_click(),
                  self.action.event_view_candidates()
                  ]
        for func in __list:
            if func:
                self.event_search_collection.append(func)
            else:
                self.event_search_collection.append(func)

    def crpo_search_applicant(self):
        self.applicant_search_collection = []
        __list = [self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_name),
                  self.search.applicant_search_button(),
                  self.applicant.applicant_get_name(self.xl_name, 1)
                  ]
        for func in __list:
            if func:
                self.applicant_search_collection.append(func)
            else:
                self.applicant_search_collection.append(func)

    def crpo_full_search_applicant(self):
        self.applicant_full_search_collection = []
        __list = [self.search.advance_search(),
                  self.search.name_field_applicant(self.full_name),
                  self.search.applicant_search_button(),
                  self.applicant.applicant_get_name(self.full_name, 1)
                  ]
        for func in __list:
            if func:
                self.applicant_full_search_collection.append(func)
            else:
                self.applicant_full_search_collection.append(func)

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
