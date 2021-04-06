from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.JobPages.CreateJobPage import JobCreationPage


class CRPOJobCreation:
    def __init__(self, driver, index, version):
        self.driver = driver

        self.job = JobCreationPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_excel = excelRead.ExcelRead()
        job_excel.read(inputFile.INPUT_PATH['job_excel'], index=index)
        xl = job_excel.excel_dict
        self.xl_job_name = xl['job_name'][0].format(version)
        self.xl_job_desc = xl['job_description'][0]
        self.xl_job_loc = xl['job_location'][0]
        self.xl_job_hm = xl['job_hm'][0]
        self.xl_job_bu = xl['job_bu'][0]
        self.xl_job_openings = xl['job_openings'][0]
        self.xl_job_male = xl['job_male'][0]
        self.xl_job_female = xl['job_female'][0]
        self.xl_job_create_tab_title = xl['job_tab_title'][0]
        self.xl_job_menu = xl['job_menu'][0]
        self.xl_job_attach_message = xl['job_attachment_message'][0]
        self.xl_job_create_message = xl['job_create_message'][0]

        # ---- Attachment from local machine
        self.job_attachment_file = inputFile.INPUT_PATH['job_attachment']

        # ---- Collection of all success items
        self.job_create_collection = []

    def crpo_job_creation(self):
        self.job_create_collection = []

        __list = [self.job.job_tab(self.xl_job_menu, self.xl_job_create_tab_title),
                  self.job.create_button(),
                  self.job.job_name(self.xl_job_name),
                  self.job.job_attachment(self.job_attachment_file),
                  self.job.job_notifier(self.xl_job_attach_message),
                  self.job.job_description(self.xl_job_desc),
                  self.job.job_location(self.xl_job_loc),
                  self.job.job_hiring_manager(self.xl_job_hm),
                  self.job.job_business_unit(self.xl_job_bu),
                  self.job.job_openings(self.xl_job_openings),
                  self.job.job_male_diversity(self.xl_job_male),
                  self.job.job_female_diversity(self.xl_job_female),
                  self.job.job_create(),
                  self.job.job_notifier(self.xl_job_create_message)
                  ]
        for func in __list:
            if func:
                self.job_create_collection.append(func)
            else:
                self.job_create_collection.append(func)
