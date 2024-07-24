import urllib3
import json
import requests
from utilities import ReadConfigFile


class CancelInterview:
    def __init__(self):
        self.cancel_irs = ''

    def cancel_api_call(self, headers, ir):
        try:
            urllib3.disable_warnings()
            api = ReadConfigFile.ReadConfig.get_amsin_abacus_cancel()
            request_data = {
                "id": ir,
                "comment": "Cancel by Vinod through UI-Automation"
            }

            cancel_api = requests.post(api, headers=headers, data=json.dumps(request_data),
                                       verify=False)
            response = cancel_api.json()
            data = response.get('data')

            self.cancel_irs = response.get('data')
            print("Cancelled Interview Response and ID:: ", self.cancel_irs)
            return True
        except ValueError as access_error:
            print(access_error)
