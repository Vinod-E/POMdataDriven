from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.JobPages.JobActionsPage import Actions
from pageObjects.Pages.JobPages.JobFeedbackConfigPage import FeedbackConfigPage


class CRPOJobFeedbackForm:
    def __init__(self, driver, index):
        self.driver = driver
        self.actions = Actions(self.driver)
        self.feedback = FeedbackConfigPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_feedback_form'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_stage1 = xl['stage1'][0]
        self.xl_form1 = xl['form1'][0]
        self.xl_stage2 = xl['stage2'][0]
        self.xl_form2 = xl['form2'][0]
        self.xl_stage3 = xl['stage3'][0]
        self.xl_form3 = xl['form3'][0]

        self.job_ff1_collection = []
        self.job_ff2_collection = []

    def crpo_job_feedback_form1(self):
        self.job_ff1_collection = []

        __list = [self.actions.job_actions_click(),
                  self.actions.job_feedback_form(),
                  self.feedback.stage_selection(self.xl_stage1),
                  self.feedback.form_search_filed_enter(self.xl_form1),
                  self.feedback.form_search(),
                  self.feedback.use_form(),
                  self.feedback.overall_mandatory(),
                  self.feedback.reject_overall_mandatory(),
                  self.feedback.save_feedback_form(),
                  self.feedback.clear_stage_field()
                  ]
        for func in __list:
            if func:
                self.job_ff1_collection.append(func)
            else:
                self.job_ff1_collection.append(func)

    def crpo_job_feedback_form2(self):
        self.job_ff2_collection = []

        __list = [self.feedback.stage_selection(self.xl_stage2),
                  self.feedback.form_search_filed_enter(self.xl_form2),
                  self.feedback.form_search(),
                  self.feedback.use_form(),
                  self.feedback.overall_mandatory(),
                  self.feedback.reject_overall_mandatory(),
                  self.feedback.save_feedback_form(),
                  ]
        for func in __list:
            if func:
                self.job_ff2_collection.append(func)
            else:
                self.job_ff2_collection.append(func)
