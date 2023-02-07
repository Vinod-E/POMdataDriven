from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import AadharVerificationPage
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CrpoAadharRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.aadhar = AadharVerificationPage.AadharPageDetails(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)
        self.back_to_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        aadhar_excel = excelRead.ExcelRead()
        aadhar_excel.read(inputFile.INPUT_PATH['microsite_Aadhar'], index=index)
        xl = aadhar_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_aadhar = xl['AadharNumber'][0]
        self.xl_message = xl['message'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.aadhar_otp_collection = []

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
                  self.pd.aadhar_number(self.xl_aadhar),
                  ]
        for func in __list:
            if func:
                self.pd_collection.append(func)
            else:
                self.pd_collection.append(func)

    def aadhar_opt_verification(self):
        self.aadhar_otp_collection = []
        __list = [self.submit.submit_registration(),
                  self.aadhar.generate_aadhar_otp(),
                  self.aadhar.enter_aadhar_otp(),
                  self.aadhar.proceed_with_aadhar_verify(),
                  self.submit.confirm_registration(),
                  self.submit.registration_successful(self.xl_message)
                  ]
        for func in __list:
            if func:
                self.aadhar_otp_collection.append(func)
            else:
                self.aadhar_otp_collection.append(func)
