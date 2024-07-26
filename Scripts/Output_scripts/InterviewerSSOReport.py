from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class SSOInterviewerReport:
    """ Number of Test cases / use cases name """
    TestCases = 15
    use_case_name = 'INTERVIEWER SSO FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['sso_interviewer_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Access Token', 'Status', 'Schedule API', 'Status', 'Video Link', 'Status',
                         'SSO-GOOGLE', 'Status', 'Proctoring Screen', 'Status', 'Cancel API', 'Status']
        color_headers = ['Status', 'Access Token', 'Schedule API', 'Video Link', 'SSO-GOOGLE', 'Proctoring Screen',
                         'Cancel API']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['SSO_interviewer_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['sso_interviewer_output_html']
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
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def saml_link_report(self, login_coll):
        testdata_headers = ['Video Link Entered']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=3, i_column=2, o_column=3, path=self.__path)

    def video_link_report(self, login_coll):
        testdata_headers = ['Page Header Validation', 'Go To Interview', 'Page Header Validation', 'Switch Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def sso_login_report(self, login_coll):
        testdata_headers = ['Google Email', 'Next button', 'Google Password', 'Next button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def proctoring_report(self, login_coll):
        testdata_headers = ['Page Header Validation', 'Close Window', 'Switch To Main']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def cancel_api_call_report(self, login_coll):
        testdata_headers = ['Cancel API']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=login_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)
