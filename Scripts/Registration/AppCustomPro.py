from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import CustomProperty
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class AppCustomPropertiesRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.cp = CustomProperty.CustomPropertyData(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        cp_excel = excelRead.ExcelRead()
        cp_excel.read(inputFile.INPUT_PATH['microsite_ACP'], index=index)
        xl = cp_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_phone = xl['phone'][0]
        self.xl_whatsapp = xl['consent'][0]
        self.xl_message = xl['message'][0]
        self.xl_text = xl['text'][0]
        self.xl_textarea = xl['textarea'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.text_details_collection = []
        self.textarea_details_collection = []
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
                  self.pd.whatsapp_consent(self.xl_whatsapp)
                  ]
        for func in __list:
            if func:
                self.pd_collection.append(func)
            else:
                self.pd_collection.append(func)

    def custom_text_details(self):
        self.text_details_collection = []
        __list = [
            self.cp.text_field(self.xl_text, 1),
            self.cp.text_field(self.xl_text, 2),
            self.cp.text_field(self.xl_text, 3),
            self.cp.text_field(self.xl_text, 4),
            self.cp.text_field(self.xl_text, 5),
            self.cp.text_field(self.xl_text, 7)
                  ]
        for func in __list:
            if func:
                self.text_details_collection.append(func)
            else:
                self.text_details_collection.append(func)

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
