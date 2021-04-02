from Config import inputFile
from datetime import datetime
from utilities import excelRead
from pageObjects.Pages.EventPages import EventActionsPage, EventSlotConfigurationPage


class SlotConfiguration:
    def __init__(self, driver, index, time):
        now = datetime.now()
        self.current_date = now.strftime("%d/%m/%Y")
        self.time = time

        self.driver = driver
        self.slot = EventActionsPage.Actions(self.driver)
        self.slot_config = EventSlotConfigurationPage.EventSlot(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        slot_excel = excelRead.ExcelRead()
        slot_excel.read(inputFile.INPUT_PATH['event_slot_config'], index=index)
        xl = slot_excel.excel_dict
        self.xl_stage_status = xl['stage_status'][0]
        self.xl_number_of_slots = xl['number_of_slots'][0]
        self.xl_count = xl['count'][0]

        self.event_slot_collection = []

    def slot_configurations(self, candidate_id):
        __list = [self.slot.event_actions_click(),
                  self.slot.event_slot_configuration(),
                  self.slot_config.current_applicant_status_choose(),
                  self.slot_config.search_status_select(self.xl_stage_status),
                  self.slot_config.go_button(),
                  self.slot_config.slot_number(self.xl_number_of_slots),
                  self.slot_config.go_button(),
                  self.slot_config.date_field(self.current_date),
                  self.slot_config.count_field(self.xl_count),
                  self.slot_config.clear_time_field(),
                  self.slot_config.time_field(self.time),
                  self.slot_config.assign_slot_button(),
                  self.slot_config.ok_button(),
                  self.slot_config.ok_button(),
                  self.slot_config.search_id(candidate_id),
                  self.slot_config.search_button(),
                  self.slot_config.login_link_action(),
                  self.slot_config.copy_candidate_login_link(candidate_id),
                  self.slot_config.cancel_button()
                  ]
        for func in __list:
            if func:
                self.event_slot_collection.append(func)
            else:
                self.event_slot_collection.append(func)
