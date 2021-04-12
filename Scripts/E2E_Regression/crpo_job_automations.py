from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MenuPages.jobSubTabPages import JobSubTabs
from pageObjects.Pages.JobPages.JobAutomationsPage import JobAutomations


class CRPOJobAutomations:
    def __init__(self, driver, index):
        self.driver = driver
        self.job_sub_tab = JobSubTabs(self.driver)
        self.automations = JobAutomations(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_automation'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_reg_stage = xl['reg_stage'][0]
        self.xl_reg_status = xl['reg_status'][0]
        self.xl_eli_stage = xl['eli_stage'][0]
        self.xl_eli_status = xl['eli_status'][0]
        self.xl_offer_stage = xl['offer_stage'][0]
        self.xl_offer_status = xl['offer_status'][0]
        self.xl_message = xl['message'][0]

        self.job_automations_collection = []

    def crpo_job_automations(self):
        self.job_automations_collection = []

        __list = [self.job_sub_tab.job_automation(),
                  self.automations.registration_stage(),
                  self.automations.hop_stage(self.xl_reg_stage),
                  self.automations.hop_status(self.xl_reg_status),
                  self.automations.eligibility_stage(),
                  self.automations.hop_stage(self.xl_eli_stage),
                  self.automations.hop_status(self.xl_eli_status),
                  self.automations.offer_stage(),
                  self.automations.hop_stage(self.xl_offer_stage),
                  self.automations.hop_status(self.xl_offer_status),
                  self.automations.all_round_button_on(),
                  self.automations.automation_save(),
                  self.automations.job_automation_save_notifier(self.xl_message),
                  self.automations.job_automations_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_automations_collection.append(func)
            else:
                self.job_automations_collection.append(func)
