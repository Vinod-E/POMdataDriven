from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.candidateLoginTabPages import CandidateLoginMenus
from pageObjects.Pages.EmbraceCandidatePages.RaiseQuery import CandidateQueryPage


class CandidateQueryRaise:

    def __init__(self, driver, index):
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
        self.xl_category_1 = xl['category1'][0]
        self.xl_category_2 = xl['category2'][0]
        self.xl_category_3 = xl['category3'][0]
        self.xl_subject = xl['subject'][0]
        self.xl_message = xl['message'][0]
        self.xl_notifier = xl['notifier'][0]

        self.query_1_collection = []
        self.query_2_collection = []
        self.query_3_collection = []

    def candidate_query_1(self):
        self.query_1_collection = []
        __list = [self.menu.help_tab(self.xl_help_menu),
                  self.query_raise.more_queries_button(),
                  self.query_raise.category_select(self.xl_category_1),
                  self.query_raise.subject_entry(self.xl_subject),
                  self.query_raise.message_entry(self.xl_message),
                  self.query_raise.query_raise_button(),
                  self.query_raise.query_raise_notifier(self.xl_notifier),
                  self.query_raise.query_raise_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.query_1_collection.append(func)
            else:
                self.query_1_collection.append(func)

    def candidate_query_2(self):
        self.query_2_collection = []
        __list = [self.menu.help_tab(self.xl_help_menu),
                  self.query_raise.more_queries_button(),
                  self.query_raise.category_select(self.xl_category_2),
                  self.query_raise.subject_entry(self.xl_subject),
                  self.query_raise.message_entry(self.xl_message),
                  self.query_raise.query_raise_button(),
                  self.query_raise.query_raise_notifier(self.xl_notifier),
                  self.query_raise.query_raise_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.query_2_collection.append(func)
            else:
                self.query_2_collection.append(func)

    def candidate_query_3(self):
        self.query_3_collection = []
        __list = [self.menu.help_tab(self.xl_help_menu),
                  self.query_raise.more_queries_button(),
                  self.query_raise.category_select(self.xl_category_3),
                  self.query_raise.subject_entry(self.xl_subject),
                  self.query_raise.message_entry(self.xl_message),
                  self.query_raise.query_raise_button(),
                  self.query_raise.query_raise_notifier(self.xl_notifier),
                  self.query_raise.query_raise_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.query_3_collection.append(func)
            else:
                self.query_3_collection.append(func)
