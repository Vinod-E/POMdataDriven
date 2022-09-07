from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from pageObjects.Pages.NewRegistrationPage import RazorPayPage
from utilities import excelRead
from utilities.SwitchWindow import SwitchWindowClose


class CrpoRazorPayRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)
        self.razorpay = RazorPayPage.RazorPayPageDetails(self.driver)
        self.back_to_window = SwitchWindowClose(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        razorpay_excel = excelRead.ExcelRead()
        razorpay_excel.read(inputFile.INPUT_PATH['microsite_razorpay'], index=index)
        xl = razorpay_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_phone = xl['phone'][0]
        self.xl_whatsapp = xl['consent'][0]
        self.xl_message = xl['message'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.certi1_collection = []
        self.submit_collection = []
        self.razorpay_collection = []

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

    def submit_details(self):
        self.submit_collection = []
        __list = [self.submit.submit_registration(),
                  self.submit.confirm_registration(),
                  ]
        for func in __list:
            if func:
                self.submit_collection.append(func)
            else:
                self.submit_collection.append(func)

    def razorpay_submit_payment(self):
        self.razorpay_collection = []
        __list = [self.razorpay.merchant_name(self.xl_name),
                  self.razorpay.qrcode(),
                  self.back_to_window.switch_back_from_iframe(),
                  self.submit.registration_successful(self.xl_message),
                  self.submit.order_id(),
                  self.submit.payment_id()
                  ]
        for func in __list:
            if func:
                self.razorpay_collection.append(func)
            else:
                self.razorpay_collection.append(func)
