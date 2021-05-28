from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.candidateLoginTabPages import CandidateLoginMenus
from pageObjects.Pages.EmbraceCandidatePages.RaiseQuery import CandidateQueryPage


class CandidateQueryRaise:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = CandidateLoginMenus(self.driver)
        self.query_raise = CandidateQueryPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        query_excel = excelRead.ExcelRead()
        query_excel.read(inputFile.INPUT_PATH['candidate_queries'], index=index)
        xl = query_excel.excel_dict
        self.xl_help_menu = xl['help_menu'][0]

        self.query_collection = []

    def candidate_queries(self):
        self.query_collection = []
        __list = [self.menu.help_tab(self.xl_help_menu),
                  self.query_raise.more_queries_button(),
                  ]
        for func in __list:
            if func:
                self.query_collection.append(func)
            else:
                self.query_collection.append(func)
