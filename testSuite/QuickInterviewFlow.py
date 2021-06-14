from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.QuickInterview.crpo_event_applicant_search import CrpoQuickEvent
from Scripts.QuickInterview.crpo_event_quick_schedule import CRPOQuickInterviewSchedule
from Scripts.QuickInterview.crpo_quick_int1_login import CrpoInt1Login
from Scripts.QuickInterview.crpo_quick_int2_login import CrpoInt2Login
from Scripts.QuickInterview.crpo_quick_feedback_int1 import CrpoInt1Feedback
from Scripts.QuickInterview.crpo_quick_feedback_int2 import CrpoInt2Feedback
from Scripts.Output_scripts import QuickInterviewReport


class QuickInterviewFlow:
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
        event = CrpoQuickEvent(driver=driver, index=index, version=version)
        quick_schedule = CRPOQuickInterviewSchedule(driver=driver, index=index, version=version)
        int1 = CrpoInt1Login(driver=driver, index=index, version=version)
        int1_feed = CrpoInt1Feedback(driver=driver, index=index, version=version)
        int2 = CrpoInt2Login(driver=driver, index=index, version=version)
        int2_feed = CrpoInt2Feedback(driver=driver, index=index, version=version)
        QUICK_OUTPUT = QuickInterviewReport.QuickOutputReport(version=version, server=server, start_date_time=date_time)

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
        self.event.quick_event_applicant_search()
        self.QUICK_OUTPUT.event_app_report(self.event.event_search_collection)

    def schedule_quick_interview_config(self):
        self.quick_schedule.quick_interview_config()
        self.QUICK_OUTPUT.quick_report(self.quick_schedule.quick_config_collection)

    def schedule_quick_interview(self):
        self.quick_schedule.quick_interview_schedule()
        self.QUICK_OUTPUT.quick_schedule_report(self.quick_schedule.quick_schedule_collection)

    def interviewer_one_login(self):
        self.int1.interviewer1_login()
        self.QUICK_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interviewer_one_quick_feedback(self):
        self.int1_feed.quick_interview1_feedback()
        self.QUICK_OUTPUT.interviewer1_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_one_provide_feedback(self):
        self.int1_feed.int1_provide_feedback()
        self.QUICK_OUTPUT.interviewer1_provide_feedback_report(self.int1_feed.pf1_collection)

    def interviewer_two_login(self):
        self.int2.interviewer2_login()
        self.QUICK_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interviewer_two_quick_feedback(self):
        self.int2_feed.quick_interview2_feedback()
        self.QUICK_OUTPUT.interviewer2_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_two_partial_submission(self):
        self.int2_feed.int2_partial_submission()
        self.QUICK_OUTPUT.interviewer2_partial_report(self.int2_feed.partial_collection)

    def interviewer_two_provide_feedback(self):
        self.int2_feed.int2_provide_feedback()
        self.QUICK_OUTPUT.interviewer2_provide_feedback_report(self.int2_feed.pf2_collection)


Object = QuickInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_applicant_search()
    Object.schedule_quick_interview_config()
    Object.schedule_quick_interview()
    Object.interviewer_one_login()
    Object.interviewer_one_quick_feedback()
    Object.interviewer_one_provide_feedback()
    Object.interviewer_two_login()
    Object.interviewer_two_quick_feedback()
    Object.interviewer_two_partial_submission()
    Object.interviewer_two_provide_feedback()
    """
     <<=========== OUTPUT REPORTS GENERATOR PARTS HERE BELOW =============>>
    """
    Object.QUICK_OUTPUT.overall_status()
    Object.QUICK_OUTPUT.history_html_generator()
    Object.environment.close()
