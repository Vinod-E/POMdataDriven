from datetime import datetime
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator
from utilities import excelWrite
from Config import outputFile


class HelpDeskOutputReport:

    """ Number of Test cases / use cases name """
    TestCases = 124
    use_case_name = 'QUERY HELP DESK FLOW'
    fail_color = ''

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['Help_desk_output']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=self.TestCases)

        excel_headers_1 = ['Requirement (Configuration)', 'Status', 'Default Configuration', 'Status',
                           'Job Configuration', 'Status', 'Event Configuration', 'Status', 'Save configuration',
                           'Status']
        color_headers_1 = ['Status', 'Requirement (Configuration)', 'Default Configuration', 'Job Configuration',
                           'Event Configuration', 'Save configuration']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Candidate (login)', 'Status', 'Query (Admit card)', 'Status', 'Query (Accommodation)',
                           'Status', 'Query (Application Filling)', 'Status']
        color_headers_2 = ['Candidate (login)', 'Query (Admit card)', 'Query (Accommodation)',
                           'Query (Application Filling)', 'Status']
        self.xlw.excel_header_by_index(row=19, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

        excel_headers_3 = ['User_1 Login', 'Status', 'Query Reply', 'Status', 'User_2 Login', 'Status', 'Query Reply',
                           'Status', 'User_3 Login', 'Status', 'Query Reply', 'Status']
        color_headers_3 = ['User_1 Login', 'Query Reply', 'User_2 Login', 'Query Reply',
                           'User_3 Login', 'Query Reply', 'Status']
        self.xlw.excel_header_by_index(row=28, col=0, excel_headers_list=excel_headers_3,
                                       color_headers_list=color_headers_3)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Help_desk_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Help_desk_output_html']
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

    def req_config_report(self, collection):
        testdata_headers = ['Requirement Tab', 'Advance Search Action', 'Advance Name Field', 'Search Button',
                            'Requirement Card Click', 'Requirement validate', 'Configurations Tab', 'Query Tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def default_query_report(self, collection):
        testdata_headers = ['Admit card Category', 'Search', 'Select', 'Done', 'User', 'Search', 'Select', 'Done',
                            'SLA']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def job_query_report(self, collection):
        testdata_headers = ['Accommodation card Category', 'Search', 'Select', 'Done', 'Job', 'Search', 'Select',
                            'Done', 'User', 'Search', 'Select', 'Done', 'SLA']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def event_query_report(self, collection):
        testdata_headers = ['Application Filling Category', 'Search', 'Select', 'Done', 'Job', 'Search', 'Select',
                            'Done', 'Event', 'Search', 'Done', 'Select', 'User', 'Search', 'Select', 'Done', 'SLA']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def save_query_report(self, collection):
        testdata_headers = ['Save Query Config', 'Validate Notifier', 'Dismiss Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def candidate_login_report(self, collection):
        testdata_headers = ['Login Url Entered', 'Login Name', 'Password', 'Login', 'Validate Account name']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=20, i_column=0, o_column=1, path=self.__path)

    def query_1_report(self, collection):
        testdata_headers = ['Help Menu', 'More Queries', 'Category select', 'Subject Entry', 'Message Entry',
                            'Query Raise', 'Validate Notifier', 'Dismiss Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=20, i_column=2, o_column=3, path=self.__path)

    def query_2_report(self, collection):
        testdata_headers = ['Help Menu', 'More Queries', 'Category select', 'Subject Entry', 'Message Entry',
                            'Query Raise', 'Validate Notifier', 'Dismiss Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=20, i_column=4, o_column=5, path=self.__path)

    def query_3_report(self, collection):
        testdata_headers = ['Help Menu', 'More Queries', 'Category select', 'Subject Entry', 'Message Entry',
                            'Query Raise', 'Validate Notifier', 'Dismiss Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=20, i_column=6, o_column=7, path=self.__path)

    def user_1_login_report(self, collection):
        testdata_headers = ['Login Url Entered', 'Login Name', 'Password', 'Login', 'Validate Account name']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=0, o_column=1, path=self.__path)

    def reply_1_query_report(self, collection):
        testdata_headers = ['Query Search', 'Click on Query Card', 'Message Entry', 'Reply',
                            'In Progress Tab', 'Query Search', 'Click on Query Card', 'Message Entry',
                            'Mark as closed', 'Confirm']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=2, o_column=3, path=self.__path)

    def user_2_login_report(self, collection):
        testdata_headers = ['Login Url Entered', 'Login Name', 'Password', 'Login', 'Validate Account name']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=4, o_column=5, path=self.__path)

    def reply_2_query_report(self, collection):
        testdata_headers = ['Query Search', 'Click on Query Card', 'Message Entry', 'Reply',
                            'In Progress Tab', 'Query Search', 'Click on Query Card', 'Message Entry',
                            'Mark as closed', 'Confirm']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=6, o_column=7, path=self.__path)

    def user_3_login_report(self, collection):
        testdata_headers = ['Login Url Entered', 'Login Name', 'Password', 'Login', 'Validate Account name']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=8, o_column=9, path=self.__path)

    def reply_3_query_report(self, collection):
        testdata_headers = ['Query Search', 'Click on Query Card', 'Message Entry', 'Reply',
                            'In Progress Tab', 'Query Search', 'Click on Query Card', 'Message Entry',
                            'Mark as closed', 'Confirm']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=29, i_column=10, o_column=11, path=self.__path)
