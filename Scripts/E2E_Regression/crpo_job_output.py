import datetime
import xlwt
from datetime import date
from Listeners.logger_settings import ui_logger
from utilities import styles
from Config import Enviroment, outputFile


class JobOutputReport(styles.FontColor):

    def __init__(self):
        super(JobOutputReport, self).__init__()

        self.__e = Enviroment.EnvironmentSetup()

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 88)))
        self.Actual_success_cases = []

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.__e.sprint_version))

        index = 0
        excelheaders = ['Candidate_login', 'Status']
        for headers in excelheaders:
            if headers in ['Candidate_login', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def __common_result_pass(self, row, result_key, column):
        try:
            if result_key == 'Pass':
                self.Actual_success_cases.append(result_key)
                self.ws.write(row, column, 'Pass', self.style7)
            else:
                self.ws.write(row, column, 'Fail', self.style3)
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100 / len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.__e.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'MASS INTERVIEW FLOW', self.style4)
            if self.Expected_success_cases == self.Actual_success_cases:
                self.ws.write(0, 1, 'Pass', self.style5)
            else:
                self.ws.write(0, 1, 'Fail', self.style6)

            self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
            self.ws.write(0, 3, 'Sprint_{}'.format(self.__e.sprint_version), self.style5)
            self.ws.write(0, 4, 'SPRINT DATE', self.style4)
            self.ws.write(0, 5, self.date_now, self.style5)
            self.ws.write(0, 6, 'SERVER', self.style4)
            self.ws.write(0, 7, self.__e.server, self.style5)
            self.ws.write(0, 8, 'Success Cases', self.style4)
            self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
            self.ws.write(0, 10, 'Failure Cases', self.style4)
            if failure_cases == 0:
                self.ws.write(0, 11, failure_cases, self.style5)
            else:
                self.ws.write(0, 11, failure_cases, self.style6)
            self.ws.write(0, 12, 'Success %', self.style4)
            self.ws.write(0, 13, percentage, self.style5)
            self.ws.write(0, 14, 'Time Taken (min)', self.style4)
            self.ws.write(0, 15, minutes, self.style5)
            self.wb_Result.save(outputFile.OUTPUT_PATH['E2E_output'])

        except Exception as error:
            ui_logger.error(error)
