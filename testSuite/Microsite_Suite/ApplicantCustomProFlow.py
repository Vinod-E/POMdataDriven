from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.AppCustomPro import AppCustomPropertiesRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_cp import CRPOCustomValues
from Scripts.Output_scripts import RegistrationACPReport


class APPCustomProperties:
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
        ACP_page = AppCustomPropertiesRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        cpv = CRPOCustomValues(driver=driver, index=index)

        ACP_output = RegistrationACPReport.ACPOutputReport(version=version, server=server,
                                                           start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.ACP_page.registration_page_entry()
        self.ACP_output.entry_page_report(self.ACP_page.entry_collection)

    def personal_details_entry(self):
        self.ACP_page.personal_details_entry()
        self.ACP_output.personal_details_report(self.ACP_page.pd_collection)

    def app_custom_details(self):
        self.ACP_page.custom_text_details()
        self.ACP_output.text_details_report(self.ACP_page.text_details_collection)

    def submit_register_data(self):
        self.ACP_page.submit_details()
        self.ACP_output.submit_data_report(self.ACP_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.ACP_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.ACP_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.ACP_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_custom_property_verification(self):
        self.cpv.crpo_applicant_custom_properties()
        self.ACP_output.applicant_cp_report(self.cpv.applicant_acp_collection)


Object = APPCustomProperties()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.app_custom_details()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_custom_property_verification()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.ACP_output.overall_status()
    Object.ACP_output.history_html_generator()
    Object.environment.close()
