from Config import inputFile
from pageObjects.Pages.MenuPages.menuPage import Menu
from utilities import excelRead
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.RequirementPages.RequirementGetByNamePage import RequirementGetByName
from pageObjects.Pages.MenuPages.requirementSubTabPages import RequirementSubTabs


class CrpoRequirementSearch:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = RequirementGetByName(self.driver)
        self.sub_tab = RequirementSubTabs(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['requirement_excel'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_req_name = xl['name'][0].format(version)

        self.help_desk_collection = []

    def requirement_search(self):
        self.help_desk_collection = []
        __list = [self.menu.requirement_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_req_name),
                  self.search.search_button(),
                  self.getby.req_name_click(self.xl_req_name),
                  self.getby.req_name_validation(self.xl_req_name),
                  self.sub_tab.requirement_configurations(),
                  self.sub_tab.requirement_query()
                  ]
        for func in __list:
            if func:
                self.help_desk_collection.append(func)
            else:
                self.help_desk_collection.append(func)
