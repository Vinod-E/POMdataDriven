from datetime import datetime
from Config import inputFile
from utilities import excelRead, SwitchWindow
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from pageObjects.Pages.MultiSearchAddValue.multiSelectValues import MultiSelectValues
from pageObjects.Pages.EventPages import EventGetByNamePage, EventApplicantPage, \
    EventActionsPage, EventCreationPage


class CRPOEventCreation:

    def __init__(self, driver, index, version):
        now = datetime.now()
        self.__test_from_date = now.strftime("%d/%m/%Y")
        self.__test_to_date = now.strftime("%d/%m/%Y")
        self.driver = driver
        self.event = EventCreationPage.EventCreation(self.driver)
        self.multi_value = MultiSelectValues(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.event_action = EventActionsPage.Actions(self.driver)
        self.applicant_grid = EventApplicantPage.EventApplicant(self.driver)
        self.window_switch = SwitchWindow.SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_excel'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['name'][0].format(version)
        self.xl_slot = xl['slot'][0]
        self.xl_em = xl['event_manager'][0]
        self.xl_college = xl['college'][0]
        self.xl_create_message = xl['message'][0]

        self.event_create_collection = []

    def crpo_event_creation(self):
        self.event_create_collection = []
        __list = [self.search.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.event.new_event_button(),
                  self.event.event_name_field(self.xl_event_name),
                  self.event.event_req_field(self.xl_event_name),
                  self.event.event_job_field(),
                  self.multi_value.search(self.xl_event_name),
                  self.multi_value.move_all_items(),
                  self.multi_value.done(),
                  self.event.event_slot_field(self.xl_slot),
                  self.event.event_from_date(self.__test_from_date),
                  self.event.event_to_date(self.__test_to_date),
                  self.event.event_report_date(self.__test_from_date),
                  self.event.event_manager_field(self.xl_em),
                  self.event.event_college_field(self.xl_college),
                  self.event.event_ec_enable(),
                  self.event.event_create_button(),
                  self.event.event_create_notifier(self.xl_create_message),
                  self.event.event_create_notifier_dismiss()
                  ]
        for func in __list:
            if func:
                self.event_create_collection.append(func)
            else:
                self.event_create_collection.append(func)
