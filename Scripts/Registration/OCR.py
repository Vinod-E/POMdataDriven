from Config import inputFile
from pageObjects.Pages.NewRegistrationPage import EntryPage
from pageObjects.Pages.NewRegistrationPage import PersonalDetailsPage
from pageObjects.Pages.NewRegistrationPage import EducationDetails
from pageObjects.Pages.NewRegistrationPage import SubmitPage
from utilities import excelRead


class EducationalOCR:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.entry = EntryPage.EntryButton(self.driver)
        self.pd = PersonalDetailsPage.PersonalDetailsData(self.driver)
        self.edu = EducationDetails.EducationalDetailsData(self.driver)
        self.submit = SubmitPage.SubmitData(self.driver)

        # ---- Attachment from local machine
        self.attachment_resume = inputFile.INPUT_PATH['job_attachment']
        self.attachment_photo = inputFile.INPUT_PATH['OCR_candidate']
        self.attachment_pan = inputFile.INPUT_PATH['OCR_PAN']
        self.attachment_idcard = inputFile.INPUT_PATH['OCR_id_card']
        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        certificate_excel = excelRead.ExcelRead()
        certificate_excel.read(inputFile.INPUT_PATH['microsite_OCR'], index=index)
        xl = certificate_excel.excel_dict
        self.xl_first = xl['first_name'][0].format(version)
        self.xl_middle = xl['middle_name'][0]
        self.xl_last = xl['last_name'][0]
        self.xl_email = xl['email'][0].format(self.xl_first)
        self.xl_phone = xl['phone'][0]
        self.xl_message = xl['message'][0]
        self.xl_pan_number = xl['Pan_number'][0]
        self.xl_pan_type = xl['Pan_Type'][0]

        self.entry_collection = []
        self.pd_collection = []
        self.submit_collection = []
        self.attachment_collection = []

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
        __list = [self.pd.first_name(self.xl_first),
                  self.pd.middle_name(self.xl_middle),
                  self.pd.last_name(self.xl_last),
                  self.pd.usn_number(self.xl_first),
                  self.pd.email_id(self.xl_email),
                  self.pd.mobile_number(self.xl_phone),
                  ]
        for func in __list:
            if func:
                self.pd_collection.append(func)
            else:
                self.pd_collection.append(func)

    def attachment_details_entry(self):
        self.attachment_collection = []
        __list = [self.pd.photo_upload(self.attachment_photo),
                  self.pd.idcard_type(self.xl_pan_type),
                  self.pd.idcard_upload(self.attachment_pan),
                  self.pd.idcard_number(self.xl_pan_number),
                  self.pd.resume_upload(self.attachment_resume),
                  self.pd.college_id_upload(self.attachment_idcard),
                  ]
        for func in __list:
            if func:
                self.attachment_collection.append(func)
            else:
                self.attachment_collection.append(func)

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
