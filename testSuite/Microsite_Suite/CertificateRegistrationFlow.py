from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.Certificates import CrpoNewRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_Certificates import CRPOCertificate
from Scripts.Output_scripts import RegistrationReport


class RegistrationCertificate:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.registration_app('certificate')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        page_valid = EntryPage.EntryButton(driver=driver)
        Certificate_page = CrpoNewRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        certificate = CRPOCertificate(driver=driver, index=index)

        Certi_output = RegistrationReport.CertOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.Certificate_page.registration_page_entry()
        self.Certi_output.entry_page_report(self.Certificate_page.entry_collection)

    def personal_details_entry(self):
        self.Certificate_page.personal_details_entry()
        self.Certi_output.personal_details_report(self.Certificate_page.pd_collection)

    def certificate1_details_entry(self):
        self.Certificate_page.certificate1_details_entry()
        self.Certi_output.certificate1_details_report(self.Certificate_page.certi1_collection)

    def certificate2_details_entry(self):
        self.Certificate_page.certificate2_details_entry()
        self.Certi_output.certificate2_details_report(self.Certificate_page.certi2_collection)

    def submit_register_data(self):
        self.Certificate_page.submit_details()
        self.Certi_output.submit_data_report(self.Certificate_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.Certi_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.Certi_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.Certi_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_applicant_certificates(self):
        self.certificate.crpo_applicant_certificate()
        self.Certi_output.applicant_certificate_report(self.certificate.applicant_certificate_collection)


Object = RegistrationCertificate()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.certificate1_details_entry()
    Object.certificate2_details_entry()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_applicant_certificates()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.Certi_output.overall_status()
    Object.Certi_output.history_html_generator()
    Object.environment.close()
