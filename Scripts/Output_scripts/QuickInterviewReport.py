from Scripts.HTML_Reports.html_css_script import HTMLReport
from utilities import excelWrite
from Config import outputFile


class QuickOutputReport:

    """ Number of Test cases / use cases name """
    TestCases = 96
    use_case_name = 'QUICK INTERVIEW FLOW'
    fail_color = ''

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Quick_Interview_output']
        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=self.TestCases)

        excel_headers_1 = ['Event (Applicants)', 'Status', 'Quick Interview (screen)', 'Status',
                           'Quick Interview (schedule)', 'Status', 'Interview_1 (Login)', 'Status', 'Event (search)',
                           'Status', 'Interview_1 (Feedback)', 'Status']
        color_headers_1 = ['Status', 'Event (Applicants)', 'Quick Interview (screen)', 'Quick Interview (schedule)',
                           'Interview_1 (Feedback)', 'Event (search)', 'Interview_1 (Login)']
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

        excel_headers_2 = ['Interview_2 (Login)', 'Status', 'Event (search)', 'Status', 'Interview_2 (Partial Submit)',
                           'Status', 'Interview_2 (Feedback)', 'Status']
        color_headers_2 = ['Status', 'Interview_2 (Login)', 'Event (search)', 'Interview_2 (Partial Submit)',
                           'Interview_2 (Feedback)']
        self.xlw.excel_header_by_index(row=14, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

        """ <<<================== HTML Report Generator =================================>>> """
        self.__html_path = outputFile.OUTPUT_PATH['Quick_Interview_output_html']
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

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name=self.use_case_name)

    def event_app_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Name Field', 'Search Button',
                            'Event Card Click', 'Event validate', 'Event Actions', 'View Applicant Action',
                            'Applicant Advance Search', 'Applicant Name Enter', 'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def quick_report(self, quick_coll):
        testdata_headers = ['Select Applicant', 'More Actions', 'Quick Interview Action', 'Select Interviewers Field',
                            'Search Interviewer_1', 'Move Interviewer_1', 'Clear Search', 'Search Interviewer_2',
                            'Move Interviewer_2', 'Done selection']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=quick_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def quick_schedule_report(self, quick_schedule_coll):
        testdata_headers = ['Interview Stage selection', 'Quick Comment', 'Quick Schedule', 'Quick Schedule Notifier',
                            'Quick Schedule Notifier Dismiss', 'Applicant Name Click', 'Candidate status - Schedule',
                            'Window Close', 'Switch to Old screen']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=quick_schedule_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def interviewer1_login_report(self, int1_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def interviewer1_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def interviewer1_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['shortlist - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def interviewer2_login_report(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=15, i_column=0, o_column=1, path=self.__path)

    def interviewer2_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=15, i_column=2, o_column=3, path=self.__path)

    def interviewer2_partial_report(self, int1_pf_coll):
        testdata_headers = ['shortlist - decision', 'Ratings', 'comments', 'overall comment', 'Partial Submission',
                            'Feedback validation Agree', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=15, i_column=4, o_column=5, path=self.__path)

    def interviewer2_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['Partial Bucket', 'Select Applicant', 'Feedback Provide Action', 'Switch to new tab',
                            'Submit feedback', 'Feedback validation Agree', 'Review Feedback', 'Close Tab',
                            'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=15, i_column=6, o_column=7, path=self.__path)
