import re
import json
import pandas as pd


class HistoryDataRead:

    def __init__(self, path):
        self.path = path
        self.history_data_AMSIN_dict = []
        self.history_data_BETA_dict = []
        self.history_data_AMS_dict = []
        self.history_data_INDIA_dict = []

        self.version_number = ''

    def excel_data_dict(self):
        print('**----->> History Data reading from History Excel')

        """ ======== Open and Read Excel to get the sheet data ==========="""
        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='AMSIN')
        self.history_data_AMSIN_dict = json.loads(reader.to_json(orient='records'))
        print('Excel Sheet to JSON:\n', self.history_data_AMSIN_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='BETA')
        self.history_data_BETA_dict = json.loads(reader.to_json(orient='records'))
        print('Excel Sheet to JSON:\n', self.history_data_BETA_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='AMS')
        self.history_data_AMS_dict = json.loads(reader.to_json(orient='records'))
        print('Excel Sheet to JSON:\n', self.history_data_AMS_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='INDIA')
        self.history_data_INDIA_dict = json.loads(reader.to_json(orient='records'))
        print('Excel Sheet to JSON:\n', self.history_data_INDIA_dict)

    def last_five_history_data(self, current_sprint_number):
        # self.version_number = re.search(r'\d+', current_sprint_number).group()
        # print(self.version_number)

        pass_cases = []
        sprint_name = []
        time_taken = []

        all_sprint_names = [x['Sprint Name'] for x in self.history_data_AMSIN_dict]

        if len(self.history_data_AMSIN_dict) > 5:
            if current_sprint_number in all_sprint_names:
                index = all_sprint_names.index(current_sprint_number)
                last_5_data = self.history_data_AMSIN_dict[index - 5:index]
                print('amsin_if :: ', last_5_data)
                for k in last_5_data:
                    pass_cases.append(k['Pass Cases'])
                    sprint_name.append(k['Sprint Name'])
                    time_taken.append(k['Time Taken'])
            else:
                last_5_data = self.history_data_AMSIN_dict[-5:]
                print('amsin_else :: ', last_5_data)
                for k in last_5_data:
                    pass_cases.append(k['Pass Cases'])
                    sprint_name.append(k['Sprint Name'])
                    time_taken.append(k['Time Taken'])
        else:
            print('***----------->>> History Data excel should have more than 5 rows')
