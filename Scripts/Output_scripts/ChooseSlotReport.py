from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class ChooseSlotReport:
    """ Number of Test cases / use cases name """
    TestCases = 27
    use_case_name = 'CHOOSE SLOTS FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['ChooseSlot_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Captcha Verification', 'Status', 'Choose Slot', 'Status']
        color_headers = ['Status', 'Captcha Verification', 'Choose Slot']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Admin Login', 'Status', 'Event Search', 'Status', 'Event Applicant', 'Status',
                         'Candidate Verification', 'Status']
        color_headers = ['Status', 'Admin Login', 'Event Search', 'Event Applicant', 'Candidate Verification']
        self.xlw.excel_header_by_index(row=8, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Choose_slot_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Choose_slot_output_html']
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
        testdata_headers = ['Captcha Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=entry_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def choose_slot_report(self, pd_coll):
        testdata_headers = ['Choose Slot One', 'Reset', 'Choose SLot One', 'Submit', 'Thank you Page!']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=pd_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def update_choose_slot_report(self, pd_coll):
        testdata_headers = ['Choose Slot One', 'Submit', 'Thank you Page!']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=pd_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def admin_login_report(self, admin_coll):
        testdata_headers = ['Enter Alias', 'Next Button', 'Login Name', 'Password', 'Login Button',
                            'Verify User Login']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=9, i_column=0, o_column=1, path=self.__path)

    def event_search_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Name Field', 'Search Button', 'Event Getbyname',
                            'Event name Validation', 'Event Action', 'View Applicants']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=9, i_column=2, o_column=3, path=self.__path)

    def candidate_search_report(self, event_coll):
        testdata_headers = ['Event Actions', 'Applicants', 'Search', 'Search Button', 'Candidate Getbyname',
                            'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=9, i_column=4, o_column=5, path=self.__path)

    def candidate_verification_report(self, event_coll):
        testdata_headers = ['Status Verification', 'Close Switch Window', 'Main window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=9, i_column=6, o_column=7, path=self.__path)

