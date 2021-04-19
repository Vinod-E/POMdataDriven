from Config import inputFile
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.EmbracePages.CandidatePage import CandidatePage
from pageObjects.Pages.EmbracePages.CandidateSearchPage import CandidateSearchPage


class CRPOEmbraceTask:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = CandidateSearchPage(self.driver)
        self.task = CandidatePage(self.driver)
        self.window_switch = SwitchWindow.SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['embrace'], index=index)
        xl = status_excel.excel_dict
        self.xl_more_menu = xl['menu1'][0]
        self.xl_embrace_candidate_tab = xl['menu2'][0]
        self.xl_candidate_name = xl['name'][0].format(version)
        self.xl_message = xl['submit_message'][0]

        self.event_mbrace_collection = []

    def crpo_embrace_behalf_of_candidate(self):
        self.event_mbrace_collection = []

        __list = [self.menu.more_tab(self.xl_more_menu),
                  self.menu.embrace_tab(),
                  self.window_switch.switch_to_window(1),
                  self.menu.embrace_candidate_tab(),
                  self.search.advance_search(),
                  self.search.candidate_name_field(self.xl_candidate_name),
                  self.search.advance_search_button(),
                  self.task.behalf_of_submit_task(),
                  self.task.candidate_acceptance_yes(),
                  self.task.submit_task(),
                  self.task.submit_task_notifier(self.xl_message),
                  self.task.submit_task_notifier_dismiss(),
                  self.window_switch.window_close(),
                  self.window_switch.switch_to_window(0)
                  ]
        for func in __list:
            if func:
                self.event_mbrace_collection.append(func)
            else:
                self.event_mbrace_collection.append(func)
