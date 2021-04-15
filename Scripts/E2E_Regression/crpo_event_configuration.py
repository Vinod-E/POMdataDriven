from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.EventPages.EventActivityTaskConfigPage import EventActivityTaskConfigPage
from pageObjects.Pages.EventPages.EventTestConfig import EventTestConfigPage


class CRPOEventConfiguration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.get_by = EventGetByName(self.driver)
        self.task_config = EventActivityTaskConfigPage(self.driver)
        self.multi_value = MultiSelectValues(self.driver)
        self.test = EventTestConfigPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_excel'], index=index)
        xl = status_excel.excel_dict
        self.xl_event_name = xl['name'][0].format(version)
        self.xl_stage_status = xl['offer_stage_status'][0]
        self.xl_positive_stage = xl['offer_positive'][0]
        self.xl_negative_stage = xl['offer_negative'][0]
        self.xl_activity2 = xl['activity2'][0]
        self.xl_task_message = xl['task_message'][0]
        self.xl_test_stage = xl['test_stage'][0]
        self.xl_test_message = xl['test_message'][0]

        self.event_task_config_collection = []
        self.event_test_config_collection = []

    def crpo_event_task_configurations(self):
        self.event_task_config_collection = []
        __list = [self.task_config.configurations_tab(),
                  self.get_by.event_name_validation(self.xl_event_name),
                  self.task_config.event_task_configure_button(),
                  self.task_config.task_new_row(),
                  self.task_config.event_task_job_name(self.xl_event_name),
                  self.task_config.event_activity_stage_field(self.xl_stage_status),
                  self.task_config.event_activity_positive_stage_field(self.xl_positive_stage),
                  self.task_config.event_activity_negative_stage_field(self.xl_negative_stage),
                  self.task_config.event_activity_field(self.xl_activity2),
                  self.task_config.event_task_field(),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.task_config.event_activity_task_save(),
                  self.task_config.event_task_notifier(self.xl_task_message),
                  self.task_config.event_task_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.event_task_config_collection.append(func)
            else:
                self.event_task_config_collection.append(func)

    def crpo_event_test_configurations(self):
        self.event_test_config_collection = []
        __list = [self.test.event_test_configure_button(),
                  self.test.test_job_name_field(self.xl_event_name),
                  self.test.test_stage_name_field(self.xl_test_stage),
                  self.test.test_test_name_field(self.xl_event_name),
                  self.test.test_active_enable(),
                  self.test.event_test_configure_save(),
                  self.test.test_tag_notifier(self.xl_test_message),
                  self.test.test_tag_notifier_dismiss(),
                  self.test.cancel_test_extra_config()
                  ]
        for func in __list:
            if func:
                self.event_test_config_collection.append(func)
            else:
                self.event_test_config_collection.append(func)
