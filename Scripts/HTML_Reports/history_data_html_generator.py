from Scripts.HTML_Reports.history_data_read import HistoryDataRead
from Scripts.HTML_Reports.html_css_script import HTMLReport
from utilities.HistoryexcelWriter import HistoryOutput


class HistoryDataHTMLGenerator:
    fail_color = ''

    def __init__(self, history_save_read_path, html_report_generator_path):
        """ <<<================== History Report Generator ==============================>>> """
        self.__history_path = history_save_read_path
        self.history = HistoryOutput(self.__history_path)

        """ ========================>>> Read History Excel Data <<<========================= """
        self.history_dict = HistoryDataRead(self.__history_path)

        """ <<<================== HTML Report Generator =================================>>> """
        self.__html_path = html_report_generator_path
        self.html_generator = HTMLReport(self.__html_path)

    def history_data_save_read(self, server, date, time, version, total_cases, pass_cases, failure_cases,
                               time_taken_min):
        self.history.create_pandas_excel(server, date, time, version, int(total_cases), pass_cases,
                                         failure_cases, time_taken_min)
        self.history_dict.excel_data_dict()
        self.history_dict.last_five_history_data(version)

    def html_report_generation(self, server, version, date, use_case_name, result, total_cases,
                               pass_cases, failure_cases):
        if failure_cases != 0:
            self.fail_color = 'summaryFail'
        else:
            self.fail_color = 'summaryPass'

        self.html_generator.html_css(server, version, date, use_case_name, result, total_cases,
                                     pass_cases, failure_cases, self.fail_color)
