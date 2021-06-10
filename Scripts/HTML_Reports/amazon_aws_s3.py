import json
import requests
import urllib3
from Config import inputFile
from utilities import ReadConfigFile, excelRead


class AWS:
    def __init__(self, save_file_name, path):
        urllib3.disable_warnings()
        self.__html_path = path
        self.__file_name = save_file_name
        self.get_token = ''

        """
         ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=0)
        xl = login_excel.excel_dict
        self.xl_login = xl['c_login_name'][0]
        self.xl_password = xl['c_password'][0]
        self.xl_tenant = xl['c_tenant'][0]

    def login_token(self):
        url = ReadConfigFile.ReadConfig.login_api()
        headers = {"content-type": "application/json", 'APP-NAME': "crpo", 'X-APPLMA': 'true'}
        request = {"LoginName": self.xl_login,
                   "Password": self.xl_password,
                   "TenantAlias": self.xl_tenant,
                   "UserName": self.xl_login}
        login_api = requests.post(url, headers=headers, data=json.dumps(request, default=str),
                                  verify=False)
        response = json.loads(login_api.content)
        self.get_token = response.get("Token")
        print(self.get_token)

    def file_handler(self):
        """
        ===================>> Login for Token <<======================
        """
        self.login_token()
        url = ReadConfigFile.ReadConfig.file_handler_api()
        headers = {
            'X-AUTH-TOKEN': self.get_token,
        }
        with open(self.__html_path, "rb") as a_file:
            file_context = a_file.read()
            file_dict = {'{}_.html'.format(self.__file_name): file_context}
        response = requests.post(url, headers=headers, files=file_dict)
        print(response.text)
