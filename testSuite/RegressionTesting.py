from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.E2E_Regression.crpo_job_creation import CRPOJobCreation
from Scripts.E2E_Regression.crpo_job_getby import CRPOJobGetBy
from Scripts.E2E_Regression.crpo_job_selectionProcess import CRPOJobSelectionProcess
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
        job_sp = CRPOJobSelectionProcess(driver=driver, index=index, version=version)

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
        self.job_sp.crpo_job_selection_process()
        self.E2E_output.job_sp_report(self.job_sp.job_sp_collection)


Object = CRPOE2ERegression()
Object.crpo_login()

if Object.login_success:
    Object.crpo_create_job()
    Object.crpo_job_getby()
    Object.crpo_job_selection_process()
    Object.E2E_output.overall_status()
    Object.environment.close()
