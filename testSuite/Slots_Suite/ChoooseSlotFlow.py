from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Output_scripts import ChooseSlotReport
from Scripts.Slots import ChooseSlots
from Scripts.Slots.crpo_admin_login import AdminLogin
from Scripts.Slots.crpo_event import CRPOEventSearch


class InterviewSlot:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.slot_app('Choose')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        slot_app = ChooseSlots.ChooseSlotApp(driver=driver, index=index)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, app='Choose')

        slot_output = ChooseSlotReport.ChooseSlotReport(version=version,
                                                        server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def captcha_entry(self):
        self.slot_app.slot_captcha_page_entry()
        self.slot_output.entry_page_report(self.slot_app.entry_collection)

    def slot_choose(self):
        self.slot_app.slot_selections()
        self.slot_output.choose_slot_report(self.slot_app.choose_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.slot_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.slot_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_status(self):
        self.search.crpo_candidate_search()
        self.slot_output.candidate_search_report(self.search.event_candidate_collection)

    def crpo_applicant_verification(self):
        self.search.crpo_candidate_verification()
        self.slot_output.candidate_verification_report(self.search.candidate_verification_collection)


Object = InterviewSlot()
captcha = input('Authentication (Click Enter to Complete)')
Object.captcha_entry()
Object.slot_choose()
Object.crpo_admin_login()
Object.crpo_event_search()
Object.crpo_applicant_status()
Object.crpo_applicant_verification()

"""
<<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
"""
Object.slot_output.overall_status()
Object.slot_output.history_html_generator()
Object.environment.close()
