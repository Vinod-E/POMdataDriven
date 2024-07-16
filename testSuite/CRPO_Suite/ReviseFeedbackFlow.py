from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Output_scripts import ReviseFeedbackReport
from Scripts.ReviseFeedback.crpo_login import AdminLogin
from Scripts.ReviseFeedback.crpo_event import CRPOEventSearch
from Scripts.ReviseFeedback.crpo_event_applicant import CRPOEventApplicant
from Scripts.ReviseFeedback.Provide_Feedback import CrpoInterviewerFeedback


class ReviseFeedback:
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

        admin = AdminLogin(driver=driver, index=index)
        event = CRPOEventSearch(driver=driver, index=index)
        applicant = CRPOEventApplicant(driver=driver, index=index)
        feedback = CrpoInterviewerFeedback(driver=driver, index=index)

        rf_output = ReviseFeedbackReport.ReviseFeedbackReport(version=version,
                                                              server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_admin_login(self):
        try:
            self.admin.admin_login()
            self.login_success = True
            self.rf_output.admin_login_report(self.admin.admin_login_collection)
        except Exception as error:
            ui_logger.error(error)

    def crpo_event_search(self):
        self.event.crpo_search_event()
        self.rf_output.event_search_report(self.event.event_search_collection)

    def crpo_event_applicant_search(self):
        self.event.crpo_applicant_search()
        self.rf_output.applicant_search_report(self.event.event_applicant_collection)

    def crpo_schedule_interview(self):
        self.applicant.crpo_change_applicant_status()
        self.rf_output.applicant_status_change_report(self.applicant.change_applicant_collection)

    def crpo_candidate_status_verification(self):
        self.applicant.crpo_candidate_verification()
        self.rf_output.candidate_status_verification_report(self.applicant.candidate_verification_collection)

    def interview_login(self):
        self.admin.interviewer_login()
        self.rf_output.interviewer_report(self.admin.interviewer_collection)

    def crpo_int_event_search(self):
        self.event.crpo_search_event()
        self.rf_output.int_event_search_report(self.event.event_search_collection)

    def crpo_int_event_interviews(self):
        self.event.crpo_event_interviews()
        self.rf_output.int_event_interview_report(self.event.event_interview_collection)

    def interviewer_provide_feedback(self):
        self.feedback.interviewer_provide_feedback()
        self.rf_output.int_provide_feedback_report(self.feedback.int_collection)

    def crpo_admin_re_login(self):
        self.admin.admin_re_login()
        self.rf_output.crpo_admin_re_login_report(self.admin.re_login_collection)

    def crpo_event_search_re_login(self):
        self.event.crpo_search_event()
        self.rf_output.re_login_event_search_report(self.event.event_search_collection)

    def crpo_event_applicant_search_re_login(self):
        self.event.crpo_applicant_search()
        self.rf_output.re_login_applicant_search_report(self.event.event_applicant_collection)

    def crpo_revise_feedback_enable(self):
        self.applicant.crpo_revise_feedback()
        self.rf_output.revise_feedback_report(self.applicant.revise_feedback_collection)

    def crpo_candidate_revise_status_verification(self):
        self.applicant.crpo_candidate_revise_verification()
        self.rf_output.candidate_revise_status_verification_report(
            self.applicant.candidate_revise_verification_collection)

    def interview_login_revise(self):
        self.admin.interviewer_login()
        self.rf_output.interviewer_revise_report(self.admin.interviewer_collection)

    def crpo_int_event_search_revise(self):
        self.event.crpo_search_event()
        self.rf_output.int_event_search_revise_report(self.event.event_search_collection)

    def crpo_int_event_interviews_revise(self):
        self.event.crpo_event_interviews()
        self.rf_output.int_event_interview_revise_report(self.event.event_interview_collection)

    def interviewer_provide_feedback_revise(self):
        self.feedback.interviewer_revise_provide_feedback()
        self.rf_output.int_provide_feedback_revise_report(self.feedback.int_revise__collection)


Object = ReviseFeedback()
Object.crpo_admin_login()
if Object.login_success:
    Object.crpo_event_search()
    Object.crpo_event_applicant_search()
    Object.crpo_schedule_interview()
    Object.crpo_candidate_status_verification()

    Object.interview_login()
    Object.crpo_int_event_search()
    Object.crpo_int_event_interviews()
    Object.interviewer_provide_feedback()

    Object.crpo_admin_re_login()
    Object.crpo_event_search_re_login()
    Object.crpo_event_applicant_search_re_login()
    Object.crpo_revise_feedback_enable()
    Object.crpo_candidate_revise_status_verification()

    Object.interview_login_revise()
    Object.crpo_int_event_search_revise()
    Object.crpo_int_event_interviews_revise()
    Object.interviewer_provide_feedback_revise()

"""
<<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
"""
Object.rf_output.overall_status()
Object.rf_output.history_html_generator()
Object.environment.close()
