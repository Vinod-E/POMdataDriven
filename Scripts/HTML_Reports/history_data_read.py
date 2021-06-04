import pandas as pd


class HistoryDataRead:

    def __init__(self, path):
        self.path = path
        self.history_data_AMSIN_dict = []
        self.history_data_BETA_dict = []
        self.history_data_AMS_dict = []
        self.history_data_INDIA_dict = []

    def excel_data_dict(self):

        """ ======== Open and Read Excel to get the sheet data ==========="""
        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='AMSIN')
        self.history_data_AMSIN_dict = reader.to_json(orient='records')
        print('Excel Sheet to JSON:\n', self.history_data_AMSIN_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='BETA')
        self.history_data_BETA_dict = reader.to_json(orient='records')
        print('Excel Sheet to JSON:\n', self.history_data_BETA_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='AMS')
        self.history_data_AMS_dict = reader.to_json(orient='records')
        print('Excel Sheet to JSON:\n', self.history_data_AMS_dict)

        reader = pd.read_excel(self.path, engine='openpyxl', sheet_name='INDIA')
        self.history_data_INDIA_dict = reader.to_json(orient='records')
        print('Excel Sheet to JSON:\n', self.history_data_INDIA_dict)
