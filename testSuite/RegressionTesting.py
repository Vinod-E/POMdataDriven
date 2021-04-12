from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.E2E_Regression.crpo_job_creation import CRPOJobCreation
from Scripts.E2E_Regression.crpo_job_getby import CRPOJobGetBy
from Scripts.E2E_Regression.crpo_job_configuration import CRPOJobConfiguration
from Scripts.E2E_Regression.crpo_job_selection_process import CRPOJobSelectionProcess
from Scripts.E2E_Regression.crpo_job_feedback_form import CRPOJobFeedbackForm
from Scripts.E2E_Regression.crpo_job_feedback_form_new import CRPOJobFeedbackFormNew
from Scripts.E2E_Regression.crpo_job_tag_interviewers import CRPOJobTagInterviewers
from Scripts.E2E_Regression.crpo_job_automations import CRPOJobAutomations
from Scripts.E2E_Regression.crpo_req_creation import CRPOReqCreation
from Scripts.Output_scripts import E2EReport


class CRPOE2ERegression:
    """
        Required class Objects are created
    """
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
        job = CRPOJobCreation(driver=driver, index=index, version=version)
        job_getby = CRPOJobGetBy(driver=driver, index=index, version=version)
        job_Config = CRPOJobConfiguration(driver=driver, index=index)
        job_SP = CRPOJobSelectionProcess(driver=driver, index=index)
        job_feedback = CRPOJobFeedbackForm(driver=driver, index=index)
        job_new_feedback = CRPOJobFeedbackFormNew(driver=driver, index=index, version=version)
        job_interviewers = CRPOJobTagInterviewers(driver=driver, index=index)
        job_automations = CRPOJobAutomations(driver=driver, index=index)
        req = CRPOReqCreation(driver=driver, index=index, version=version)

        E2E_output = E2EReport.E2EOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True

        except Exception as error:
            ui_logger.error(error)

    def crpo_create_job(self):
        self.job.crpo_job_creation()
        self.E2E_output.job_creation_report(self.job.job_create_collection)

    def crpo_job_getby(self):
        self.job_getby.crpo_job_getby()
        self.E2E_output.job_getby_report(self.job_getby.job_getby_collection)

    def crpo_job_selection_process(self):
        self.job_SP.crpo_job_selection_process()
        self.E2E_output.job_sp_report(self.job_SP.job_sp_collection)

    def crpo_job_eligibility_criteria(self):
        self.job_Config.crpo_job_ec_configuration()
        self.E2E_output.job_ec_report(self.job_Config.job_ec_collection)

    def crpo_job_activity_task(self):
        self.job_Config.crpo_job_task_configuration()
        self.E2E_output.job_task_report(self.job_Config.job_task_collection)

    def crpo_job_interviewers(self):
        self.job_interviewers.crpo_job_tag_interviewers()
        self.E2E_output.job_tag_int_report(self.job_interviewers.job_tag_int_collection)

    def crpo_job_automations(self):
        self.job_automations.crpo_job_automations()
        self.E2E_output.job_automations_report(self.job_automations.job_automations_collection)

    def crpo_job_feedback_form1(self):
        self.job_feedback.crpo_job_feedback_form1()
        self.E2E_output.job_feed_report1(self.job_feedback.job_ff1_collection)

    def crpo_job_feedback_form2(self):
        self.job_feedback.crpo_job_feedback_form2()
        self.E2E_output.job_feed_report2(self.job_feedback.job_ff2_collection)

    def crpo_job_new_form_enable(self):
        self.job_new_feedback.crpo_job_new_form_enable()
        self.E2E_output.job_new_form_on_report(self.job_new_feedback.job_new_form_On_collection)

    def crpo_job_new_feedback_form(self):
        self.job_new_feedback.crpo_job_feedback_new_form()
        self.E2E_output.job_new_feed_report(self.job_new_feedback.job_new_form_collection)

    def crpo_job_new_form_disable(self):
        self.job_new_feedback.crpo_job_new_form_disable()
        self.E2E_output.job_new_form_off_report(self.job_new_feedback.job_new_form_Off_collection)

    def crpo_requirement_creation(self):
        self.req.crpo_req_creation()
        self.E2E_output.req_creation_report(self.req.req_create_collection)


Object = CRPOE2ERegression()
Object.crpo_login()

if Object.login_success:
    Object.crpo_create_job()
    Object.crpo_job_getby()
    Object.crpo_job_selection_process()
    Object.crpo_job_eligibility_criteria()
    Object.crpo_job_activity_task()
    Object.crpo_job_interviewers()
    Object.crpo_job_automations()
    Object.crpo_job_feedback_form1()
    Object.crpo_job_feedback_form2()
    Object.crpo_job_new_form_enable()
    Object.crpo_job_new_feedback_form()
    Object.crpo_job_new_form_disable()
    Object.crpo_requirement_creation()
    Object.E2E_output.overall_status()
    Object.environment.close()
