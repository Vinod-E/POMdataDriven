from datetime import datetime
from Scripts.HTML_Reports.html_css_script import HTMLReport
from utilities import excelWrite
from Config import outputFile
from utilities.HistoryexcelWriter import HistoryOutput


class HelpDeskOutputReport:

    """ Number of Test cases / use cases name """
    TestCases = 96
    use_case_name = 'QUERY HELP DESK FLOW'
    fail_color = ''

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['Help_desk_output']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=self.TestCases)

        excel_headers_1 = ['Event (Applicants)', 'Status']
        color_headers_1 = ['Status', 'Event (Applicants)']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        """ <<<================== HTML / History Report Generator =================================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Help_desk_output_history']
        self.history = HistoryOutput(self.__history_path)
        self.__html_path = outputFile.OUTPUT_PATH['Help_desk_output_html']
        self.html_generator = HTMLReport(self.__html_path)

    def html_report_generation(self):
        if self.xlw.failure_cases != 0:
            self.fail_color = 'summaryFail'
        else:
            self.fail_color = 'summaryPass'

        self.html_generator.html_css(self.server, self.version, self.xlw.date_now,
                                     self.use_case_name, self.xlw.result,
                                     self.xlw.total_cases, self.xlw.pass_cases,
                                     self.xlw.failure_cases, self.fail_color)

        self.history.create_pandas_excel(self.server, self.xlw.date_now, self.time,
                                         self.version, self.xlw.total_cases, self.xlw.pass_cases,
                                         self.xlw.failure_cases, self.xlw.minutes)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name=self.use_case_name)

    def event_app_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Name Field', 'Search Button',
                            'Event Card Click', 'Event validate', 'Event Actions', 'View Applicant Action',
                            'Applicant Advance Search', 'Applicant Name Enter', 'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)
