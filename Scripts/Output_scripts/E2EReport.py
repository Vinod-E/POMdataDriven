from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class E2EOutputReport:
    """ Number of Test cases / use cases name """
    TestCases = 269
    use_case_name = 'E2E REGRESSION FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['E2E_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers_1 = ['Create Job', 'Status', 'Job (SP / EC)', 'Status', 'Job (Task)', 'Status',
                           'Job Interviewers', 'Status', 'Job (Old Form)', 'Status', 'Settings - NewForm (ON/OFF)',
                           'Status', 'Job (New Form)', 'Status', 'Job Automations', 'Status']
        color_headers_1 = ['Status', 'Create Job', 'Job (SP / EC)', 'Job (Task)', 'Job (Old Form)', 'Job (New Form)',
                           'Settings - NewForm (ON/OFF)', 'Job Interviewers', 'Job Automations']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Create Requirement', 'Status', 'Clone Assessment', 'Status', 'Create Event', 'Status',
                           'Configuration (Task)', 'Status', 'Configuration (Tag Test / Owners)', 'Status',
                           'Event Upload Candidates', 'Status', 'Applicant (hopping status)', 'Status',
                           'Applicant Status Change', 'Status']
        color_headers_2 = ['Status', 'Create Requirement', 'Clone Assessment', 'Create Event', 'Configuration (Task)',
                           'Configuration (Tag Test / Owners)', 'Event Upload Candidates', 'Applicant (hopping status)',
                           'Applicant Status Change']
        self.xlw.excel_header_by_index(row=20, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

        excel_headers_3 = ['Candidate (Manage Task)', 'Status', 'Embrace (Behalf Of Submission)', 'Status',
                           'Candidate (After Submission status)', 'Status']
        color_headers_3 = ['Status', 'Candidate (Manage Task)', 'Embrace (Behalf Of Submission)',
                           'Candidate (After Submission status)']
        self.xlw.excel_header_by_index(row=39, col=0, excel_headers_list=excel_headers_3,
                                       color_headers_list=color_headers_3)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['E2E_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['E2E_output_html']
        self.history_data_with_html_report = HistoryDataHTMLGenerator(self.__history_path, self.__html_path)

    def history_html_generator(self):
        self.history_data_with_html_report.history_data_save_read(self.server, self.xlw.date_now, self.time,
                                                                  self.version, self.xlw.total_cases,
                                                                  self.xlw.pass_cases,
                                                                  self.xlw.failure_cases, self.xlw.minutes)

        self.history_data_with_html_report.html_report_generation(self.server, self.version, self.xlw.date_now,
                                                                  self.use_case_name, self.xlw.result,
                                                                  self.xlw.total_cases, self.xlw.pass_cases,
                                                                  self.xlw.failure_cases)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name=self.use_case_name)

    def job_creation_report(self, job_creation_coll):
        testdata_headers = ['Job Tab', 'Job Create Button', 'Job Name', 'Job Attachment', 'Job Notifier', 'Description',
                            'Location Field', 'Hiring Manager Field', 'Business Unit Field', 'Opening Field',
                            'Male Diversity Field', 'Female Diversity Field', 'Job created Button',
                            'Job created Notifier', 'Job created Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_creation_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def job_getby_report(self, job_getby_coll):
        testdata_headers = ['Tab Validation', 'Job Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_getby_coll,
                                     row=17, i_column=0, o_column=1, path=self.__path)

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

    def event_create_report(self, create_event_coll):
        testdata_headers = ['Event Tab', 'New Event Create', 'New Event Name', 'Requirement Name', 'Job Name Click',
                            'Job Name search', 'Event job selected', 'Selection Done', 'Event Slot', 'Event From Date',
                            'Event To Date', 'Event Reporting Date', 'Event manager selected', 'Event College Selected',
                            'Event EC enabled', 'Event Created', 'Event create Notifier',
                            'Event create  Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=create_event_coll,
                                     row=21, i_column=4, o_column=5, path=self.__path)

    def event_task_config_report(self, config_coll):
        testdata_headers = ['Event Name Validation', 'Configurations Tab', 'Task Configure', 'Task New Row',
                            'Task Job Name', 'Assign Stage_Status', 'Positive Stage_Status', 'Negative Stage_Status',
                            'Activity Field Enter', 'Task Field', 'Move all Items', 'Done', 'Task Save',
                            'Task Notifier Validate', 'Task Notifier Dismissed']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=config_coll,
                                     row=21, i_column=6, o_column=7, path=self.__path)

    def event_test_config_report(self, config_coll):
        testdata_headers = ['Test Configure', 'Test Job Name', 'Test Stage', 'Test Assessment', 'Test Active',
                            'Save Test Config', 'Test Config Notifier', 'Test Config  Notifier Dismiss',
                            'Cancel Test Config']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=config_coll,
                                     row=21, i_column=8, o_column=9, path=self.__path)

    def event_owners_config_report(self, owners_coll):
        testdata_headers = ['Event Actions', 'Manage Event Owners Action', 'Move all Owners', 'Owners Update',
                            'Owners Notifier', 'Owners Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=owners_coll,
                                     row=30, i_column=8, o_column=9, path=self.__path)

    def event_upload_candidate_report(self, upload_candidate_coll):
        testdata_headers = ['Event Actions', 'Upload Candidate Action', 'Upload Candidate File', 'Next Button',
                            'Declare Check', 'Signature Entry', 'Agree Button', 'Edit information', 'Name Edit',
                            'Email Edit', 'USN Edit', 'Save Information', 'Save Candidate', 'Upload Count Validate',
                            'Close Upload screen', 'Close Main Screen', 'Confirm - OK']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=upload_candidate_coll,
                                     row=21, i_column=10, o_column=11, path=self.__path)

    def event_applicant_hop_status_report(self, applicant_hop_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Enter', 'Search Button', 'Event GetBy Name',
                            'Event Name Validation', 'Event Actions', 'View Candidates', 'Advance Search',
                            'Applicant Name Enter', 'Search Button', 'Applicant Name Click', 'Candidate Hop status',
                            'Close Window', 'Switch To Old window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_hop_coll,
                                     row=21, i_column=12, o_column=13, path=self.__path)

    def event_applicant_status_report(self, applicant_status_coll):
        testdata_headers = ['Applicant select', 'Applicant Change Status', 'Applicant stage Entry',
                            'Applicant status Entry', 'Comment', 'Change Button', 'Change Notifier',
                            'Change Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_status_coll,
                                     row=21, i_column=14, o_column=15, path=self.__path)

    def event_applicant_manage_report(self, applicant_status_coll):
        testdata_headers = ['Applicant Name click', 'Status Validate', 'Candidate Floating Actions',
                            'Manage Task Action', 'Candidate Name Validate', 'Submitted - 0', 'Pending - 1',
                            'Rejected - 0', 'Approved - 0', 'Total - 1', 'Switch Back Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_status_coll,
                                     row=40, i_column=0, o_column=1, path=self.__path)

    def event_embrace_report(self, embrace_coll):
        testdata_headers = ['More Tab', 'Embrace Tab', 'Switch To New Window', 'Candidate Module', 'Advance Search',
                            'Candidate Behalf of action', 'Candidate acceptance - Yes', 'Submit Task', 'Task Notifier',
                            'Task Notifier Dismiss', 'Close Window', 'Switch To Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=embrace_coll,
                                     row=40, i_column=2, o_column=3, path=self.__path)

    def event_applicant_manage_task_report(self, applicant_status_coll):
        testdata_headers = ['Applicant Name click', 'Status Validate', 'Candidate Floating Actions',
                            'Manage Task Action', 'Candidate Name Validate', 'Submitted - 1', 'Pending - 12',
                            'Rejected - 0', 'Approved - 1', 'Total - 13', 'Switch Back Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_status_coll,
                                     row=40, i_column=4, o_column=5, path=self.__path)
