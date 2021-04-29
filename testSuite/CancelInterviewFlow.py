from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import NewFeedbackInterviewReport
from Scripts.CancelInterviewRequest.crpo_event_applicant_search import CrpoCancelRequestEvent
from Scripts.CancelInterviewRequest.crpo_change_applicant_status import CrpoEventApplicantSchedule
from Scripts.CancelInterviewRequest.crpo_int1_login import CrpoInt1Login
from Scripts.CancelInterviewRequest.crpo_int1_cancel_request import CrpoInt1CancelRequest
from Scripts.CancelInterviewRequest.crpo_admin_login import CrpoAdminLogin


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

        CANCEL_OUTPUT = NewFeedbackInterviewReport.NewFeedbackOutputReport(version=version, server=server,
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
        self.event.new_feed_event_applicant_search()

    def event_applicant_change_status_schedule(self):
        self.schedule.event_change_applicant_status()

    def interview_one_login(self):
        self.int1.interviewer1_login()

    def interview_one_raise_request(self):
        self.int1_request.raise_request_to_cancel()

    def admin_login(self):
        self.admin.admin_login()

    def admin_accept_request(self):
        self.admin.admin_accept_cancellation()


Object = CancelInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_applicant_search()
    Object.event_applicant_change_status_schedule()
    Object.interview_one_login()
    Object.interview_one_raise_request()
    Object.admin_login()
    Object.admin_accept_request()
    Object.CANCEL_OUTPUT.overall_status()
    Object.environment.close()
