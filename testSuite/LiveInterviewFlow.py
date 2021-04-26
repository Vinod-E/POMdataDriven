from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.LiveInterview.crpo_event_search import CrpoLiveEvent
from Scripts.LiveInterview.crpo_live_Schedule import CrpoLiveSchedule
from Scripts.LiveInterview.crpo_live_int1_login import CrpoInt1Login
from Scripts.LiveInterview.crpo_live_int2_login import CrpoInt2Login
from Scripts.LiveInterview.crpo_live_feedback_int1 import CrpoInt1Feedback
from Scripts.LiveInterview.crpo_live_feedback_int2 import CrpoInt2Feedback
from Scripts.Output_scripts import LiveInterviewReport


class MassInterviewFlow:
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
        event_search = CrpoLiveEvent(driver=driver, index=index, version=version)
        live_schedule = CrpoLiveSchedule(driver=driver, index=index, version=version)
        int1 = CrpoInt1Login(driver=driver, index=index, version=version)
        int1_feed = CrpoInt1Feedback(driver=driver, index=index, version=version)
        int2 = CrpoInt2Login(driver=driver, index=index, version=version)
        int2_feed = CrpoInt2Feedback(driver=driver, index=index, version=version)
        LIVE_OUTPUT = LiveInterviewReport.LiveOutputReport(version=version, server=server, start_date_time=date_time)

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
        self.event_search.live_event_search()
        self.LIVE_OUTPUT.event_name_report(self.event_search.event_search_collection)

    def event_live_schedule(self):
        self.live_schedule.live_interview_schedule()
        self.LIVE_OUTPUT.live_schedule_report(self.live_schedule.event_live_schedule_collection)

    def interviewer_one_login(self):
        self.int1.interviewer1_login()
        self.LIVE_OUTPUT.interviewer1_login_report(self.int1.int1_collection)

    def interviewer_one_live_feedback(self):
        self.int1_feed.live_interview1_feedback()
        self.LIVE_OUTPUT.interviewer1_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_one_provide_feedback(self):
        self.int1_feed.int1_provide_feedback()
        self.LIVE_OUTPUT.interviewer1_provide_feedback_report(self.int1_feed.pf1_collection)

    def interviewer_two_login(self):
        self.int2.interviewer2_login()
        self.LIVE_OUTPUT.interviewer2_login_report(self.int2.int2_collection)

    def interviewer_two_live_feedback(self):
        self.int2_feed.live_interview2_feedback()
        self.LIVE_OUTPUT.interviewer2_feedback_action_report(self.int1_feed.int1_feedback_collection)

    def interviewer_two_provide_feedback(self):
        self.int2_feed.int2_provide_feedback()
        self.LIVE_OUTPUT.interviewer2_provide_feedback_report(self.int2_feed.pf2_collection)


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.event_name_search()
    Object.event_live_schedule()
    Object.interviewer_one_login()
    Object.interviewer_one_live_feedback()
    Object.interviewer_one_provide_feedback()
    Object.interviewer_two_login()
    Object.interviewer_two_live_feedback()
    Object.interviewer_two_provide_feedback()
    Object.LIVE_OUTPUT.overall_status()
    Object.environment.close()
