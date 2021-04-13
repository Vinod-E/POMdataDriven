from utilities import excelWrite
from Config import outputFile


class E2EOutputReport:
    """Number of Test cases """
    TestCases = 150

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['E2E_output']

        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers_1 = ['Create Job', 'Status', 'Job (SP / EC)', 'Status', 'Job (Task)', 'Status',
                           'Job Interviewers', 'Status', 'Job (Old Form)', 'Status', 'Settings - NewForm (ON/OFF)',
                           'Status', 'Job (New Form)', 'Status', 'Job Automations', 'Status']
        color_headers_1 = ['Status', 'Create Job', 'Job (SP / EC)', 'Job (Task)', 'Job (Old Form)', 'Job (New Form)',
                           'Settings - NewForm (ON/OFF)', 'Job Interviewers', 'Job Automations']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Create Requirement', 'Status', 'Clone Assessment', 'Status']
        color_headers_2 = ['Status', 'Create Requirement', 'Clone Assessment']
        self.xlw.excel_header_by_index(row=20, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='E2E REGRESSION FLOW')

    def job_creation_report(self, job_creation_coll):
        testdata_headers = ['Job Tab', 'Job Create Button', 'Job Name', 'Job Attachment', 'Job Notifier', 'Description',
                            'Location Field', 'Hiring Manager Field', 'Business Unit Field', 'Opening Field',
                            'Male Diversity Field', 'Female Diversity Field', 'Job created Button',
                            'Job created Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_creation_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def job_getby_report(self, job_getby_coll):
        testdata_headers = ['Tab Validation', 'Job Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_getby_coll,
                                     row=16, i_column=0, o_column=1, path=self.__path)

    def job_sp_report(self, job_sp_coll):
        testdata_headers = ['Job Actions', 'Tag Selection Process Action', 'Select Selection Process', 'Save',
                            'Tagged Notifier', 'Page Refresh']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_sp_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def job_ec_report(self, job_ec_coll):
        testdata_headers = ['Configuration Tab', 'Ec Configure', 'Enter EC', 'Enter Positive stage',
                            'Enter Positive status', 'Enter Negative stage', 'Enter Negative status', 'Save EC',
                            'EC Notifier validate', 'EC Notifier Dismissed']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_ec_coll,
                                     row=8, i_column=2, o_column=3, path=self.__path)

    def job_task_report(self, job_ec_coll):
        testdata_headers = ['Task Configure', 'Task New Row', 'Assign Stage_Status', 'Positive Stage_Status',
                            'Negative Stage_Status', 'Activity Field Enter', 'Task Field', 'Search Task',
                            'Move all Items', 'Done', 'Task Save', 'Task Notifier Validate', 'Task Notifier Dismissed']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_ec_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def job_tag_int_report(self, job_int_coll):
        testdata_headers = ['Job Actions', 'Tag Interviewers Action', 'Interviewer Panel selection',
                            'Interviewer Panel Add', 'Interviewer Panel Save', 'Notifier Validate', 'Notifier Dismiss',
                            'Owner Tab', 'Validate owners count']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_int_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def job_automations_report(self, job_new_feed_coll):
        testdata_headers = ['Automations Tab', 'Registration stage for Hop', 'Hop - Eligible', 'Hop - Pending',
                            'Eligibility stage for Hop', 'Hop - Aptitude', 'Hop - Pending', 'Offer stage for Hop',
                            'Hop - Interview', 'Hop - Ready for self schedule', 'All toggle - ON', 'Automations - Save',
                            'Save - Notifier', 'Notifier - Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_new_feed_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def job_feed_report1(self, job_feed_coll):
        testdata_headers = ['Job Actions', 'Configure Feedback Action', 'Select Stage - Form1', 'Search stage - Form1',
                            'Search - Form1', 'Use Form1', 'Overall Mandatory - Form1',
                            'Reject Overall Mandatory - Form1', 'Save - Form1', 'Clear stage - Form1']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_feed_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def job_feed_report2(self, job_feed_coll):
        testdata_headers = ['Select Stage - Form2', 'Search stage - Form2', 'Search - Form2', 'Use Form2',
                            'Overall Mandatory - Form2', 'Reject Overall Mandatory - Form2', 'Save - Form2']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_feed_coll,
                                     row=12, i_column=10, o_column=11, path=self.__path)

    def job_new_form_on_report(self, job_new_form_on_coll):
        testdata_headers = ['Account Name', 'Settings', 'Interview Module', 'New Form Settings', 'New Form - On',
                            'Notifier Validate', 'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_new_form_on_coll,
                                     row=2, i_column=12, o_column=13, path=self.__path)

    def job_new_form_off_report(self, job_new_form_off_coll):
        testdata_headers = ['Account Name', 'Settings', 'Interview Module', 'New Form Settings', 'New Form - Off',
                            'Notifier Validate', 'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_new_form_off_coll,
                                     row=9, i_column=12, o_column=13, path=self.__path)

    def job_new_feed_report(self, job_new_feed_coll):
        testdata_headers = ['Job Tab', 'Advance Search', 'Job Name Enter', 'Search By Name', 'Job Name Click',
                            'Job Name Validation', 'Job Actions', 'Configure Feedback Action', 'Select Stage - NewForm',
                            'Search stage - NewForm', 'Search - NewForm', 'Use NewForm', 'Overall Mandatory - NewForm',
                            'Reject Overall Mandatory - NewForm', 'Edit - NewForm', 'Update - NewForm',
                            'Update - Notifier', 'Notifier - Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_new_feed_coll,
                                     row=2, i_column=14, o_column=15, path=self.__path)

    def req_creation_report(self, req_creation_coll):
        testdata_headers = ['Requirement Tab', 'Requirement Create Button', 'Requirement Name', 'Requirement Job Name',
                            'Job Search', 'Move All Items', 'Done', 'Hiring Track', 'College Type',
                            'Requirement created Button', 'Requirement created Notifier',
                            'Requirement Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=req_creation_coll,
                                     row=21, i_column=0, o_column=1, path=self.__path)

    def req_configuration_report(self, req_creation_coll):
        testdata_headers = ['Configurations Tab', 'Duplicity Check tab', 'Duplicity - Do not Allow',
                            'Duplicity Notifier', 'Duplicity Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=req_creation_coll,
                                     row=33, i_column=0, o_column=1, path=self.__path)

    def test_clone_report(self, test_clone_coll):
        testdata_headers = ['Assessment Tab', 'Advance search', 'Old Test name Enter', 'Search Button', 'Name Click',
                            'Assessment Name validation', 'Assessment Actions', 'Clone Assessment Action',
                            'New Test NAME', 'From Date', 'To Date', 'Clone Button Click', 'Clone Assessment Notifier',
                            'Clone Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=test_clone_coll,
                                     row=21, i_column=2, o_column=3, path=self.__path)
