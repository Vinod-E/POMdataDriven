from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.ManageInterviewers.crpo_event_search import CRPOEventApplicant
from Scripts.ManageInterviewers.criteria_configuration import CRPOCriteriaConfig
from Scripts.ManageInterviewers.crpo_int1_login import CrpoInt1Login
from Scripts.ManageInterviewers.crpo_int2_login import CrpoInt2Login
from Scripts.ManageInterviewers.nomination_acceptance import CRPONominations
from Scripts.ManageInterviewers.recruiter_login import CrpoRecruiterLogin
from Scripts.ManageInterviewers.recruiter_approval import CRPORecruiterApproval
from Scripts.Output_scripts import ManageInterviewersReport


class CRPOManageInterviewers:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''

    try:
        environment = Enviroment.EnvironmentSetup()
        environment.crpo_app()
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        login = CRPOLogin(driver=driver, index=index)
        event = CRPOEventApplicant(driver=driver, index=index, version=version)
        criteria = CRPOCriteriaConfig(driver=driver, index=index)
        int1 = CrpoInt1Login(driver=driver, index=index)
        int2 = CrpoInt2Login(driver=driver, index=index)
        nom = CRPONominations(driver=driver, index=index, version=version)
        recruiter = CrpoRecruiterLogin(driver=driver, index=index)
        approval = CRPORecruiterApproval(driver=driver, index=index)

        MANAGE_OUTPUT = ManageInterviewersReport.ManageInterviewersOutputReport(version=version,
                                                                                server=server,
                                                                                start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)

    def event_name_search(self):
        self.event.event_applicant_search()
        self.MANAGE_OUTPUT.event_search_report(self.event.event_collection)

    def criteria_configuration(self):
        self.criteria.criteria_config_skill1()
        self.MANAGE_OUTPUT.skill1_search_report(self.criteria.skill1_criteria_collection)

        self.criteria.criteria_config_skill2()
        self.MANAGE_OUTPUT.skill2_search_report(self.criteria.skill2_criteria_collection)

        self.criteria.send_nomination_mail()
        self.MANAGE_OUTPUT.send_mail_report(self.criteria.send_criteria_collection)

    def interviewer_one_login(self):
        self.int1.interviewer1_login()
        self.MANAGE_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interviewer_one_nom_confirm(self):
        self.nom.nomination_confirmation()
        self.MANAGE_OUTPUT.interviewer1_confirm_report(self.nom.int_acceptance_collection)

    def interviewer_two_login(self):
        self.int2.interviewer2_login()
        self.MANAGE_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interviewer_two_nom_confirm(self):
        self.nom.nomination_confirmation()
        self.MANAGE_OUTPUT.interviewer2_confirm_report(self.nom.int_acceptance_collection)

    def recruiter_login(self):
        self.recruiter.recruiter_login()
        self.MANAGE_OUTPUT.recruiter_login_report(self.recruiter.rec_collection)

    def recruiter_approval(self):
        self.event.event_applicant_search()
        self.MANAGE_OUTPUT.event_report(self.event.event_collection)

        self.approval.recruiter_approval_skill()
        self.MANAGE_OUTPUT.approval_report(self.approval.recruiter_acceptance_collection)

    def interviewers_tag_by_sync(self):
        self.approval.sync_interviewers()
        self.MANAGE_OUTPUT.sync_report(self.approval.sync_collection)


Object = CRPOManageInterviewers()
Object.crpo_login()

if Object.login_success:
    Object.event_name_search()
    Object.criteria_configuration()
    Object.interviewer_one_login()
    Object.interviewer_one_nom_confirm()
    Object.interviewer_two_login()
    Object.interviewer_two_nom_confirm()
    Object.recruiter_login()
    Object.recruiter_approval()
    Object.interviewers_tag_by_sync()
    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.MANAGE_OUTPUT.overall_status()
    Object.MANAGE_OUTPUT.history_html_generator()
    Object.environment.close()
