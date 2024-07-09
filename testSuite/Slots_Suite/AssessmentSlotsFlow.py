from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Output_scripts import AssessmentSlotReport
from Scripts.Slots import AssessmentSlots
from Scripts.Slots.crpo_admin_login import AdminLogin
from Scripts.Slots.crpo_event import CRPOEventSearch


class AssessmentSlot:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.slot_app('assessment')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        slot_app = AssessmentSlots.AssessmentSlotApp(driver=driver, index=index)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)

        slot_output = AssessmentSlotReport.AssessmentSlotOutputReport(version=version,
                                                                      server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def captcha_entry(self):
        self.slot_app.slot_captcha_page_entry()
        self.slot_output.entry_page_report(self.slot_app.entry_collection)

    def slot_choose(self):
        self.slot_app.slot_selections()
        self.slot_output.slot_page_report(self.slot_app.selection_collection)

    def update_slot_choose(self):
        self.slot_app.update_slot_selections()
        self.slot_output.update_slot_page_report(self.slot_app.update_selection_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.slot_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.slot_output.event_search_report(self.search.event_search_collection)

    def crpo_event_tracking(self):
        self.search.crpo_tracking_tab()
        self.slot_output.event_tracking_report(self.search.event_tracking_collection)

    def crpo_unassign_slot(self):
        self.search.crpo_unassign_assessment_slot()
        self.slot_output.unassign_slot_report(self.search.event_unslot_collection)


Object = AssessmentSlot()
captcha = input('Authentication (Click Enter to Complete)')
Object.captcha_entry()
Object.slot_choose()
Object.update_slot_choose()
Object.crpo_admin_login()
Object.crpo_event_search()
Object.crpo_event_tracking()
Object.crpo_unassign_slot()

"""
<<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
"""
Object.slot_output.overall_status()
Object.slot_output.history_html_generator()
Object.environment.close()
