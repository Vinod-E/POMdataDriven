from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.CustomProperties import CustomPropertiesRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_cp import CRPOCustomValues
from Scripts.Output_scripts import RegistrationCPReport


class CandidateCustomPRO:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        page_valid = EntryPage.EntryButton(driver=driver)
        CP_page = CustomPropertiesRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        cpv = CRPOCustomValues(driver=driver, index=index)

        CP_output = RegistrationCPReport.CPOutputReport(version=version, server=server,
                                                        start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.CP_page.registration_page_entry()
        self.CP_output.entry_page_report(self.CP_page.entry_collection)

    def personal_details_entry(self):
        self.CP_page.personal_details_entry()
        self.CP_output.personal_details_report(self.CP_page.pd_collection)

    def custom_text_details(self):
        self.CP_page.custom_text_details()
        self.CP_output.text_details_report(self.CP_page.text_details_collection)

    def custom_textarea_details(self):
        self.CP_page.custom_textarea_details()
        self.CP_output.textarea_details_report(self.CP_page.textarea_details_collection)

    def submit_register_data(self):
        self.CP_page.submit_details()
        self.CP_output.submit_data_report(self.CP_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.CP_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.CP_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.CP_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_custom_property_verification(self):
        self.cpv.crpo_applicant_text_textarea_values()
        self.CP_output.applicant_cp_report(self.cpv.applicant_tpv_collection)


Object = CandidateCustomPRO()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.custom_text_details()
    Object.custom_textarea_details()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_custom_property_verification()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.CP_output.overall_status()
    Object.CP_output.history_html_generator()
    Object.environment.close()
