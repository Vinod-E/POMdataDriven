from Config import inputFile
from utilities import excelRead, appTitle
from pageObjects.Pages.JobPages.JobGetByNamePage import JobGetByName


class CRPOJobGetBy:
    def __init__(self, driver, index, version):
        self.driver = driver

        self.tab_title = appTitle.Title(self.driver)
        self.job_getby = JobGetByName(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_config_excel'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_job_name = xl['job_name'][0].format(version)
        self.xl_job_getby_tab_title = xl['Job_getby_tab_title'][0]

        self.job_getby_collection = []

    def crpo_job_getby(self):
        self.job_getby_collection = []

        __list = [self.job_getby.job_tab_title(self.xl_job_getby_tab_title),
                  self.job_getby.job_name_validation(self.xl_job_name),
                  ]
        for func in __list:
            if func:
                self.job_getby_collection.append(func)
            else:
                self.job_getby_collection.append(func)
        print(self.job_getby_collection)
