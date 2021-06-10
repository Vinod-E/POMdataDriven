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

    def history_data_save_read(self, environment, date, time, version, total_cases, pass_cases, failure_cases,
                               time_taken_min):
        self.history.create_pandas_excel(environment, date, time, version, int(total_cases), pass_cases,
                                         failure_cases, time_taken_min)
        self.history_dict.read_excel_data_dict()
        self.history_dict.amsin_dict_data(version)
        self.history_dict.beta_dict_data(version)
        self.history_dict.ams_dict_data(version)
        self.history_dict.india_dict_data(version)

    def html_report_generation(self, environment, version, date_time, use_case_name, result, total_cases,
                               pass_cases, failure_cases, success_percentage, execution_time, time, date):
        """
         =============>> Calling above function for data pulling from different dicts <<==============
        """
        self.history_data_save_read(environment, date, time, version, total_cases, pass_cases, failure_cases,
                                    execution_time)
        """=========================================================================================="""
        if failure_cases != 0:
            self.fail_color = 'summaryFail'
        else:
            self.fail_color = 'summaryPass'

        self.html_generator.html_css(environment, version, date_time, use_case_name, result, total_cases,
                                     pass_cases, failure_cases, self.fail_color,
                                     self.history_dict.graph_sprint_names, self.history_dict.amsin_pass_cases,
                                     self.history_dict.beta_pass_cases, self.history_dict.ams_pass_cases,
                                     self.history_dict.india_pass_cases, self.history_dict.amsin_execute_time,
                                     self.history_dict.beta_execute_time, self.history_dict.ams_execute_time,
                                     self.history_dict.india_execute_time, success_percentage, execution_time)
