from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.WorkProfile import WorkProfileRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_workprofile import CRPOWorkProfile
from Scripts.Output_scripts import RegistrationWorkReport


class RegistrationOCR:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.registration_app('workProfile')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        page_valid = EntryPage.EntryButton(driver=driver)
        WP_page = WorkProfileRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        wp = CRPOWorkProfile(driver=driver, index=index)

        WP_output = RegistrationWorkReport.WPOutputReport(version=version, server=server,
                                                          start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.WP_page.registration_page_entry()
        self.WP_output.entry_page_report(self.WP_page.entry_collection)

    def personal_details_entry(self):
        self.WP_page.personal_details_entry()
        self.WP_output.personal_details_report(self.WP_page.pd_collection)

    def work_profile_details_one(self):
        self.WP_page.work_profile1_details()
        self.WP_output.wf1_details_report(self.WP_page.wf1_details_collection)

    def work_profile_details_two(self):
        self.WP_page.work_profile2_details()
        self.WP_output.wf2_details_report(self.WP_page.wf2_details_collection)

    def submit_register_data(self):
        self.WP_page.submit_details()
        self.WP_output.submit_data_report(self.WP_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.WP_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.WP_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.WP_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_workprofile_verification(self):
        self.wp.crpo_applicant_workprofile()
        self.WP_output.applicant_wp_report(self.wp.applicant_wp_collection)


Object = RegistrationOCR()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.work_profile_details_one()
    Object.work_profile_details_two()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_workprofile_verification()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.WP_output.overall_status()
    Object.WP_output.history_html_generator()
    Object.environment.close()
