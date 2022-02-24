from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import CertificateDeatilsPage
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class EducationalRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.certi = CertificateDeatilsPage.CertificateDetailsData(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)

        # ---- Attachment from local machine
        self.attachment_file = inputFile.INPUT_PATH['job_attachment']
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite_education'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_phone = xl['phone'][0]
        self.xl_whatsapp = xl['consent'][0]
        self.xl_message = xl['message'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.certi1_collection = []
        self.submit_collection = []

    def registration_page_entry(self):
        self.entry_collection = []
        __list = [self.entry.entry_next()
                  ]
        for func in __list:
            if func:
                self.entry_collection.append(func)
            else:
                self.entry_collection.append(func)

    def personal_details_entry(self):
        self.pd_collection = []
        __list = [self.pd.full_name(self.xl_name),
                  self.pd.email_id(self.xl_email),
                  self.pd.mobile_number(self.xl_phone),
                  self.pd.usn_number(self.xl_name),
                  self.pd.whatsapp_consent(self.xl_whatsapp)
                  ]
        for func in __list:
            if func:
                self.pd_collection.append(func)
            else:
                self.pd_collection.append(func)

    def certificate1_details_entry(self):
        self.certi1_collection = []
        __list = [self.certi.certificate_type(self.xl_c1_type, 1),
                  self.certi.certificate_name(self.xl_c1_name, 1),
                  self.certi.certificate_status(self.xl_c1_status, 1),
                  self.certi.certificate_institute(self.xl_c1_institute, 1),
                  self.certi.no_of_attempts(self.xl_c1_attempts, 1),
                  self.certi.from_month(self.xl_c1_from_month, 1),
                  self.certi.from_year(self.xl_c1_from_year, 1),
                  self.certi.to_month(self.xl_c1_to_month, 1),
                  self.certi.to_year(self.xl_c1_to_year, 1),
                  self.certi.choose_file(self.attachment_file)
                  ]
        for func in __list:
            if func:
                self.certi1_collection.append(func)
            else:
                self.certi1_collection.append(func)

    def submit_details(self):
        self.submit_collection = []
        __list = [self.submit.job_selection(),
                  self.submit.submit_registration(),
                  self.submit.confirm_registration(),
                  self.submit.registration_successful(self.xl_message)
                  ]
        for func in __list:
            if func:
                self.submit_collection.append(func)
            else:
                self.submit_collection.append(func)
