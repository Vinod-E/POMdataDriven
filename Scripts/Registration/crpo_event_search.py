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

        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_event_name = xl['event_name'][0]
        self.xl_c1_name = xl['c1_name'][0]
        self.xl_c2_name = xl['c2_name'][0]

        self.event_search_collection = []
        self.applicant_search_collection = []

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
                  self.applicant.applicant_get_name(self.xl_name, 1),
                  self.candidate.certificates_details_check(self.xl_c1_name, 1),
                  self.candidate.certificates_details_check(self.xl_c2_name, 2),
                  self.switch_window.window_close(),
                  self.switch_window.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.applicant_search_collection.append(func)
            else:
                self.applicant_search_collection.append(func)
