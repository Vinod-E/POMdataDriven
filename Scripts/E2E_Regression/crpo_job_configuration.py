from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.jobSubTabPages import JobSubTabs
from pageObjects.Pages.JobPages.ActivityTaskConfigPage import ActivityTaskConfigPage
from pageObjects.Pages.JobPages.EligibilityCriteriaConfigPage import EligibilityCriteriaPage
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues


class CRPOJobConfiguration:
    def __init__(self, driver, index):
        self.driver = driver
        self.job_sub_tab = JobSubTabs(self.driver)
        self.job_ec = EligibilityCriteriaPage(self.driver)
        self.job_task = ActivityTaskConfigPage(self.driver)
        self.multi_value = MultiSelectValues(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_config_excel'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_ec = xl['eligibility_criteria'][0]
        self.xl_ec_stage = xl['Ec stage'][0]
        self.xl_positive = xl['Positive status'][0]
        self.xl_negative = xl['Negative status'][0]
        self.xl_ec_notifier = xl['notifier'][0]

        self.xl_stage_status = xl['offer_stage_status'][0]
        self.xl_positive_status = xl['offer_positive'][0]
        self.xl_negative_status = xl['offer_negative'][0]
        self.xl_activity = xl['activity1'][0]
        self.xl_task = xl['activity1_task1'][0]
        self.xl_task_notifier = xl['task_notifier'][0]

        self.job_ec_collection = []
        self.job_task_collection = []

    def crpo_job_ec_configuration(self):
        self.job_ec_collection = []

        __list = [self.job_sub_tab.job_configurations(),
                  self.job_ec.job_configure_button(),
                  self.job_ec.job_ec_field(self.xl_ec),
                  self.job_ec.job_positive_stage_field(self.xl_ec_stage),
                  self.job_ec.job_positive_status_field(self.xl_positive),
                  self.job_ec.job_negative_stage_field(self.xl_ec_stage),
                  self.job_ec.job_negative_status_field(self.xl_negative),
                  self.job_ec.job_ec_save(),
                  self.job_ec.job_ec_notifier(self.xl_ec_notifier),
                  self.job_ec.job_ec_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_ec_collection.append(func)
            else:
                self.job_ec_collection.append(func)

    def crpo_job_task_configuration(self):
        self.job_task_collection = []

        __list = [self.job_task.job_task_configure_button(),
                  self.job_task.task_new_row(),
                  self.job_task.job_activity_stage_field(self.xl_stage_status),
                  self.job_task.job_activity_positive_stage_field(self.xl_positive_status),
                  self.job_task.job_activity_negative_stage_field(self.xl_negative_status),
                  self.job_task.job_activity_field(self.xl_activity),
                  self.job_task.job_task_field(),
                  self.multi_value.search(self.xl_task),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.job_task.job_activity_task_save(),
                  self.job_task.job_task_notifier(self.xl_task_notifier),
                  self.job_task.job_task_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_task_collection.append(func)
            else:
                self.job_task_collection.append(func)
