from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.ManageNominationPages.NominationPage import EventNominationTabPage


class CRPONominations:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.nomination = EventNominationTabPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['manage_interviewers'], index=index)
        xl = status_excel.excel_dict
        self.xl_jr = xl['jobrole'][0].format(version)
        self.xl_menu = xl['menu'][0]
        self.xl_menu_title = xl['menu_title'][0]

        self.int_acceptance_collection = []

    def nomination_confirmation(self):
        self.int_acceptance_collection = []
        __list = [self.menu.nominations_tab(self.xl_menu, self.xl_menu_title),
                  self.nomination.event_row_arrow_down(),
                  self.nomination.nomination_job_validation(self.xl_jr),
                  self.nomination.confirm_interviewer_nomination(),
                  self.nomination.ok_confirm(),
                  self.nomination.nomination_accept_validation()
                  ]
        for func in __list:
            if func:
                self.int_acceptance_collection.append(func)
            else:
                self.int_acceptance_collection.append(func)
