import urllib3
import datetime
import json
import requests
from utilities import ReadConfigFile


class CommonLogin(object):

    def __init__(self):
        super(CommonLogin, self).__init__()
        self.lambda_headers = {"content-type": "application/json"}
        self.Non_lambda_headers = {"content-type": "application/json"}
        self.headers = {"content-type": "application/json"}
        self.api = ""
        self.get_token = ""

    def abacus_access_login(self, server, client_id, client_secret):
        # -------------------------------- CRPO LOGIN APPLICATION ------------------------------------------------------

        print("-------------------------------------------------")
        print("Run Started at :", str(datetime.datetime.now()))
        print("-------------------------------------------------")

        try:
            urllib3.disable_warnings()
            if server == 'amsin':
                self.api = ReadConfigFile.ReadConfig.get_amsin_abacus_access()
            elif server == 'ams':
                self.api = ReadConfigFile.ReadConfig.get_ams_abacus_access()

            request_data = {
                "client_id": client_id,
                "client_secret": client_secret
            }

            access_api = requests.post(self.api, headers=self.headers, data=json.dumps(request_data),
                                       verify=False)
            response = access_api.json()
            token = response.get('access_token')
            self.headers['Authorization'] = "bearer " + token
            print(self.headers)
            return True
        except ValueError as access_error:
            print(access_error)
