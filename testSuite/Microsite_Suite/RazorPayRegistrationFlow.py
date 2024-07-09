from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.RazorPay import CrpoRazorPayRegistration
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_Razorpay import CRPORazorPay
from Scripts.Output_scripts import RegistrationRazorpayReport


class RegistrationRazorPay:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.registration_app('payment')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        page_valid = EntryPage.EntryButton(driver=driver)
        Razorpay_page = CrpoRazorPayRegistration(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        pay = CRPORazorPay(driver=driver, index=index)

        Razorpay_output = RegistrationRazorpayReport.RazorPayOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.Razorpay_page.registration_page_entry()
        self.Razorpay_output.entry_page_report(self.Razorpay_page.entry_collection)

    def personal_details_entry(self):
        self.Razorpay_page.personal_details_entry()
        self.Razorpay_output.personal_details_report(self.Razorpay_page.pd_collection)

    def submit_register_data(self):
        self.Razorpay_page.submit_details()
        self.Razorpay_output.submit_data_report(self.Razorpay_page.submit_collection)

    def submit_razorpay_data(self):
        self.Razorpay_page.razorpay_submit_payment()
        self.Razorpay_output.razorpay_data_report(self.Razorpay_page.razorpay_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.Razorpay_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.Razorpay_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_search_applicant()
        self.Razorpay_output.applicant_search_report(self.search.applicant_search_collection)

    def crpo_applicant_payment(self):
        self.pay.crpo_applicant_payment()
        self.Razorpay_output.applicant_payment_report(self.pay.applicant_payment_collection)


Object = RegistrationRazorPay()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.submit_register_data()
    Object.submit_razorpay_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_applicant_payment()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.Razorpay_output.overall_status()
    Object.Razorpay_output.history_html_generator()
    Object.environment.close()
