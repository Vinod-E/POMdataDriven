from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.SettingsPage.AccountNameSettingsPage import AccountName
from pageObjects.Pages.SettingsPage.InterviewModulePage import InterviewModulePage


class CRPOJobFeedbackFormNew:
    def __init__(self, driver, index):
        self.driver = driver
        self.account = AccountName(self.driver)
        self.new_form = InterviewModulePage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_feedback_form'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_stage3 = xl['stage3'][0]
        self.xl_form3 = xl['form3'][0]
        self.xl_message = xl['new_form_config_msg'][0]

        self.job_new_form_collection = []

    def crpo_job_feedback_new_form(self):
        self.job_new_form_collection = []

        __list = [self.account.account_name_click(),
                  self.account.account_settings(),
                  self.new_form.interview_module(),
                  self.new_form.new_form_setting(),
                  self.new_form.enable_new_form(),
                  self.new_form.save_notifier(self.xl_message),
                  self.new_form.notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_new_form_collection.append(func)
            else:
                self.job_new_form_collection.append(func)
