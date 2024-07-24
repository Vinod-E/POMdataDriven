from Listeners.logger_settings import ui_logger
from Scripts.Output_scripts import SSOReport
from Scripts.SSO import Generate_SAML_links
import datetime


class CandidateSSO:
    """
        Required class Objects are created
    """
    try:
        start_date_time = datetime.datetime.now()
        server = input('Please Enter testing Environment:: ')
        sprint_version = input('Please Enter Sprint version:: ')

        candidate_link = Generate_SAML_links.SAMLLinks(server=server)

        sso_output = SSOReport.SSOCandidateReport(version=sprint_version,
                                                  server=server, start_date_time=start_date_time)

    except Exception as error:
        ui_logger.error(error)
        candidate_link.driver.close()

    def login_api_call(self):
        self.candidate_link.access_token()
        self.sso_output.login_api_call_report(self.candidate_link.login_collection)

    def schedule_api_call(self):
        self.candidate_link.abacus_interviewer_schedule()
        self.sso_output.schedule_api_call_report(self.candidate_link.schedule_collection)

    def saml_login_candidate(self):
        self.candidate_link.candidate_video_link()

    def cancel_api_call(self):
        self.candidate_link.abacus_cancel_interview()
        self.sso_output.cancel_api_call_report(self.candidate_link.cancel_collection)


Object = CandidateSSO()
Object.login_api_call()
Object.schedule_api_call()
Object.saml_login_candidate()
Object.cancel_api_call()

"""
<<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
"""
Object.sso_output.overall_status()
Object.sso_output.history_html_generator()
Object.candidate_link.driver.close()
