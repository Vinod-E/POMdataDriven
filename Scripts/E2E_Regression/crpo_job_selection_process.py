from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.JobPages.JobActionsPage import Actions
from pageObjects.Pages.JobPages.SelectionProcessPage import SelectionProcessPage


class CRPOJobSelectionProcess:
    def __init__(self, driver, index):
        self.driver = driver
        self.actions = Actions(self.driver)
        self.sp = SelectionProcessPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_config_excel'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_job_sp = xl['job_sp'][0]
        self.xl_sp_notifier = xl['notifier'][0]

        self.job_sp_collection = []

    def crpo_job_selection_process(self):
        self.job_sp_collection = []

        __list = [self.actions.job_actions_click(),
                  self.actions.tag_selection_process(),
                  self.sp.job_sp(self.xl_job_sp),
                  self.sp.job_sp_save(),
                  self.sp.job_sp_notifier(self.xl_sp_notifier),
                  self.sp.page_refresh()
                  ]
        for func in __list:
            if func:
                self.job_sp_collection.append(func)
            else:
                self.job_sp_collection.append(func)
