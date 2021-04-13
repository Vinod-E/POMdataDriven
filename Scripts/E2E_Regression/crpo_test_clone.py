import ssl
from datetime import datetime
from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.AssessmentPages.CloneAssessmentPage import CloneAssessmentPage
from pageObjects.Pages.AssessmentPages.AssessmentGetByNamePage import AssessmentGetByName
from pageObjects.Pages.AssessmentPages.AssessmentActionsPage import Actions
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search


class CRPOAssessmentClone:
    def __init__(self, driver, index, version):
        now = datetime.now()
        self.__test_from_date = now.strftime("%d/%m/%Y")
        self.__test_to_date = now.strftime("%d/%m/%Y")
        self.driver = driver
        self.clone = CloneAssessmentPage(self.driver)
        self.search = Search(self.driver)
        self.get_by = AssessmentGetByName(self.driver)
        self.actions = Actions(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_excel = excelRead.ExcelRead()
        job_excel.read(inputFile.INPUT_PATH['assessment_excel'], index=index)
        xl = job_excel.excel_dict
        self.xl_new_test_name = xl['new_test'][0].format(version)
        self.xl_menu = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_clone_test_name = xl['clone_test_name'][0]
        self.xl_msg = xl['create_message'][0]

        # ---- Collection of all success items
        self.test_clone_collection = []

    def crpo_assessment_clone(self):
        self.test_clone_collection = []

        __list = [self.clone.assessment_tab(self.xl_menu, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.test_name_search_field(self.xl_clone_test_name),
                  self.search.search_button(),
                  self.get_by.test_name_click(self.xl_clone_test_name),
                  self.get_by.assessment_name_validation(self.xl_clone_test_name),
                  self.actions.assessment_actions_click(),
                  self.actions.clone_assessment(),
                  self.clone.new_test_name(self.xl_new_test_name),
                  self.clone.test_from_date(self.__test_from_date),
                  self.clone.test_to_date(self.__test_to_date),
                  self.clone.clone_test_button(),
                  self.clone.clone_assessment_notifier(self.xl_msg),
                  self.clone.clone_assessment_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.test_clone_collection.append(func)
            else:
                self.test_clone_collection.append(func)
