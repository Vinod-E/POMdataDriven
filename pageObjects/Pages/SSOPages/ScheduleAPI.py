import urllib3
import json
import requests
from utilities import ReadConfigFile


class ScheduleInterview:

    def __init__(self):
        print("------------------- SCHEDULE API CALL -----------------")
        self.IR = ''
        self.candidate_link = ''
        self.interview_link = ''

    def schedule_api_call(self, headers, xl_abacus_id, xl_stage, xl_time,
                          xl_int_first_name, xl_int_middle_name, xl_int_last_name,
                          xl_int_email):
        try:
            urllib3.disable_warnings()
            api = ReadConfigFile.ReadConfig.get_amsin_abacus_schedule()
            request_data = {
                "abacusCandidateId": xl_abacus_id,
                "isSaml": True,
                "isCandidateSaml": True,
                "interviewName": xl_stage,
                "interviewTime": xl_time,
                "interviewerDetails": [
                    {
                        "firstName": xl_int_first_name,
                        "middleName": xl_int_middle_name,
                        "lastName": xl_int_last_name,
                        "email": xl_int_email
                    }
                ],
                "physicalInterviewDetails": {
                    "location": "Bangalore"
                }
            }

            schedule_api = requests.post(api, headers=headers, data=json.dumps(request_data),
                                         verify=False)
            response = schedule_api.json()
            data = response.get('data')

            self.IR = data.get('interviewId')
            self.candidate_link = data.get('candidateInterviewLink')
            for i in data.get('interviewerLinks'):
                self.interview_link = i.get('interviewLink')

            print("Scheduled IR is:: ", self.IR)
            print("Candidate Video Link is:: ", self.candidate_link)
            print("Interviewer Video Link is:: ", self.interview_link)
            return True
        except ValueError as access_error:
            print(access_error)
