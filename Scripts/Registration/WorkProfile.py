from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import WrokProfile
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class WorkProfileRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.pro = WrokProfile.WorkProfileDetailsData(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite_WorkProfile'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_name = xl['candidate_name'][0].format(version)
        self.xl_email = xl['email'][0].format(self.xl_name)
        self.xl_phone = xl['phone'][0]
        self.xl_whatsapp = xl['consent'][0]
        self.xl_message = xl['message'][0]
        self.xl_wp1_company = xl['wp1_company'][0]
        self.xl_wp1_sector = xl['wp1_sector'][0]
        self.xl_wp1_designation = xl['wp1_designation'][0]
        self.xl_wp1_from_month = xl['wp1_from_month'][0]
        self.xl_wp1_to_month = xl['wp1_to_month'][0]
        self.xl_wp1_from_year = xl['wp1_from_year'][0]
        self.xl_wp1_to_year = xl['wp1_to_year'][0]
        self.xl_wp2_company = xl['wp2_company'][0]
        self.xl_wp2_sector = xl['wp2_sector'][0]
        self.xl_wp2_designation = xl['wp2_designation'][0]
        self.xl_wp2_from_month = xl['wp2_from_month'][0]
        self.xl_wp2_to_month = xl['wp2_to_month'][0]
        self.xl_wp2_from_year = xl['wp2_from_year'][0]
        self.xl_wp2_to_year = xl['wp1_to_year'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.wf1_details_collection = []
        self.wf2_details_collection = []
        self.twelfth_details_collection = []
        self.tenth_details_collection = []
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

    def work_profile1_details(self):
        self.wf1_details_collection = []
        __list = [self.pro.company(self.xl_wp1_company, 1),
                  self.pro.sector(self.xl_wp1_sector, 1),
                  self.pro.designation(self.xl_wp1_designation, 1),
                  self.pro.from_month(self.xl_wp1_from_month, 1),
                  self.pro.to_month(self.xl_wp1_to_month, 1),
                  self.pro.from_year(self.xl_wp1_from_year, 1),
                  self.pro.to_year(self.xl_wp1_to_year, 1),
                  self.pro.add_more_profile()
                  ]
        for func in __list:
            if func:
                self.wf1_details_collection.append(func)
            else:
                self.wf1_details_collection.append(func)

    def work_profile2_details(self):
        self.wf2_details_collection = []
        __list = [self.pro.company(self.xl_wp2_company, 2),
                  self.pro.sector(self.xl_wp2_sector, 2),
                  self.pro.designation(self.xl_wp2_designation, 2),
                  self.pro.from_month(self.xl_wp2_from_month, 2),
                  self.pro.to_month(self.xl_wp2_to_month, 2),
                  self.pro.from_year(self.xl_wp2_from_year, 2),
                  self.pro.to_year(self.xl_wp2_to_year, 2),
                  ]
        for func in __list:
            if func:
                self.wf2_details_collection.append(func)
            else:
                self.wf2_details_collection.append(func)

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
