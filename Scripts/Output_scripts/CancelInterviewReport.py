from datetime import datetime
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator
from utilities import excelWrite
from Config import outputFile


class CancelInterviewOutputReport:

    """ Number of Test cases / use cases name """
    TestCases = 119
    use_case_name = 'CANCEL INTERVIEW FLOW'
    fail_color = ''

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['Cancel_Interview_output']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=self.TestCases)

        excel_headers_1 = ['Event (Applicants)', 'Status', 'Applicant (Status change)', 'Status', 'Interview_1 (Login)',
                           'Status', 'Interview_1 (Cancel Request Raise)', 'Status', 'Admin (login)', 'Status',
                           'Admin (Accept Request)', 'Status', 'Event (search)', 'Status']
        color_headers_1 = ['Status', 'Event (Applicants)', 'Applicant (Status change)', 'Interview_1 (Login)',
                           'Interview_1 (Cancel Request Raise)', 'Admin (login)', 'Admin (Accept Request)',
                           'Event (search)']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Applicant (Status change2)', 'Status', 'Interview_2 (Login)', 'Status',
                           'Interview_2 (Cancel Interview)', 'Status']
        color_headers_2 = ['Status', 'Applicant (Status change2)', 'Interview_2 (Login)',
                           'Interview_2 (Cancel Interview)']
        self.xlw.excel_header_by_index(row=17, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Cancel_Interview_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Cancel_Interview_output_html']
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

    def event_app_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Name Field', 'Search Button',
                            'Event Card Click', 'Event validate', 'Event Actions', 'View Applicant Action',
                            'Applicant Advance Search', 'Applicant Name Enter', 'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def change_status_report(self, status_coll):
        testdata_headers = ['Select Applicant', 'Change Applicant Status', 'Select Stage', 'Select Status',
                            'Select Interviewers', 'Move all Interviewers', 'Done', 'Comment', 'Change Button',
                            'Change Status Notifier', 'Change Status Notifier Dismiss', 'Applicant Get name',
                            'Candidate Status Validate', 'Window Close', 'Switch to Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=status_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def interviewer1_login_report(self, int1_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Event Tab', 'Advance Search Action',
                            'Advance Name Field', 'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def interviewer1_request_report(self, int1_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Cancellation Request Action', 'Request Reason',
                            'Request Comment', 'Request Confirm', 'Notifier', 'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def admin_login_report(self, admin_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Event Tab', 'Advance Search Action',
                            'Advance Name Field', 'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def admin_acceptance_report(self, admin_coll):
        testdata_headers = ['Tracking Tab', 'Cancel request Tab', 'Accept Button', 'Comment', 'Confirm acceptance',
                            'Go Ahead button', 'Accept Button', 'Comment', 'Confirm acceptance', 'Notifier',
                            'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def event_action_report(self, action_coll):
        testdata_headers = ['Event Actions', 'View Applicant Action', 'Applicant Advance Search',
                            'Applicant Name Enter', 'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=action_coll,
                                     row=2, i_column=12, o_column=13, path=self.__path)

    def change_status_report2(self, status_coll):
        testdata_headers = ['Select Applicant', 'Change Applicant Status', 'Select Stage', 'Select Status',
                            'Select Interviewers', 'Move all Interviewers', 'Done', 'Comment', 'Change Button',
                            'Change Status Notifier', 'Change Status Notifier Dismiss', 'Applicant Get name',
                            'Candidate Status Validate', 'Window Close', 'Switch to Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=status_coll,
                                     row=18, i_column=0, o_column=1, path=self.__path)

    def interviewer2_login_report(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Event Tab', 'Advance Search Action',
                            'Advance Name Field', 'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=18, i_column=2, o_column=3, path=self.__path)

    def interviewer2_cancel_report(self, int1_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Cancellation Interview Action',
                            'Request Comment', 'Request Confirm', 'Notifier', 'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=18, i_column=4, o_column=5, path=self.__path)
