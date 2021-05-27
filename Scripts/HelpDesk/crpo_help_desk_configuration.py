from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.RequirementPages.RequirementHelpDeskConfig import RequirementHelpDeskConfig


class CrpoRequirementHelpDeskConfig:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.helpdesk_config = RequirementHelpDeskConfig(self.driver)
        self.multi_value = MultiSelectValues(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        hd_excel = excelRead.ExcelRead()
        hd_excel.read(inputFile.INPUT_PATH['help_desk'], index=index)
        xl = hd_excel.excel_dict
        self.xl_job_name = xl['config_to'][0].format(version)
        self.xl_event_name = xl['config_to'][0].format(version)
        self.xl_sla = xl['sla'][0]
        self.xl_default_category = xl['default_category'][0]
        self.xl_default_user = xl['default_user'][0]
        self.xl_job_category = xl['job_category'][0]
        self.xl_job_user = xl['job_user'][0]
        self.xl_event_category = xl['event_category'][0]
        self.xl_event_user = xl['event_user'][0]
        self.xl_message = xl['message'][0]

        self.default_collection = []
        self.job_level_collection = []
        self.event_level_collection = []
        self.save_config_collection = []

    def default_level_config(self):
        self.default_collection = []
        __list = [self.helpdesk_config.default_category(),
                  self.multi_value.search(self.xl_default_category),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.category_user_selection(),
                  self.multi_value.search(self.xl_default_user),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.category_sla_hour_selection(self.xl_sla)
                  ]
        for func in __list:
            if func:
                self.default_collection.append(func)
            else:
                self.default_collection.append(func)

    def job_level_config(self):
        self.job_level_collection = []
        __list = [self.helpdesk_config.job_category(),
                  self.multi_value.search(self.xl_job_category),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.category_job_selection(),
                  self.multi_value.search(self.xl_job_name),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.job_user_selection(),
                  self.multi_value.search(self.xl_job_user),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.job_sla_hour_selection(self.xl_sla)
                  ]
        for func in __list:
            if func:
                self.job_level_collection.append(func)
            else:
                self.job_level_collection.append(func)

    def event_level_config(self):
        self.event_level_collection = []
        __list = [self.helpdesk_config.event_category(),
                  self.multi_value.search(self.xl_event_category),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.event_job_selection(),
                  self.multi_value.search(self.xl_job_name),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.category_event_selection(),
                  self.multi_value.search(self.xl_event_name),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.event_user_selection(),
                  self.multi_value.search(self.xl_event_user),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.helpdesk_config.event_sla_hour_selection(self.xl_sla)
                  ]
        for func in __list:
            if func:
                self.event_level_collection.append(func)
            else:
                self.event_level_collection.append(func)

    def save_configurations(self):
        self.save_config_collection = []
        __list = [self.helpdesk_config.save_help_desk_config(),
                  self.helpdesk_config.config_notifier(self.xl_message),
                  self.helpdesk_config.config_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.save_config_collection.append(func)
            else:
                self.save_config_collection.append(func)
