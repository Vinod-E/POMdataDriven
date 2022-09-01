from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import EducationDetails
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class EducationalRegistration:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.edu = EducationDetails.EducationalDetailsData(self.driver)
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
        self.pg_details_collection = []
        self.ug_details_collection = []
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
                  self.pd.usn_number(self.xl_name),
                  self.pd.whatsapp_consent(self.xl_whatsapp)
                  ]
        for func in __list:
            if func:
                self.pd_collection.append(func)
            else:
                self.pd_collection.append(func)

    def entry_pg_details(self):
        self.pg_details_collection = []
        __list = [self.edu.pg_education_type('Post Graduate'),
                  self.edu.pg_degree("M.Tech.(Master of Technology)"),
                  self.edu.pg_college("AMIE"),
                  self.edu.pg_branch("Computer Science"),
                  self.edu.pg_yop("2016"),
                  self.edu.pg_select_cgpa(),
                  self.edu.pg_cgpa("4.5"),
                  self.edu.pg_cgpa_out_of("5"),
                  self.edu.add_more_education()
                  ]
        for func in __list:
            if func:
                self.pg_details_collection.append(func)
            else:
                self.pg_details_collection.append(func)

    def entry_ug_details(self):
        self.ug_details_collection = []
        __list = [self.edu.ug_education_type("Under Graduate"),
                  self.edu.ug_degree("B.Tech.(Bachelor of Technology)"),
                  self.edu.ug_college("AIM"),
                  self.edu.ug_branch("Computer Science"),
                  self.edu.ug_yop("2014"),
                  self.edu.ug_select_percent(),
                  self.edu.ug_percent("73.9"),
                  self.edu.add_more_education()
                  ]
        for func in __list:
            if func:
                self.ug_details_collection.append(func)
            else:
                self.ug_details_collection.append(func)

    def entry_twelfth_details(self):
        self.twelfth_details_collection = []
        __list = [self.edu.twelfth_education_type("12th/Diploma"),
                  self.edu.twelfth_yop("2011"),
                  self.edu.twelfth_select_cgpa(),
                  self.edu.twelfth_cgpa("4.5"),
                  self.edu.add_more_education()
                  ]
        for func in __list:
            if func:
                self.twelfth_details_collection.append(func)
            else:
                self.twelfth_details_collection.append(func)

    def entry_tenth_details(self):
        self.tenth_details_collection = []
        __list = [self.edu.tenth_education_type("10th"),
                  self.edu.tenth_yop("2008"),
                  self.edu.tenth_select_percent(),
                  self.edu.tenth_percent("89.3"),
                  ]
        for func in __list:
            if func:
                self.tenth_details_collection.append(func)
            else:
                self.tenth_details_collection.append(func)

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
