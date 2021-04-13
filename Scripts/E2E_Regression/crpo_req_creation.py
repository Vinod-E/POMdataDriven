from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.MenuPages.requirementSubTabPages import RequirementSubTabs
from pageObjects.Pages.RequirementPages.CreateRequirementPage import RequirementCreationPage
from pageObjects.Pages.RequirementPages.RequirementDuplicityConfig import DuplicityCheck


class CRPOReqCreation:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.req = RequirementCreationPage(self.driver)
        self.multi_value = MultiSelectValues(self.driver)
        self.tab = RequirementSubTabs(self.driver)
        self.duplicity = DuplicityCheck(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_excel = excelRead.ExcelRead()
        job_excel.read(inputFile.INPUT_PATH['requirement_excel'], index=index)
        xl = job_excel.excel_dict
        self.xl_req_name = xl['name'][0].format(version)
        self.xl_menu = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_track = xl['track'][0]
        self.xl_type = xl['type'][0]
        self.xl_msg = xl['message'][0]
        self.xl_duplicity = xl['duplicity'][0]
        self.xl_duplicity_msg = xl['duplicity_msg'][0]

        # ---- Collection of all success items
        self.req_create_collection = []
        self.req_config_collection = []

    def crpo_req_creation(self):
        self.req_create_collection = []

        __list = [self.req.requirement_tab(self.xl_menu, self.xl_tab_title),
                  self.req.create_button(),
                  self.req.requirement_name(self.xl_req_name),
                  self.req.requirement_job(),
                  self.multi_value.search(self.xl_req_name),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.req.requirement_hiring(self.xl_track),
                  self.req.requirement_type(self.xl_type),
                  self.req.requirement_create(),
                  self.req.req_creation_notifier(self.xl_msg),
                  self.req.req_creation_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.req_create_collection.append(func)
            else:
                self.req_create_collection.append(func)

    def crpo_req_configuration(self):
        self.req_config_collection = []

        __list = [self.tab.requirement_configurations(),
                  self.tab.requirement_duplicity(),
                  self.duplicity.do_not_allow_duplicates(self.xl_duplicity),
                  self.duplicity.req_duplicity_notifier(self.xl_duplicity_msg),
                  self.duplicity.req_duplicity_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.req_config_collection.append(func)
            else:
                self.req_config_collection.append(func)
