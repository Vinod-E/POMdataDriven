from Config import inputFile
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.EventPages.EventApplicantActions import EventApplicantActions
from utilities import excelRead, SwitchWindow


class CRPOEventSearch:

    def __init__(self, driver, index):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = Search(self.driver)
        self.get_by = EventGetByName(self.driver)
        self.action = Actions(self.driver)
        self.applicant_grid = EventApplicant(self.driver)
        self.applicant_action = EventApplicantActions(self.driver)
        self.switch_window = SwitchWindow.SwitchWindowClose(self.driver)

        self.event_search_collection = []
        self.event_applicant_collection = []
        self.event_interview_collection = []

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        excel = excelRead.ExcelRead()
        excel.read(inputFile.INPUT_PATH['revise_feedback'], index=index)
        xl = excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0]
        self.xl_applicant_name = xl['applicant_name'][0]

    def crpo_search_event(self):
        self.event_search_collection = []
        __list = [self.menu.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.get_by.event_name_click(),
                  self.get_by.event_name_validation(self.xl_event_name)
                  ]
        for func in __list:
            if func:
                self.event_search_collection.append(func)
            else:
                self.event_search_collection.append(func)

    def crpo_applicant_search(self):
        self.event_applicant_collection = []
        __list = [self.action.event_actions_click(),
                  self.action.event_view_candidates(),
                  self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_applicant_name),
                  self.search.search_button()
                  ]
        for func in __list:
            if func:
                self.event_applicant_collection.append(func)
            else:
                self.event_applicant_collection.append(func)

    def crpo_event_interviews(self):
        self.event_interview_collection = []
        __list = [self.action.event_actions_click(),
                  self.action.event_interviews(),
                  self.search.advance_search(),
                  self.search.candidate_name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.applicant_grid.select_applicant(),
                  self.applicant_action.provide_feedback_action(),
                  self.switch_window.switch_to_window(1)
                  ]
        for func in __list:
            if func:
                self.event_interview_collection.append(func)
            else:
                self.event_interview_collection.append(func)
