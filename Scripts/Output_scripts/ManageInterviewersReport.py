from datetime import datetime
from Scripts.HTML_Reports.amazon_aws_s3 import AWS
from Scripts.HTML_Reports.history_data_html_generator import HistoryDataHTMLGenerator
from utilities import excelWrite
from Config import outputFile


class ManageInterviewersOutputReport:

    """ Number of Test cases / use cases name """
    TestCases = 77
    use_case_name = 'MANAGE INTERVIEWERS FLOW'
    fail_color = ''

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.time = datetime.now()
        self.__path = outputFile.OUTPUT_PATH['Manage_output']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=self.TestCases)

        excel_headers_1 = ['Event(Search)', 'Status', 'Panel_1(criteria)', 'Status', 'Panel_2(criteria)',
                           'Status', 'Send Mail (Nominations)', 'Status']
        color_headers_1 = ['Event(Search)', 'Panel_1(criteria)', 'Panel_2(criteria)', 'Send Mail (Nominations)',
                           'Status']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Login(Interviewer1)', 'Status', 'Nomination(Accept)', 'Status', 'Login(Interviewer2)',
                           'Status', 'Nomination(Accept)', 'Status']
        color_headers_2 = ['Login(Interviewer1)', 'Nomination(Accept)', 'Login(Interviewer2)', 'Nomination(Accept)',
                           'Status']
        self.xlw.excel_header_by_index(row=10, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

        excel_headers_3 = ['Login(Event Manager)', 'Status', 'Event(Search)', 'Status', 'Recruiter(Approval)', 'Status',
                           'Sync(Tag Interviewers)', 'Status']
        color_headers_3 = ['Login(Event Manager)', 'Event(Search)', 'Recruiter(Approval)', 'Sync(Tag Interviewers)',
                           'Status']
        self.xlw.excel_header_by_index(row=18, col=0, excel_headers_list=excel_headers_3,
                                       color_headers_list=color_headers_3)

        """ <<<================== HTML / History Report Generator ==============================>>> """
        self.__history_path = outputFile.OUTPUT_PATH['Manage_output_history']
        self.__html_path = outputFile.OUTPUT_PATH['Manage_output_html']
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

    def event_search_report(self, collection):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button',
                            'Event name GetByid', 'Event Name Validation', 'Event Actions Clicked',
                            'Manage Interviewers Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def skill1_search_report(self, collection):
        testdata_headers = ['Add Criteria', 'Panel(Technical Java)', 'Search(Interviewers)', 'Interviewer(Count)',
                            'Nominations(Count)']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def skill2_search_report(self, collection):
        testdata_headers = ['Panel(Technical Java)', 'Search(Interviewers)', 'Interviewer(Count)', 'Nominations(Count)']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def send_mail_report(self, collection):
        testdata_headers = ['Send Mail Interviewers', 'Confirm(Event Level On)', 'Confirm(Send mail)',
                            'Confirm(Event is Today)', 'Criteria Notifier',
                            'Notifier Dismiss', 'Nomination Tab', 'Header validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def interviewer1_login_report(self, collection):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=11, i_column=0, o_column=1, path=self.__path)

    def interviewer1_confirm_report(self, collection):
        testdata_headers = ['Nomination Tab', 'Validate Job role', 'Confirm by Interviewers',
                            'Ok - Confirmation', 'Validate acceptance']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=11, i_column=2, o_column=3, path=self.__path)

    def interviewer2_login_report(self, collection):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=11, i_column=4, o_column=5, path=self.__path)

    def interviewer2_confirm_report(self, collection):
        testdata_headers = ['Nomination Tab', 'Validate Job role', 'Confirm by Interviewers',
                            'Ok - Confirmation', 'Validate acceptance']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=11, i_column=6, o_column=7, path=self.__path)

    def recruiter_login_report(self, collection):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=19, i_column=0, o_column=1, path=self.__path)

    def event_report(self, collection):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button',
                            'Event name GetByid',
                            'Event Name Validation', 'Event Actions Clicked', 'Manage Interviewers Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=19, i_column=2, o_column=3, path=self.__path)

    def approval_report(self, collection):
        testdata_headers = ['Refresh List', 'Panel(Technical Java)', 'Select Applicant', 'Actions', 'Approve',
                            'Refresh List','Panel(Technical NodeJs)', 'Select Applicant', 'Actions', 'Approve']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=19, i_column=4, o_column=5, path=self.__path)

    def sync_report(self, collection):
        testdata_headers = ['Sync(approved interviewers)', 'Sync Notifier', 'notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=19, i_column=6, o_column=7, path=self.__path)
