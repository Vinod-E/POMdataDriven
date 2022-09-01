from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import CertificateDeatilsPage
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class CrpoNewRegistration:

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
        certificate_excel.read(inputFile.INPUT_PATH['microsite_certificate'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_phone = xl['phone'][0]
        self.xl_c1_type = xl['c1_type'][0]
        self.xl_c1_name = xl['c1_name'][0]
        self.xl_c1_status = xl['c1_status'][0]
        self.xl_c1_institute = xl['c1_institute'][0]
        self.xl_c1_attempts = xl['c1_attempts'][0]
        self.xl_c1_from_month = xl['c1_from_month'][0]
        self.xl_c1_to_month = xl['c1_to_month'][0]
        self.xl_c1_from_year = xl['c1_from_year'][0]
        self.xl_c1_to_year = xl['c1_to_year'][0]
        self.xl_c2_type = xl['c2_type'][0]
        self.xl_c2_name = xl['c2_name'][0]
        self.xl_c2_status = xl['c2_status'][0]
        self.xl_c2_institute = xl['c2_institute'][0]
        self.xl_c2_attempts = xl['c2_attempts'][0]
        self.xl_c2_from_month = xl['c2_from_month'][0]
        self.xl_c2_to_month = xl['c2_to_month'][0]
        self.xl_c2_from_year = xl['c2_from_year'][0]
        self.xl_c2_to_year = xl['c2_to_year'][0]
        self.xl_message = xl['message'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.certi1_collection = []
        self.certi2_collection = []
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
                  self.pd.mobile_number(self.xl_phone)
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

    def certificate2_details_entry(self):
        self.certi2_collection = []
        __list = [self.certi.add_certificate(),
                  self.certi.certificate_type(self.xl_c2_type, 2),
                  self.certi.certificate_name(self.xl_c2_name, 2),
                  self.certi.certificate_status(self.xl_c2_status, 2),
                  self.certi.certificate_institute(self.xl_c2_institute, 2),
                  self.certi.no_of_attempts(self.xl_c2_attempts, 2),
                  self.certi.from_month(self.xl_c2_from_month, 2),
                  self.certi.from_year(self.xl_c2_from_year, 2),
                  self.certi.to_month(self.xl_c2_to_month, 2),
                  self.certi.to_year(self.xl_c2_to_year, 2),
                  self.certi.choose_file2(self.attachment_file)
                  ]
        for func in __list:
            if func:
                self.certi2_collection.append(func)
            else:
                self.certi2_collection.append(func)

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
