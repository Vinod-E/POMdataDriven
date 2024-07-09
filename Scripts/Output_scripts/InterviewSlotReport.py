from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class AadharOutputReport:
    """ Number of Test cases / use cases name """
    TestCases = 33
    use_case_name = 'INTERVIEW SLOTS FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['InterviewSlot_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Personal Details', 'Status', 'Aadhar Verification', 'Status']
        color_headers = ['Status', 'Personal Details', 'Aadhar Verification']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Admin Login', 'Status', 'Event Search', 'Status', 'Applicant Search', 'Status',
                         'Aadhar Communication', 'Status']
        color_headers = ['Status', 'Admin Login', 'Event Search', 'Applicant Search', 'Aadhar Communication']
        self.xlw.excel_header_by_index(row=9, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Interview_slot_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Interview_slot_output_html']
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

    def entry_page_report(self, entry_coll):
        testdata_headers = ['Entry Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=entry_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def personal_details_report(self, pd_coll):
        testdata_headers = ['Full Name', 'Email', 'Aadhar Number']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=pd_coll,
                                     row=3, i_column=0, o_column=1, path=self.__path)

    def submit_and_aadhar_data_report(self, submit_coll):
        testdata_headers = ['Submit', 'Generate Aadhar OTP', 'Submit Aadhar OTP', 'Proceed with Aadhar verified',
                            'Confirm and Submit', 'Registration Successfully']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=submit_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def admin_login_report(self, admin_coll):
        testdata_headers = ['Enter Alias', 'Next Button', 'Login Name', 'Password', 'Login Button',
                            'Verify User Login']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=10, i_column=0, o_column=1, path=self.__path)

    def event_search_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Name Field', 'Search Button', 'Event Getbyname',
                            'Event name Validation', 'Event Action', 'View Applicants']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=10, i_column=2, o_column=3, path=self.__path)

    def applicant_search_report(self, applicant_coll):
        testdata_headers = ['Advance Search', 'Name Field', 'Search Button', 'Applicant Getbyname']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_coll,
                                     row=10, i_column=4, o_column=5, path=self.__path)

    def aadhar_verification_report(self, applicant_coll):
        testdata_headers = ['Aadhar Number Verified', 'Communication Tab', 'Open communication status',
                            'Aadhar Verified - True', 'Window Close', 'Switch To Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=applicant_coll,
                                     row=10, i_column=6, o_column=7, path=self.__path)

