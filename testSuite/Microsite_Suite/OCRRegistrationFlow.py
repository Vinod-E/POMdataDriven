from Config import Enviroment
from Listeners.logger_settings import ui_logger
from pageObjects.Pages.NewRegistrationPage import EntryPage
from Scripts.Registration.OCR import EducationalOCR
from Scripts.Registration.crpo_login import AdminLogin
from Scripts.Registration.crpo_event_search import CRPOEventSearch
from Scripts.Registration.crpo_OCR import CRPOOCRDetails
from Scripts.Output_scripts import RegistrationOCRReport


class RegistrationOCR:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.registration_app('ocr')
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        page_valid = EntryPage.EntryButton(driver=driver)
        OCR_page = EducationalOCR(driver=driver, index=index, version=version)
        admin = AdminLogin(driver=driver, index=index)
        search = CRPOEventSearch(driver=driver, index=index, version=version)
        OCR = CRPOOCRDetails(driver=driver, index=index, version=version)

        OCR_output = RegistrationOCRReport.OcrOutputReport(version=version, server=server,
                                                           start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def page_entry(self):
        self.OCR_page.registration_page_entry()
        self.OCR_output.entry_page_report(self.OCR_page.entry_collection)

    def personal_details_entry(self):
        self.OCR_page.personal_details_entry()
        self.OCR_output.personal_details_report(self.OCR_page.pd_collection)

    def attachments_details_entry(self):
        self.OCR_page.attachment_details_entry()
        self.OCR_output.attachment_details_report(self.OCR_page.attachment_collection)

    def submit_register_data(self):
        self.OCR_page.submit_details()
        self.OCR_output.submit_data_report(self.OCR_page.submit_collection)

    def crpo_admin_login(self):
        self.admin.admin_login(server=self.server)
        self.OCR_output.admin_login_report(self.admin.admin_login_collection)

    def crpo_event_search(self):
        self.search.crpo_search_event()
        self.OCR_output.event_search_report(self.search.event_search_collection)

    def crpo_applicant_search(self):
        self.search.crpo_full_search_applicant()
        self.OCR_output.applicant_search_report(self.search.applicant_full_search_collection)

    def crpo_ocr_verification(self):
        self.OCR.crpo_ocr_applicant_verification()
        self.OCR_output.applicant_ocr_report(self.OCR.applicant_ocr_collection)


Object = RegistrationOCR()

if Object.page_valid.page_validation():
    # captcha = input('Authentication (Click Enter to Complete)')
    # Object.page_entry()
    Object.personal_details_entry()
    Object.attachments_details_entry()
    Object.submit_register_data()
    Object.crpo_admin_login()
    Object.crpo_event_search()
    Object.crpo_applicant_search()
    Object.crpo_ocr_verification()

    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.OCR_output.overall_status()
    Object.OCR_output.history_html_generator()
    Object.environment.close()
