from utilities import excelWrite
from Config import outputFile


class QuickOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Quick_Interview_output']
        test_cases = 88
        excel_headers_1 = ['Event (Applicants)', 'Status', 'Quick Interview (screen)', 'Status',
                           'Quick Interview (schedule)', 'Status', 'Interview_1 (Login)', 'Status', 'Event (search)',
                           'Status', 'Interview_1 (Feedback)', 'Status']
        color_headers_1 = ['Status', 'Event (Applicants)', 'Quick Interview (screen)', 'Quick Interview (schedule)',
                           'Interview_1 (Feedback)', 'Event (search)', 'Interview_1 (Login)']

        excel_headers_2 = ['Interview_2 (Login)', 'Status', 'Event (search)', 'Status', 'Interview_2 (Feedback)',
                           'Status']
        color_headers_2 = ['Status', 'Interview_2 (Login)', 'Event (search)', 'Interview_2 (Feedback)']

        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)
        self.xlw.excel_header_by_index(row=14, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='QUICK INTERVIEW FLOW')

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

    def interviewer2_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['shortlist - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=15, i_column=4, o_column=5, path=self.__path)
