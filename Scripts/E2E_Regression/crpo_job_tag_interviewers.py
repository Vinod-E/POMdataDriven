from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.JobPages.JobActionsPage import Actions
from pageObjects.Pages.JobPages.JobInterviewersPage import TagInterviewersPage
from pageObjects.Pages.MenuPages.jobSubTabPages import JobSubTabs


class CRPOJobTagInterviewers:
    def __init__(self, driver, index):
        self.driver = driver
        self.actions = Actions(self.driver)
        self.int = TagInterviewersPage(self.driver)
        self.job_tab = JobSubTabs(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_config_excel'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_job_int = xl['interviewers'][0]
        self.xl_job_int_tag_msg = xl['int_tag_message'][0]
        self.xl_job_owners = xl['total_owners'][0]

        self.job_tag_int_collection = []

    def crpo_job_tag_interviewers(self):
        self.job_tag_int_collection = []

        __list = [self.actions.job_actions_click(),
                  self.actions.job_tag_interviewers(),
                  self.int.job_int_panel(self.xl_job_int),
                  self.int.job_int_add(),
                  self.int.job_int_save(),
                  self.int.job_tag_int_notifier(self.xl_job_int_tag_msg),
                  self.int.job_tag_int_notifier_dismiss(),
                  self.job_tab.job_owners(),
                  self.int.total_tag_interviewers(self.xl_job_owners)
                  ]
        for func in __list:
            if func:
                self.job_tag_int_collection.append(func)
            else:
                self.job_tag_int_collection.append(func)
