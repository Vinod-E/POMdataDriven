import os.path
import pandas as pd
from openpyxl import load_workbook


class HistoryOutput:
    def __init__(self, history_data_path):
        self.HISTORY_DATA_OUTPUT = history_data_path

    def create_pandas_excel(self, sheet_name, date, time, sprint, total, success, fail, time_taken):

        if sheet_name == 'amsin':
            sheet_name = 'AMSIN'
        elif sheet_name == 'beta':
            sheet_name = 'BETA'
        elif sheet_name == 'ams':
            sheet_name = 'AMS'
        elif sheet_name == 'india':
            sheet_name = 'INDIA'
        elif sheet_name == 'amsinc':
            sheet_name = 'AMSIN'
        elif sheet_name == 'amsc':
            sheet_name = 'AMS'
        elif sheet_name == 'betac':
            sheet_name = 'AMS'
        elif sheet_name == 'amsine':
            sheet_name = 'AMSIN'
        elif sheet_name == 'amse':
            sheet_name = 'AMS'
        elif sheet_name == 'betae':
            sheet_name = 'AMS'
        elif sheet_name == 'amsino':
            sheet_name = 'AMSIN'
        elif sheet_name == 'amso':
            sheet_name = 'AMS'
        elif sheet_name == 'betao':
            sheet_name = 'AMS'
        elif sheet_name == 'amsinr':
            sheet_name = 'AMSIN'
        elif sheet_name == 'amsr':
            sheet_name = 'AMS'
        elif sheet_name == 'betar':
            sheet_name = 'AMS'
        # ----------------------- Headers initialization ----------------------------
        h1 = 'Run Date'
        h2 = 'Run Time'
        h3 = 'Sprint Name'
        h4 = 'Total Cases'
        h5 = 'Pass Cases'
        h6 = 'Fail Cases'
        h7 = 'Time Taken'
        headers = [h1, h2, h3, h4, h5, h6, h7]

        # ------------------ Validation for File exists  ------------------------------
        local_path = os.path.exists(self.HISTORY_DATA_OUTPUT)
        if local_path:
            print('**----->> File exists in your machine')
        else:
            vinod = pd.ExcelWriter(self.HISTORY_DATA_OUTPUT, engine='xlsxwriter')
            sheetsList = ['AMSIN', 'BETA', 'AMS', 'INDIA']

            for new_sheet in sheetsList:
                df_dynamic = pd.DataFrame(columns=headers)
                df_dynamic.to_excel(vinod, sheet_name=new_sheet, startrow=1, header=False, index=False)
                workbook = vinod.book
                header_format = workbook.add_format({'bold': True, 'valign': 'top', 'fg_color': '#00FA9A',
                                                     'font_size': 10.5})
                worksheet = vinod.sheets[new_sheet]
                for col_num, value in enumerate(df_dynamic.columns.values):
                    worksheet.write(0, col_num, value, header_format)
                    col_num += 1
            vinod.save()
            print('**----->> File has been created successfully')

        # ------------- Appending the values into their columns --------------------
        df = pd.DataFrame(columns=headers)
        df.loc[1, h1] = date
        df.loc[1, h2] = time
        df.loc[1, h3] = sprint
        df.loc[1, h4] = total
        df.loc[1, h5] = success
        df.loc[1, h6] = fail
        df.loc[1, h7] = time_taken

        """ ======== Load Excel file before open ==========="""
        book = load_workbook(self.HISTORY_DATA_OUTPUT)
        writer = pd.ExcelWriter(self.HISTORY_DATA_OUTPUT, engine='openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        writer.save()

        """ ======== Open and Read Excel to get the sheet data ==========="""
        reader = pd.read_excel(self.HISTORY_DATA_OUTPUT, engine='openpyxl', sheet_name=sheet_name)
        length = len(reader)

        """ ======== In case of excel sheet having no rows it returns None==========="""
        if length is None:
            length = 0
        df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=length + 1)
        writer.save()
        writer.close()
        print('**----->> Excel History Data - Saved')
