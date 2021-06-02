from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Login.crpo_candidate_login import CRPOCandidateLogin
from Scripts.HelpDesk.crpo_requirement_search import CrpoRequirementSearch
from Scripts.HelpDesk.crpo_help_desk_configuration import CrpoRequirementHelpDeskConfig
from Scripts.HelpDesk.candidate_raise_queries import CandidateQueryRaise
from Scripts.Output_scripts import HelpDeskReport


class CRPOHelpDesk:
    """
        Required class Objects are created
    """
    candidate_email = input("Enter Candidate Email:: ")
    candidate_password = input("Enter Candidate Password:: ")
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        login = CRPOLogin(driver=driver, index=index)
        candidate_login = CRPOCandidateLogin(driver=driver, index=index, version=version, server=server)
        req = CrpoRequirementSearch(driver=driver, index=index, version=version)
        help_desk_config = CrpoRequirementHelpDeskConfig(driver=driver, index=index, version=version)
        query = CandidateQueryRaise(driver=driver, index=index)

        HELPDESK_output = HelpDeskReport.HelpDeskOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)

    def crpo_candidate_login(self):
        try:
            self.candidate_login.candidate_login(self.candidate_email, self.candidate_password)

        except Exception as error:
            ui_logger.error(error)

    def crpo_help_desk_requirement_search(self):
        self.req.requirement_search()

    def default_help_desk_config(self):
        self.help_desk_config.default_level_config()

    def job_help_desk_config(self):
        self.help_desk_config.job_level_config()

    def event_help_desk_config(self):
        self.help_desk_config.event_level_config()

    def save_help_desk_configurations(self):
        self.help_desk_config.save_configurations()

    def candidate_login_query_1(self):
        self.query.candidate_query_1()

    def candidate_login_query_2(self):
        self.query.candidate_query_2()

    def candidate_login_query_3(self):
        self.query.candidate_query_3()


Object = CRPOHelpDesk()
Object.crpo_login()

if Object.login_success:
    Object.crpo_help_desk_requirement_search()
    Object.default_help_desk_config()
    Object.job_help_desk_config()
    Object.event_help_desk_config()
    Object.save_help_desk_configurations()
    Object.crpo_candidate_login()
    Object.candidate_login_query_1()
    Object.candidate_login_query_2()
    Object.candidate_login_query_3()
    Object.HELPDESK_output.overall_status()
    Object.environment.close()
