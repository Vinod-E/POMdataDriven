from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.UnlockUpdateFeedback.crpo_event_applicant_search import CrpoUnlockEvent
from Scripts.UnlockUpdateFeedback.crpo_change_applicant_status import EventApplicant
from Scripts.UnlockUpdateFeedback.crpo_unlock_update_int1_login import CrpoInt1Login
from Scripts.UnlockUpdateFeedback.crpo_unlock_update_int2_login import CrpoInt2Login
from Scripts.UnlockUpdateFeedback.crpo_unlock_update_feedback_int1 import CrpoInt1Feedback
from Scripts.UnlockUpdateFeedback.crpo_unlock_update_feedback_int2 import CrpoInt2Feedback
from Scripts.UnlockUpdateFeedback.crpo_admin_login import CrpoAdminLogin

from Scripts.Output_scripts import UnlockUpdateFeedbackReport


class UnlockUpdateFeedbackInterviewFlow:
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
        event = CrpoUnlockEvent(driver=driver, index=index, version=version)
        schedule = EventApplicant(driver=driver, index=index, version=version)
        int1 = CrpoInt1Login(driver=driver, index=index, version=version)
        int2 = CrpoInt2Login(driver=driver, index=index, version=version)
        int1_feed = CrpoInt1Feedback(driver=driver, index=index, version=version)
        int2_feed = CrpoInt2Feedback(driver=driver, index=index, version=version)
        unlock = CrpoAdminLogin(driver=driver, index=index, version=version)
        UNLOCK_OUTPUT = UnlockUpdateFeedbackReport.UnlockUpdateOutputReport(version=version, server=server,
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
        self.event.unlock_feed_event_applicant_search()
        self.UNLOCK_OUTPUT.event_app_report(self.event.event_search_collection)

    def event_applicant_change_status_schedule(self):
        self.schedule.event_change_applicant_status()
        self.UNLOCK_OUTPUT.change_status_report(self.schedule.applicant_status_collection)

    def interviewer_one_login(self):
        self.int1.interviewer1_login()
        self.UNLOCK_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interviewer_one_feedback(self):
        self.int1_feed.interview1_feedback()
        self.UNLOCK_OUTPUT.interviewer1_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_one_provide_feedback(self):
        self.int1_feed.int1_provide_feedback()
        self.UNLOCK_OUTPUT.interviewer1_provide_feedback_report(self.int1_feed.pf1_collection)

    def interviewer_two_login(self):
        self.int2.interviewer2_login()
        self.UNLOCK_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interviewer_two_feedback(self):
        self.int2_feed.interview2_feedback()
        self.UNLOCK_OUTPUT.interviewer2_feedback_action_report(self.int2_feed.int2_feedback_collection)

    def interviewer_two_provide_feedback(self):
        self.int2_feed.int2_provide_feedback()
        self.UNLOCK_OUTPUT.interviewer2_provide_feedback_report(self.int2_feed.pf2_collection)

    def admin_event_action(self):
        self.unlock.admin_login()
        self.UNLOCK_OUTPUT.admin_login_report(self.unlock.admin_collection)

    def admin_unlock_feedback(self):
        self.unlock.admin_unlock()
        self.UNLOCK_OUTPUT.admin_unlock_report(self.unlock.unlock_collection)

    def interviewer_one_login1(self):
        self.int1.interviewer1_login()
        self.UNLOCK_OUTPUT.interviewer1_login_report1(self.int1.int1_collection)

    def int1_completed_bucket(self):
        self.int1_feed.completed_bucket()
        self.UNLOCK_OUTPUT.bucket1_report(self.int1_feed.completed_bucket_collection)

    def interviewer_one_feedback1(self):
        self.int1_feed.interview1_feedback()
        self.UNLOCK_OUTPUT.interviewer1_feedback_action_report1(self.int1_feed.int1_feedback_collection)

    def interviewer_one_update_feedback_decision(self):
        self.int1_feed.int1_update_feedback_decision()
        self.UNLOCK_OUTPUT.interviewer1_provide_feedback_report1(self.int1_feed.update_f_d_collection)

    def interviewer_two_login1(self):
        self.int2.interviewer2_login()
        self.UNLOCK_OUTPUT.interviewer2_login_report1(self.int2.int2_collection)

    def int2_completed_bucket(self):
        self.int2_feed.completed_bucket()
        self.UNLOCK_OUTPUT.bucket2_report(self.int2_feed.completed_bucket_collection)

    def interviewer_two_feedback1(self):
        self.int2_feed.interview2_feedback()
        self.UNLOCK_OUTPUT.interviewer2_feedback_action_report1(self.int2_feed.int2_feedback_collection)

    def interviewer_two_update_feedback_decision(self):
        self.int2_feed.int2_update_feedback_decision()
        self.UNLOCK_OUTPUT.interviewer2_provide_feedback_report1(self.int2_feed.update_f_d_collection)


Object = UnlockUpdateFeedbackInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_applicant_search()
    Object.event_applicant_change_status_schedule()
    Object.interviewer_one_login()
    Object.interviewer_one_feedback()
    Object.interviewer_one_provide_feedback()
    Object.interviewer_two_login()
    Object.interviewer_two_feedback()
    Object.interviewer_two_provide_feedback()
    Object.admin_event_action()
    Object.admin_unlock_feedback()
    Object.interviewer_one_login1()
    Object.int1_completed_bucket()
    Object.interviewer_one_feedback1()
    Object.interviewer_one_update_feedback_decision()
    Object.interviewer_two_login1()
    Object.int2_completed_bucket()
    Object.interviewer_two_feedback1()
    Object.interviewer_two_update_feedback_decision()
    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.UNLOCK_OUTPUT.overall_status()
    Object.UNLOCK_OUTPUT.history_html_generator()
    Object.environment.close()
