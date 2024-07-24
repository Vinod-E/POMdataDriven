from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class SSOCandidateReport:
    """ Number of Test cases / use cases name """
    TestCases = 15
    use_case_name = 'SSO FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['sso_candidate_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Admin Login', 'Status', 'Event Search', 'Status', 'Applicant Search', 'Status',
                         'Schedule Interview', 'Status', 'Candidate Verification', 'Status']
        color_headers = ['Status', 'Admin Login', 'Event Search', 'Applicant Search', 'Schedule Interview',
                         'Candidate Verification']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['SSO_candidate_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['sso_candidate_output_html']
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

    def login_api_call_report(self, login_coll):
        testdata_headers = ['Access API']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def schedule_api_call_report(self, login_coll):
        testdata_headers = ['Schedule API']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=3, i_column=0, o_column=1, path=self.__path)

    def cancel_api_call_report(self, login_coll):
        testdata_headers = ['Cancel API']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=4, i_column=0, o_column=1, path=self.__path)