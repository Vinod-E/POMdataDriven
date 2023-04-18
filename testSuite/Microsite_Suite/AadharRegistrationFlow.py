from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.Aadhar import CrpoAadharRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_Aadhar import CRPOAadhar
from Scripts.Output_scripts import RegistrationAadharReport


class RegistrationAadhar:
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
        Aadhar_page = CrpoAadharRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        aadhar = CRPOAadhar(driver=driver, index=index)

        Aadhar_output = RegistrationAadharReport.AadharOutputReport(version=version,
                                                                    server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.Aadhar_page.registration_page_entry()
        self.Aadhar_output.entry_page_report(self.Aadhar_page.entry_collection)

    def personal_details_entry(self):
        self.Aadhar_page.personal_details_entry()
        self.Aadhar_output.personal_details_report(self.Aadhar_page.pd_collection)

    def otp_verification_aadhar(self):
        self.Aadhar_page.aadhar_opt_verification()
        self.Aadhar_output.submit_and_aadhar_data_report(self.Aadhar_page.aadhar_otp_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.Aadhar_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.Aadhar_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_aadhar_name_search_applicant()
        self.Aadhar_output.applicant_search_report(self.search.applicant_aadhar_name_search_collection)

    def crpo_aadhar_verification(self):
        self.aadhar.crpo_applicant_aadhar()
        self.Aadhar_output.aadhar_verification_report(self.aadhar.applicant_aadhar_collection)


Object = RegistrationAadhar()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    # Object.personal_details_entry()
    # Object.otp_verification_aadhar()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_aadhar_verification()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.Aadhar_output.overall_status()
    Object.Aadhar_output.history_html_generator()
    Object.environment.close()
