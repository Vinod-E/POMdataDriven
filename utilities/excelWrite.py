import xlwt
import datetime
from datetime import date
from utilities import styles
from Listeners.logger_settings import ui_logger


class ExcelReportWrite(styles.FontColor):
    def __init__(self, version, test_cases):
        super(ExcelReportWrite, self).__init__()

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, test_cases)))
        self.Actual_success_cases = []
        self.total_cases = str(len(self.Expected_success_cases))
        self.pass_cases = ''
        self.failure_cases = ''
        self.result = ''
        self.minutes = ''
        self.percentage = ''

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_{}'.format(version))

    def excel_header_by_index(self, row, col, excel_headers_list, color_headers_list):
        column = col
        excelheaders = excel_headers_list
        for headers in excelheaders:
            if headers in color_headers_list:
                self.ws.write(row, column, headers, self.style0)
            else:
                self.ws.write(row, column, headers, self.style1)
            column += 1

    def __input_data_verification(self, row, column, input_key):
        self.ws.write(row, column, input_key, self.style8)

    def __common_result_pass(self, row, column, result_key, path):
        try:
            if result_key is None:
                self.ws.write(row, column, 'Fail', self.style3)
            else:
                result_key = 'Pass'
                self.Actual_success_cases.append(result_key)
                self.ws.write(row, column, 'Pass', self.style7)

            self.wb_Result.save(path)
        except Exception as error:
            ui_logger.error(error)

    def input_output_report(self, testdata_headers, collection, row, i_column, o_column, path):
        try:
            row = row
            testdata_headers = testdata_headers
            print(collection)
            for loop in range(0, len(collection)):
                self.__input_data_verification(row=row, column=i_column, input_key=testdata_headers[loop])
                self.__common_result_pass(row=row, column=o_column, result_key=collection[loop], path=path)
                row += 1
        except Exception as error:
            ui_logger.error(error)

    def status(self, path, excel_save_name, start_date_time, version, server):
        try:
            self.failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            self.pass_cases = len(self.Actual_success_cases)
            print('Expected Cases::', len(self.Expected_success_cases))
            print('Actual Cases::', len(self.Actual_success_cases))
            self.percentage = len(self.Actual_success_cases) * 100 / len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - start_date_time
            self.minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, excel_save_name, self.style4)
            if self.Expected_success_cases == self.Actual_success_cases:
                self.ws.write(0, 1, 'Pass', self.style5)
                self.result = 'Pass'
            else:
                self.ws.write(0, 1, 'Fail', self.style6)
                self.result = 'Fail'

            self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
            self.ws.write(0, 3, 'Sprint_{}'.format(version), self.style5)
            self.ws.write(0, 4, 'SPRINT DATE', self.style4)
            self.ws.write(0, 5, self.date_now, self.style5)
            self.ws.write(0, 6, 'SERVER', self.style4)
            self.ws.write(0, 7, server, self.style5)
            self.ws.write(0, 8, 'Success Cases', self.style4)
            self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
            self.ws.write(0, 10, 'Failure Cases', self.style4)
            if self.failure_cases == 0:
                self.ws.write(0, 11, self.failure_cases, self.style5)
            else:
                self.ws.write(0, 11, self.failure_cases, self.style6)
            self.ws.write(0, 12, 'Success %', self.style4)
            self.ws.write(0, 13, self.percentage, self.style5)
            self.ws.write(0, 14, 'Time Taken (min)', self.style4)
            self.ws.write(0, 15, self.minutes, self.style5)
            self.wb_Result.save(path)

        except Exception as error:
            ui_logger.error(error)
