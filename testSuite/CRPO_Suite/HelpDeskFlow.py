from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.HelpDesk.candidate_login import CrpoCandidateLogin
from Scripts.HelpDesk.crpo_requirement_search import CrpoRequirementSearch
from Scripts.HelpDesk.crpo_help_desk_configuration import CrpoRequirementHelpDeskConfig
from Scripts.HelpDesk.candidate_raise_queries import CandidateQueryRaise
from Scripts.HelpDesk.embrace_login import CrpoEmbraceLogin
from Scripts.HelpDesk.Query_reply import CandidateQueryReply
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
        candidate_login = CrpoCandidateLogin(driver=driver, index=index, version=version, server=server)
        embrace_login = CrpoEmbraceLogin(driver=driver, index=index, server=server)
        req = CrpoRequirementSearch(driver=driver, index=index, version=version)
        help_desk_config = CrpoRequirementHelpDeskConfig(driver=driver, index=index, version=version)
        query = CandidateQueryRaise(driver=driver, index=index)
        reply = CandidateQueryReply(driver=driver, index=index, version=version)

        HELPDESK_OUTPUT = HelpDeskReport.HelpDeskOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)

    def crpo_help_desk_requirement_search(self):
        self.req.requirement_search()
        self.HELPDESK_OUTPUT.req_config_report(self.req.help_desk_collection)

    def default_help_desk_config(self):
        self.help_desk_config.default_level_config()
        self.HELPDESK_OUTPUT.default_query_report(self.help_desk_config.default_collection)

    def job_help_desk_config(self):
        self.help_desk_config.job_level_config()
        self.HELPDESK_OUTPUT.job_query_report(self.help_desk_config.job_level_collection)

    def event_help_desk_config(self):
        self.help_desk_config.event_level_config()
        self.HELPDESK_OUTPUT.event_query_report(self.help_desk_config.event_level_collection)

    def save_help_desk_configurations(self):
        self.help_desk_config.save_configurations()
        self.HELPDESK_OUTPUT.save_query_report(self.help_desk_config.save_config_collection)

    def embrace_candidate_login(self):
        self.candidate_login.candidate_login(self.candidate_email, self.candidate_password)
        self.HELPDESK_OUTPUT.candidate_login_report(self.candidate_login.login_collection)

    def candidate_login_query_1(self):
        self.query.candidate_query_1()
        self.HELPDESK_OUTPUT.query_1_report(self.query.query_1_collection)

    def candidate_login_query_2(self):
        self.query.candidate_query_2()
        self.HELPDESK_OUTPUT.query_2_report(self.query.query_2_collection)

    def candidate_login_query_3(self):
        self.query.candidate_query_3()
        self.HELPDESK_OUTPUT.query_3_report(self.query.query_3_collection)

    def staffing_user_login_1(self):
        self.embrace_login.embrace_user_1_login()
        self.HELPDESK_OUTPUT.user_1_login_report(self.embrace_login.login_1_collection)

        self.reply.user_reply_1()
        self.HELPDESK_OUTPUT.reply_1_query_report(self.reply.reply_1_collection)

    def staffing_user_login_2(self):
        self.embrace_login.embrace_user_2_login()
        self.HELPDESK_OUTPUT.user_2_login_report(self.embrace_login.login_2_collection)

        self.reply.user_reply_2()
        self.HELPDESK_OUTPUT.reply_2_query_report(self.reply.reply_2_collection)

    def staffing_user_login_3(self):
        self.embrace_login.embrace_user_3_login()
        self.HELPDESK_OUTPUT.user_3_login_report(self.embrace_login.login_3_collection)

        self.reply.user_reply_3()
        self.HELPDESK_OUTPUT.reply_3_query_report(self.reply.reply_3_collection)


Object = CRPOHelpDesk()
Object.crpo_login()

if Object.login_success:
    Object.crpo_help_desk_requirement_search()
    Object.default_help_desk_config()
    Object.job_help_desk_config()
    Object.event_help_desk_config()
    Object.save_help_desk_configurations()
    Object.embrace_candidate_login()
    Object.candidate_login_query_1()
    Object.candidate_login_query_2()
    Object.candidate_login_query_3()
    Object.staffing_user_login_1()
    Object.staffing_user_login_2()
    Object.staffing_user_login_3()
    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.HELPDESK_OUTPUT.overall_status()
    Object.HELPDESK_OUTPUT.history_html_generator()
    Object.environment.close()
