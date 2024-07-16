from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class ReviseFeedbackReport:
    """ Number of Test cases / use cases name """
    TestCases = 115
    use_case_name = 'REVISE FEEDBACK FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['revise_feedback_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Admin Login', 'Status', 'Event Search', 'Status', 'Applicant Search', 'Status',
                         'Schedule Interview', 'Status', 'Candidate Verification', 'Status']
        color_headers = ['Status', 'Admin Login', 'Event Search', 'Applicant Search', 'Schedule Interview',
                         'Candidate Verification']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Interviewer Login', 'Status', 'Event Search', 'Status', 'Event Interviews', 'Status',
                         'Provide Feedback', 'Status']
        color_headers = ['Status', 'Interviewer Login', 'Event Search', 'Event Interviews', 'Provide Feedback']
        self.xlw.excel_header_by_index(row=14, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Admin Re-Login', 'Status', 'Event Search', 'Status', 'Applicant Search', 'Status',
                         'Revise Feedback Enable', 'Status', 'Candidate Verification', 'Status']
        color_headers = ['Status', 'Admin Re-Login', 'Event Search', 'Applicant Search', 'Revise Feedback Enable',
                         'Candidate Verification']
        self.xlw.excel_header_by_index(row=24, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Interviewer Login', 'Status', 'Event Search', 'Status', 'Event Interviews', 'Status',
                         'Provide Feedback', 'Status']
        color_headers = ['Status', 'Interviewer Login', 'Event Search', 'Event Interviews', 'Provide Feedback']
        self.xlw.excel_header_by_index(row=33, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Revise_feedback_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Revise_feedback_output_html']
        self.history_data_with_html_report = HistoryDataHTMLGenerator(self.__history_path, self.__html_path)
        self.amazon_s3 = AWS('{}.html'.format(self.use_case_name), self.__html_path)

    def history_html_generator(self):
        self.history_data_with_html_report.html_report_generation(self.server, self.version, self.start_date_time,
                                                                  self.use_case_name, self.xlw.result,
                                                                  self.xlw.total_cases, self.xlw.pass_cases,
                                                                  self.xlw.failure_cases, self.xlw.percentage,
                                                                  self.xlw.minutes, self.time, self.xlw.date_now,
                                                                  self.__path)
        self.amazon_s3.file_handler()

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name=self.use_case_name)

    def admin_login_report(self, login_coll):
        testdata_headers = ['Enter Alias', 'Next Button', 'Login Name', 'Password', 'Login Button',
                            'Verify User Login']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def event_search_report(self, login_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button', 'GetBy Event Name',
                            'Event Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def applicant_search_report(self, login_coll):
        testdata_headers = ['Event Actions', 'View Applicants', 'Advance Search', 'Applicant Name Field',
                            'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def applicant_status_change_report(self, login_coll):
        testdata_headers = ['All Applicants check Box', 'Change Status Action', 'Stage', 'Status',
                            'Interviewers Field', 'Search Interviewers', 'Move All', 'Done Button', 'Comment',
                            'Change Button', 'Notifier Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def candidate_status_verification_report(self, login_coll):
        testdata_headers = ['Applicant Get By Name', 'Switch To Details Page', 'Status Verification',
                            'Close Switch Window', 'Main window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def interviewer_report(self, login_coll):
        testdata_headers = ['Account Center', 'Logout Button', 'Login Again', 'Login Name',
                            'Login Password', 'Login Button', 'Login User Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=15, i_column=0, o_column=1, path=self.__path)

    def int_event_search_report(self, login_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button', 'GetBy Event Name',
                            'Event Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=15, i_column=2, o_column=3, path=self.__path)

    def int_event_interview_report(self, login_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Search Button',
                            'Name Search Field', 'Search Button', 'Select IR', 'Provide Feedback Action',
                            'Switch Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=15, i_column=4, o_column=5, path=self.__path)

    def int_provide_feedback_report(self, login_coll):
        testdata_headers = ['Question Rating', 'Question Comment', 'Feedback Decision', 'Overall Comment',
                            'Submit Feedback', 'Agree And Submit', 'Switch to Main Tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=15, i_column=6, o_column=7, path=self.__path)

    def crpo_admin_re_login_report(self, login_coll):
        testdata_headers = ['Account Center', 'Logout Button', 'Login Again', 'Login Name',
                            'Login Password', 'Login Button', 'Login User Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=25, i_column=0, o_column=1, path=self.__path)

    def re_login_event_search_report(self, login_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button', 'GetBy Event Name',
                            'Event Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=25, i_column=2, o_column=3, path=self.__path)

    def re_login_applicant_search_report(self, login_coll):
        testdata_headers = ['Event Actions', 'View Applicants', 'Advance Search', 'Applicant Name Field',
                            'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=25, i_column=4, o_column=5, path=self.__path)

    def revise_feedback_report(self, login_coll):
        testdata_headers = ['All Applicants check Box', 'More Actions', 'Revise Feedback Action', 'Comment',
                            'Revise Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=25, i_column=6, o_column=7, path=self.__path)

    def candidate_revise_status_verification_report(self, login_coll):
        testdata_headers = ['Applicant Get By Name', 'Switch To Details Page', 'Status Verification',
                            'Close Switch Window', 'Main window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=25, i_column=8, o_column=9, path=self.__path)

    def interviewer_revise_report(self, login_coll):
        testdata_headers = ['Account Center', 'Logout Button', 'Login Again', 'Login Name',
                            'Login Password', 'Login Button', 'Login User Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=34, i_column=0, o_column=1, path=self.__path)

    def int_event_search_revise_report(self, login_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button', 'GetBy Event Name',
                            'Event Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=34, i_column=2, o_column=3, path=self.__path)

    def int_event_interview_revise_report(self, login_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Search Button',
                            'Name Search Field', 'Search Button', 'Select IR', 'Provide Feedback Action',
                            'Switch Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=34, i_column=4, o_column=5, path=self.__path)

    def int_provide_feedback_revise_report(self, login_coll):
        testdata_headers = ['Question Rating', 'Question Comment', 'Feedback Decision', 'Overall Comment',
                            'Submit Feedback', 'Agree And Submit', 'Switch to Main Tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=34, i_column=6, o_column=7, path=self.__path)
