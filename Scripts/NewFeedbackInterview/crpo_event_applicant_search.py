from Config import inputFile
from pageObjects.Pages.MenuPages.menuPage import Menu
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.EventPages import EventGetByNamePage, EventActionsPage


class CrpoNewEvent:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_status_change'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0].format(version)

        self.event_search_collection = []

    def new_feed_event_applicant_search(self):
        self.event_search_collection = []
        __list = [self.menu.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event_name),
                  self.event_action.event_actions_click(),
                  self.event_action.event_view_candidates(),
                  self.search.advance_search(),
                  self.search.name_field_applicant(self.xl_event_name),
                  self.search.applicant_search_button()
                  ]
        for func in __list:
            if func:
                self.event_search_collection.append(func)
            else:
                self.event_search_collection.append(func)
