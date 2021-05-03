from utilities import excelWrite
from Config import outputFile


class NewFeedbackOutputReport:
    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['New_Interview_output']
        test_cases = 82
        excel_headers_1 = ['Event (Applicants)', 'Status', 'Applicant (Status change)', 'Status', 'Interview_1 (Login)',
                           'Status', 'Event (search)', 'Status', 'Interview_1 (Feedback)', 'Status',
                           'Interview_2 (Login)', 'Status', 'Event (search)', 'Status', 'Interview_2 (Feedback)',
                           'Status']
        color_headers_1 = ['Status', 'Event (Applicants)', 'Applicant (Status change)', 'Interview_1 (Feedback)',
                           'Event (search)', 'Interview_1 (Login)', 'Interview_2 (Feedback)', 'Interview_2 (Login)']

        self.xlw = excelWrite.ExcelReportWrite(version=version, test_cases=test_cases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='NEW FEEDBACK INTERVIEW FLOW')

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
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_coll,
                                     row=2, i_column=4, o_column=5, path=self.__path)

    def interviewer1_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=6, o_column=7, path=self.__path)

    def interviewer1_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['Ratings', 'comments', 'shortlist - decision', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=2, i_column=8, o_column=9, path=self.__path)

    def interviewer2_login_report(self, int2_coll):
        testdata_headers = ['Account Name Click', 'Logout', 'Click Here Login', 'Login Name Field', 'Password Field',
                            'Next Button', 'Account Name Validate', 'Advance Search Action', 'Advance Name Field',
                            'Search Button', 'Event Card Click', 'Event validate']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int2_coll,
                                     row=2, i_column=10, o_column=11, path=self.__path)

    def interviewer2_feedback_action_report(self, int1_action_coll):
        testdata_headers = ['Event Actions', 'Event Interviews Action', 'Advance Search', 'Applicant Name search',
                            'Search Button', 'Select Applicant', 'Feedback Provide Action', 'Switch to new tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_action_coll,
                                     row=2, i_column=12, o_column=13, path=self.__path)

    def interviewer2_provide_feedback_report(self, int1_pf_coll):
        testdata_headers = ['Ratings', 'comments', 'shortlist - decision', 'overall comment', 'Submit Feedback',
                            'Feedback validation Agree', 'Switch to tab']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=int1_pf_coll,
                                     row=2, i_column=14, o_column=15, path=self.__path)
