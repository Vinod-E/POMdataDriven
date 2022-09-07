from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.Education import EducationalRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_Education import CRPOEducation
from Scripts.Output_scripts import RegistrationEducationReport


class RegistrationEducation:
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
        Education_page = EducationalRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        Education = CRPOEducation(driver=driver, index=index)

        education_output = RegistrationEducationReport.EduOutputReport(version=version, server=server,
                                                                       start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.Education_page.registration_page_entry()
        self.education_output.entry_page_report(self.Education_page.entry_collection)

    def personal_details_entry(self):
        self.Education_page.personal_details_entry()
        self.education_output.personal_details_report(self.Education_page.pd_collection)

    def pg_details_entry(self):
        self.Education_page.entry_pg_details()
        self.education_output.pg_details_report(self.Education_page.pg_details_collection)

    def ug_details_entry(self):
        self.Education_page.entry_ug_details()
        self.education_output.ug_details_report(self.Education_page.ug_details_collection)

    def twelfth_details_entry(self):
        self.Education_page.entry_twelfth_details()
        self.education_output.twelfth_details_report(self.Education_page.twelfth_details_collection)

    def tenth_details_entry(self):
        self.Education_page.entry_tenth_details()
        self.education_output.tenth_details_report(self.Education_page.tenth_details_collection)

    def submit_register_data(self):
        self.Education_page.submit_details()
        self.education_output.submit_data_report(self.Education_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.education_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.education_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.education_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_applicant_educations(self):
        self.Education.crpo_applicant_education()
        self.education_output.applicant_education_report(self.Education.applicant_education_collection)


Object = RegistrationEducation()

if Object.page_valid.page_validation():
    captcha = input('Authentication (Click Enter to Complete)')
    Object.page_entry()
    Object.personal_details_entry()
    Object.pg_details_entry()
    Object.ug_details_entry()
    Object.twelfth_details_entry()
    Object.tenth_details_entry()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_applicant_educations()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.education_output.overall_status()
    Object.education_output.history_html_generator()
    Object.environment.close()
