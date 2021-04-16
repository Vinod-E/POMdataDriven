from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.SettingsPage.AccountNameSettingsPage import AccountName
from pageObjects.Pages.SettingsPage.InterviewModulePage import InterviewModulePage
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.JobPages.JobGetByNamePage import JobGetByName
from pageObjects.Pages.JobPages.JobActionsPage import Actions
from pageObjects.Pages.JobPages.JobNewFeedbackPage import NewFeedbackConfigPage


class CRPOJobFeedbackFormNew:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.account = AccountName(self.driver)
        self.new_form = InterviewModulePage(self.driver)
        self.menu = Menu(self.driver)
        self.search = Search(self.driver)
        self.job_get_name = JobGetByName(self.driver)
        self.actions = Actions(self.driver)
        self.new_feedback = NewFeedbackConfigPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        job_config_excel = excelRead.ExcelRead()
        job_config_excel.read(inputFile.INPUT_PATH['job_feedback_form'], index=index)
        xl = job_config_excel.excel_dict
        self.xl_job_name = xl['job_name'][0].format(version)
        self.xl_tab_title = xl['job_tab_title'][0]
        self.xl_menu = xl['job_menu'][0]
        self.xl_stage3 = xl['stage3'][0]
        self.xl_form3 = xl['form3'][0]
        self.xl_message = xl['new_form_config_msg'][0]
        self.xl_update_message = xl['update_form_msg'][0]

        self.job_new_form_collection = []
        self.job_new_form_On_collection = []
        self.job_new_form_Off_collection = []

    def crpo_job_new_form_enable(self):
        self.job_new_form_On_collection = []

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
                self.job_new_form_On_collection.append(func)
            else:
                self.job_new_form_On_collection.append(func)

    def crpo_job_new_form_disable(self):
        self.job_new_form_Off_collection = []

        __list = [self.account.account_name_click(),
                  self.account.account_settings(),
                  self.new_form.interview_module(),
                  self.new_form.new_form_setting(),
                  self.new_form.disable_new_form(),
                  self.new_form.save_notifier(self.xl_message),
                  self.new_form.notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_new_form_Off_collection.append(func)
            else:
                self.job_new_form_Off_collection.append(func)

    def crpo_job_feedback_new_form(self):
        self.job_new_form_collection = []

        __list = [self.menu.job_tab(self.xl_menu, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_job_name),
                  self.search.job_search_button(),
                  self.job_get_name.job_name_click(self.xl_job_name),
                  self.job_get_name.job_name_validation(self.xl_job_name),
                  self.actions.job_actions_click(),
                  self.actions.job_feedback_form(),
                  self.new_feedback.stage_selection(self.xl_stage3),
                  self.new_feedback.form_search_filed_enter(self.xl_form3),
                  self.new_feedback.form_search(),
                  self.new_feedback.use_form(),
                  self.new_feedback.edit_form(),
                  self.new_feedback.overall_mandatory(),
                  self.new_feedback.reject_overall_mandatory(),
                  self.new_feedback.update_feedback_form(),
                  self.new_feedback.job_new_form_notifier(self.xl_update_message),
                  self.new_feedback.job_new_form_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.job_new_form_collection.append(func)
            else:
                self.job_new_form_collection.append(func)
