from utilities import excelWrite
from Config import outputFile


class LiveOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Live_Interview_output']
        test_cases = 76
        excel_headers_1 = ['Event Search', 'Status', 'Live Schedule', 'Status', 'Interviewer_1 Login', 'Status',
                           'Applicant (stage feedback)', 'Status', 'Interviewer-1 (Feedback)', 'Status',
                           'Interviewer-2 Login', 'Status', 'Applicant (stage feedback)', 'Status',
                           'Interviewer-2 (Feedback)', 'Status']
        color_headers_1 = ['Status', 'Event Search', 'Live Schedule', 'Interviewer_1 Login', 'Interviewer_2 Login',
                           'Applicant (stage feedback)', 'Interviewer-1 (Feedback)', 'Interviewer-2 (Feedback)']

        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='LIVE INTERVIEW FLOW')

    def event_name_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search', 'Event Name Field', 'Search Button', 'Event name GetByid',
                            'Event Name Validation', 'Event Actions Clicked', 'Live Interview Schedule Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def live_schedule_report(self, live_coll):
        testdata_headers = ['Stage Selection', 'Applicant Name search', 'Search', 'Select Applicant', 'Schedule select',
                            'Validate Screen', 'Select Interviewers', 'Live Schedule', 'Notifier', 'Notifier Dismiss']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=live_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def interviewer1_login_report(self, int1_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def interviewer1_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Live Interview Schedule Action', 'Stage Selection',
                            'Applicant Name search', 'Search', 'Arrow Down', 'Feedback Provide Action',
                            'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def interviewer1_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['shortlist - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def interviewer2_login_report(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def interviewer2_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Live Interview Schedule Action', 'Stage Selection',
                            'Applicant Name search', 'Search', 'Arrow Down', 'Feedback Provide Action',
                            'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=12, o_column=13, path=self.__path)

    def interviewer2_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['shortlist - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=2, i_column=14, o_column=15, path=self.__path)