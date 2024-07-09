from Config import inputFile
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.SearchPages.AdvanceSearchPage import Search
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventApplicantPage import EventApplicant
from pageObjects.Pages.CandidatePages.CandidateDetailsPage import CandidateDetailsPage
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs
from pageObjects.Pages.EventPages.EventAssessmentSlotPage import AssessmentSlot
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose
from utilities.uiNotifier import Notifier


class CRPOEventSearch:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.subtab = EventSubTabs(self.driver)
        self.slot_search = AssessmentSlot(self.driver)
        self.notifier = Notifier(self.driver)
        self.search = Search(self.driver)
        self.get_by = EventGetByName(self.driver)
        self.action = Actions(self.driver)
        self.applicant = EventApplicant(self.driver)
        self.candidate = CandidateDetailsPage(self.driver)
        self.switch_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['assessment_slot'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['event_name'][0]
        self.xl_job_filter = xl['job_name'][0]
        self.xl_stage_filter = xl['stage_name'][0]
        self.xl_unassign_slot = xl['unassign_slot'][0]
        self.xl_notifier = xl['notifier'][0]

        self.event_search_collection = []
        self.event_tracking_collection = []
        self.event_unslot_collection = []

    def crpo_search_event(self):
        self.event_search_collection = []
        __list = [self.menu.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.get_by.event_name_click(),
                  self.get_by.event_name_validation(self.xl_event_name)
                  ]
        for func in __list:
            if func:
                self.event_search_collection.append(func)
            else:
                self.event_search_collection.append(func)

    def crpo_tracking_tab(self):
        self.event_tracking_collection = []
        __list = [self.subtab.tracking(),
                  self.subtab.assessment_slot_tab(),
                  self.slot_search.job_filters(self.xl_job_filter),
                  self.slot_search.stage_filter(self.xl_stage_filter)
                  ]
        for func in __list:
            if func:
                self.event_tracking_collection.append(func)
            else:
                self.event_tracking_collection.append(func)

    def crpo_unassign_assessment_slot(self):
        self.event_unslot_collection = []
        __list = [self.slot_search.go_button(),
                  self.slot_search.check_box(),
                  self.slot_search.un_assign_slot_icon(),
                  self.slot_search.select_slot_to_unassign(self.xl_unassign_slot),
                  self.slot_search.unassign_button(),
                  self.notifier.glowing_messages(self.xl_notifier)
                  ]
        for func in __list:
            if func:
                self.event_unslot_collection.append(func)
            else:
                self.event_unslot_collection.append(func)
