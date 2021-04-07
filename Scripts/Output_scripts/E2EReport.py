from utilities import excelWrite
from Config import outputFile


class E2EOutputReport:
    """Number of Test cases """
    TestCases = 150

    def __init__(self, version, server, start_date_time):
        self.version = version
        self.server = server
        self.start_date_time = start_date_time
        self.__path = outputFile.OUTPUT_PATH['E2E_output']

        excel_headers_1 = ['Create Job', 'Status', 'Job Config']
        color_headers_1 = ['Status', 'Create Job', 'Job Config']

        self.xlw = excelWrite.ExcelReportWrite(version=self.version, test_cases=self.TestCases)
        self.xlw.excel_header_by_index(row=1, col=0, excel_headers_list=excel_headers_1,
                                       color_headers_list=color_headers_1)

    def overall_status(self):
        self.xlw.status(start_date_time=self.start_date_time, version=self.version, server=self.server,
                        path=self.__path, excel_save_name='E2E REGRESSION FLOW')

    def job_creation_report(self, job_creation_coll):
        testdata_headers = ['Job Tab', 'Job Create Button', 'Job Name', 'Job Attachment', 'Job Notifier', 'Description',
                            'Location Field', 'Hiring Manager Field', 'Business Unit Field', 'Opening Field',
                            'Male Diversity Field', 'Female Diversity Field', 'Job created Button',
                            'Job created Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_creation_coll,
                                     row=2, i_column=0, o_column=1, path=self.__path)

    def job_getby_report(self, job_getby_coll):
        testdata_headers = ['Tab Validation', 'Job Name Validation']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_getby_coll,
                                     row=16, i_column=0, o_column=1, path=self.__path)

    def job_sp_report(self, job_sp_coll):
        testdata_headers = ['Job Actions', 'Tag Selection Process Action', 'Select Selection Process', 'Save',
                            'Tagged Notifier']
        self.xlw.input_output_report(testdata_headers=testdata_headers, collection=job_sp_coll,
                                     row=2, i_column=2, o_column=3, path=self.__path)
