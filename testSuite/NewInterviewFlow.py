from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.NewFeedbackInterview.crpo_event_applicant_search import CrpoNewEvent
from Scripts.NewFeedbackInterview.crpo_change_applicant_status import EventApplicant
from Scripts.NewFeedbackInterview.crpo_new_int1_login import CrpoInt1Login
from Scripts.NewFeedbackInterview.crpo_new_int2_login import CrpoInt2Login
from Scripts.NewFeedbackInterview.crpo_new_feedback_int1 import CrpoInt1Feedback
from Scripts.NewFeedbackInterview.crpo_new_feedback_int2 import CrpoInt2Feedback
from Scripts.Output_scripts import NewFeedbackInterviewReport


class NewFeedbackInterviewFlow:
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
        event = CrpoNewEvent(driver=driver, index=index, version=version)
        schedule = EventApplicant(driver=driver, index=index, version=version)
        int1 = CrpoInt1Login(driver=driver, index=index, version=version)
        int1_feed = CrpoInt1Feedback(driver=driver, index=index, version=version)
        int2 = CrpoInt2Login(driver=driver, index=index, version=version)
        int2_feed = CrpoInt2Feedback(driver=driver, index=index, version=version)
        NEW_OUTPUT = NewFeedbackInterviewReport.NewFeedbackOutputReport(version=version, server=server,
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
        self.NEW_OUTPUT.event_app_report(self.event.event_search_collection)

    def event_applicant_change_status_schedule(self):
        self.schedule.event_change_applicant_status()
        self.NEW_OUTPUT.change_status_report(self.schedule.applicant_status_collection)

    def interviewer_one_login(self):
        self.int1.interviewer1_login()
        self.NEW_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interviewer_one_new_feedback(self):
        self.int1_feed.new_form_interview1_feedback()
        self.NEW_OUTPUT.interviewer1_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_one_provide_feedback(self):
        self.int1_feed.int1_provide_feedback()
        self.NEW_OUTPUT.interviewer1_provide_feedback_report(self.int1_feed.pf1_collection)

    def interviewer_two_login(self):
        self.int2.interviewer2_login()
        self.NEW_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interviewer_two_new_feedback(self):
        self.int2_feed.new_form_interview2_feedback()
        self.NEW_OUTPUT.interviewer2_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_two_provide_feedback(self):
        self.int2_feed.int2_provide_feedback()
        self.NEW_OUTPUT.interviewer2_provide_feedback_report(self.int2_feed.pf2_collection)


Object = NewFeedbackInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_applicant_search()
    Object.event_applicant_change_status_schedule()
    Object.interviewer_one_login()
    Object.interviewer_one_new_feedback()
    Object.interviewer_one_provide_feedback()
    Object.interviewer_two_login()
    Object.interviewer_two_new_feedback()
    Object.interviewer_two_provide_feedback()
    Object.NEW_OUTPUT.overall_status()
    Object.environment.close()
