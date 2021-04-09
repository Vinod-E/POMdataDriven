from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.E2E_Regression.crpo_job_creation import CRPOJobCreation
from Scripts.E2E_Regression.crpo_job_getby import CRPOJobGetBy
from Scripts.E2E_Regression.crpo_job_configuration import CRPOJobSelectionProcess
from Scripts.E2E_Regression.crpo_job_feedback_form import CRPOJobFeedbackForm
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
        job_Config = CRPOJobSelectionProcess(driver=driver, index=index)
        job_feedback = CRPOJobFeedbackForm(driver=driver, index=index)

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
        self.job_Config.crpo_job_selection_process()
        self.E2E_output.job_sp_report(self.job_Config.job_sp_collection)

    def crpo_job_eligibility_criteria(self):
        self.job_Config.crpo_job_ec_configuration()
        self.E2E_output.job_ec_report(self.job_Config.job_ec_collection)

    def crpo_job_activity_task(self):
        self.job_Config.crpo_job_task_configuration()
        self.E2E_output.job_task_report(self.job_Config.job_task_collection)

    def crpo_job_feedback_form1(self):
        self.job_feedback.crpo_job_feedback_form1()
        self.E2E_output.job_feed_report1(self.job_feedback.job_ff1_collection)

    def crpo_job_feedback_form2(self):
        self.job_feedback.crpo_job_feedback_form2()
        self.E2E_output.job_feed_report2(self.job_feedback.job_ff2_collection)


Object = CRPOE2ERegression()
Object.crpo_login()

if Object.login_success:
    Object.crpo_create_job()
    Object.crpo_job_getby()
    Object.crpo_job_selection_process()
    Object.crpo_job_eligibility_criteria()
    Object.crpo_job_activity_task()
    Object.crpo_job_feedback_form1()
    Object.crpo_job_feedback_form2()
    Object.E2E_output.overall_status()
    Object.environment.close()
