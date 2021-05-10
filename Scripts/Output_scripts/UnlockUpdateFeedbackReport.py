from utilities import excelWrite
from Config import outputFile


class UnlockUpdateOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['Unlock_update_output']
        test_cases = 160
        excel_headers_1 = ['Event (Applicants)', 'Status', 'Applicant (Status change)', 'Status', 'Interview_1 (Login)',
                           'Status', 'Interview_1 (Feedback)', 'Status', 'Interview_2 (Login)', 'Status',
                           'Interview_2 (Feedback)', 'Status']
        color_headers_1 = ['Event (Applicants)', 'Applicant (Status change)', 'Interview_1 (Login)',
                           'Interview_1 (Feedback)', 'Interview_2 (Login)', 'Interview_2 (Feedback)', 'Status']
        excel_headers_2 = ['Admin (Login)', 'Status', 'Admin (Unlock Feedback)', 'Status', 'Interview_1 (Login)',
                           'Status',  'Interview_1 (Update Decision/Feedback)', 'Status', 'Interview_2 (Login)',
                           'Status', 'Interview_2 (Update Decision/Feedback)', 'Status']
        color_headers_2 = ['Admin (Login)', 'Admin (Unlock Feedback)', 'Interview_1 (Login)',
                           'Interview_1 (Update Decision/Feedback)', 'Interview_2 (Login)',
                           'Interview_2 (Update Decision/Feedback)', 'Status']

        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)
        self.xlw.excel_header_by_index(row=17, col=0, excel_headers_list=excel_headers_2,
                                       color_headers_list=color_headers_2)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='UNLOCK/UPDATE INTERVIEW FLOW')

    def event_app_report(self, event_coll):
        testdata_headers = ['Event Tab', 'Advance Search Action', 'Advance Name Field', 'Search Button',
                            'Event Card Click', 'Event validate', 'Event Actions', 'View Applicant Action',
                            'Applicant Advance Search', 'Applicant Name Enter', 'Search Button']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=event_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def change_status_report(self, status_coll):
        testdata_headers = ['Select Applicant', 'Change Applicant Status', 'Select Stage', 'Select Status',
                            'Select Interviewers', 'Move all Interviewers', 'Done', 'Comment', 'Change Button',
                            'Change Status Notifier', 'Change Status Notifier Dismiss', 'Applicant Get name',
                            'Candidate Status Validate', 'Window Close', 'Switch to Old Window']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=status_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)

    def interviewer1_login_report(self, int1_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate', 'Event Actions',
                            'Event Interviews Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def interviewer1_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Advance Search', 'Applicant Name search', 'Search Button', 'Select Applicant',
                            'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def interviewer1_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['Pending - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=8, i_column=6, o_column=7, path=self.__path)

    def interviewer2_login_report(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate', 'Event Actions',
                            'Event Interviews Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def interviewer2_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Advance Search', 'Applicant Name search', 'Search Button', 'Select Applicant',
                            'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def interviewer2_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['Pending - decision', 'Ratings', 'comments', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=8, i_column=10, o_column=11, path=self.__path)

    def admin_login_report(self, admin_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Event Tab', 'Advance Search Action',
                            'Advance Name Field', 'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=18, i_column=0, o_column=1, path=self.__path)

    def admin_unlock_report(self, admin_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Completed Bucket', 'Select Applicant',
                            'Unlock Feedback Action', 'Select Interviewers', 'Unlock Button', 'Unlock Comment',
                            'Confirm Button', 'Unlock Notifier', 'Unlock Notifier Dismiss', 'Close Unlock screen']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=admin_coll,
                                     row=18, i_column=2, o_column=3, path=self.__path)

    def interviewer1_login_report1(self, int1_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate', 'Event Actions',
                            'Event Interviews Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=18, i_column=4, o_column=5, path=self.__path)

    def interviewer1_feedback_action_report1(self, int1_action_coll):
        testdata_headers = ['Advance Search', 'Applicant Name search', 'Search Button', 'Select Applicant',
                            'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=19, i_column=6, o_column=7, path=self.__path)

    def bucket1_report(self, collection):
        testdata_headers = ['Completed Interviews']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=18, i_column=6, o_column=7, path=self.__path)

    def interviewer1_provide_feedback_report1(self, int1_pf_coll):
        testdata_headers = ['shortlist - Update decision', 'Ratings', 'comments', 'overall comment', 'Update Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=25, i_column=6, o_column=7, path=self.__path)

    def interviewer2_login_report1(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate', 'Event Actions',
                            'Event Interviews Action']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=18, i_column=8, o_column=9, path=self.__path)

    def interviewer2_feedback_action_report1(self, int1_action_coll):
        testdata_headers = ['Advance Search', 'Applicant Name search', 'Search Button', 'Select Applicant',
                            'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=19, i_column=10, o_column=11, path=self.__path)

    def bucket2_report(self, collection):
        testdata_headers = ['Completed Interviews']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=collection,
                                     row=18, i_column=10, o_column=11, path=self.__path)

    def interviewer2_provide_feedback_report1(self, int2_pf_coll):
        testdata_headers = ['shortlist - update decision', 'Ratings', 'comments', 'overall comment', 'Update Feedback',
                            'Feedback validation Agree', 'Review Feedback', 'Close Tab', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_pf_coll,
                                     row=25, i_column=10, o_column=11, path=self.__path)
