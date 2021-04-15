from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EventPages.EventActionsPage import Actions
from pageObjects.Pages.EventPages.EventGetByNamePage import EventGetByName
from pageObjects.Pages.EventPages.EventUploadCandidatePage import EventUploadCandidate


class CRPOUploadCandidate:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.action = Actions(self.driver)
        self.upload = EventUploadCandidate(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_excel'], index=index)
        xl = status_excel.excel_dict
        self.__upload = inputFile.INPUT_PATH['upload']
        self.xl_event_name = xl['name'][0].format(version)
        self.xl_success_msg = xl['upload_message'][0]

        self.event_upload_collection = []

    def crpo_event_upload_candidates(self, email):
        self.event_upload_collection = []
        __list = [self.action.event_actions_click(),
                  self.action.event_upload_candidates(),
                  self.upload.upload_file(self.__upload),
                  self.upload.next_button(),
                  self.upload.declare_check(),
                  self.upload.signature_entry(),
                  self.upload.agreed_button(),
                  self.upload.edit_excel_information(),
                  self.upload.name_edit(self.xl_event_name),
                  self.upload.email_edit(email),
                  self.upload.usn_edit(self.xl_event_name),
                  self.upload.save_info(),
                  self.upload.save_candidate(),
                  self.upload.success_upload(self.xl_success_msg)
                  ]
        for func in __list:
            if func:
                self.event_upload_collection.append(func)
            else:
                self.event_upload_collection.append(func)
