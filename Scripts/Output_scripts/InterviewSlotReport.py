from datetime import datetime
from utilities import excelWrite
from Config import outputFile
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator


class InterviewSlotOutputReport:
    """ Number of Test cases / use cases name """
    TestCases = 26
    use_case_name = 'INTERVIEW SLOTS FLOW'

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['InterviewSlot_output']
        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)

        excel_headers = ['Captcha Page', 'Status', 'Slot Page', 'Status']
        color_headers = ['Status', 'Captcha Page', 'Slot Page']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers,
                                       color_headers_list=color_headers)

        excel_headers = ['Admin Login', 'Status', 'Event Search', 'Status', 'Event Tracking', 'Status',
                         'UnAssign Slot', 'Status']
        color_headers = ['Status', 'Admin Login', 'Event Search', 'Event Tracking', 'UnAssign Slot']
        self.xlw.excel_header_by_index(row=7, col=0, excel_headers_list=excel_headers,
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
        testdata_headers = ['Header Verification', 'Captcha Verification']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=entry_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def slot_page_report(self, entry_coll):
        testdata_headers = ['Select Slot Time', 'Save Slot', 'Thank you page', 'Already slot Assigned']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=entry_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def admin_login_report(self, admin_coll):
        testdata_headers = ['Enter Alias', 'Next Button', 'Login Name', 'Password', 'Login Button',
                            'Verify User Login']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=8, i_column=0, o_column=1, path=self.__path)

    def event_search_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Name Field', 'Search Button', 'Event Getbyname',
                            'Event name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=8, i_column=2, o_column=3, path=self.__path)

    def event_tracking_report(self, event_coll):
        testdata_headers = ['Tracking Tab', 'Interview SLot Tab', 'Stage field click', 'Stage Filter Value', 'GO Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=8, i_column=4, o_column=5, path=self.__path)

    def unassign_slot_report(self, event_coll):
        testdata_headers = ['All Assigned', 'Unassign icon', 'Success-OK']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=8, i_column=6, o_column=7, path=self.__path)
