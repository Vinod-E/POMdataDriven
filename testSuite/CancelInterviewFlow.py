from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.CancelInterviewRequest.crpo_event_applicant_search import CrpoCancelRequestEvent
from Scripts.CancelInterviewRequest.crpo_change_applicant_status import CrpoEventApplicantSchedule
from Scripts.CancelInterviewRequest.crpo_int1_login import CrpoInt1Login
from Scripts.CancelInterviewRequest.crpo_int2_login import CrpoInt2Login
from Scripts.CancelInterviewRequest.crpo_int1_cancel_request import CrpoInt1CancelRequest
from Scripts.CancelInterviewRequest.crpo_admin_login import CrpoAdminLogin
from Scripts.CancelInterviewRequest.crpo_admin_accept_cancellation import CrpoAdminAccept
from Scripts.CancelInterviewRequest.crpo_int2_cancel_interview import CrpoInt2CancelRequest
from Scripts.Output_scripts import CancelInterviewReport


class CancelInterviewFlow:
    """
        Required class Objects are created
    """
    environment = ''
    login_success = ''
    """
    Environment setup instance and other required function instances
    """
    try:
        environment = Enviroment.EnvironmentSetup()
        driver = environment.driver
        index = environment.index
        server = environment.server
        version = environment.sprint_version
        date_time = environment.start_date_time

        login = CRPOLogin(driver=driver, index=index)
        event = CrpoCancelRequestEvent(driver=driver, index=index, version=version)
        schedule = CrpoEventApplicantSchedule(driver=driver, index=index, version=version)
        int1 = CrpoInt1Login(driver=driver, index=index, version=version)
        int1_request = CrpoInt1CancelRequest(driver=driver, index=index, version=version)
        admin = CrpoAdminLogin(driver=driver, index=index, version=version)
        admin_accept = CrpoAdminAccept(driver=driver, index=index)
        int2 = CrpoInt2Login(driver=driver, index=index, version=version)
        int2_cancel = CrpoInt2CancelRequest(driver=driver, index=index, version=version)

        CANCEL_OUTPUT = CancelInterviewReport.CancelInterviewOutputReport(version=version, server=server,
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

    def event_applicant_search(self):
        self.event.event_applicant_search()
        self.CANCEL_OUTPUT.event_app_report(self.event.event_search_collection)

    def event_applicant_change_status_schedule(self):
        self.schedule.event_change_applicant_status()
        self.CANCEL_OUTPUT.change_status_report(self.schedule.applicant_status_collection)

    def interview_one_login(self):
        self.int1.interviewer1_login()
        self.CANCEL_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interview_one_raise_request(self):
        self.int1_request.raise_request_to_cancel()
        self.CANCEL_OUTPUT.interviewer1_request_report(self.int1_request.int1_cancel_collection)

    def admin_login(self):
        self.admin.admin_login()
        self.CANCEL_OUTPUT.admin_login_report(self.admin.admin_collection)

    def admin_accept_request(self):
        self.admin_accept.admin_accept_cancellation()
        self.CANCEL_OUTPUT.admin_acceptance_report(self.admin_accept.admin_accept_collection)

    def admin_event_action(self):
        self.schedule.event_action_view_candidates()
        self.CANCEL_OUTPUT.event_action_report(self.schedule.event_action_collection)

    def event_applicant_change_status_schedule2(self):
        self.schedule.event_change_applicant_status()
        self.CANCEL_OUTPUT.change_status_report2(self.schedule.applicant_status_collection)

    def interview_two_login(self):
        self.int2.interviewer2_login()
        self.CANCEL_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interview_two_cancel_interview(self):
        self.int2_cancel.cancel_interview()
        self.CANCEL_OUTPUT.interviewer2_cancel_report(self.int2_cancel.int2_cancel_collection)


Object = CancelInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_applicant_search()
    Object.event_applicant_change_status_schedule()
    Object.interview_one_login()
    Object.interview_one_raise_request()
    Object.admin_login()
    Object.admin_accept_request()
    Object.admin_event_action()
    Object.event_applicant_change_status_schedule2()
    Object.interview_two_login()
    Object.interview_two_cancel_interview()
    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOWn =============>>
    """
    Object.CANCEL_OUTPUT.overall_status()
    Object.CANCEL_OUTPUT.html_report_generation()
    Object.environment.close()
