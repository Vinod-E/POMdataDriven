from Config import Enviroment
from Listeners.logger_settings import ui_logger
from Scripts.Login.crpo_login_page import CRPOLogin
from Scripts.Output_scripts import MassInterviewReport
from Scripts.MassInterview.crpo_room_create import Room
from Scripts.MassInterview.crpo_assign_room import AssignRoom
from Scripts.MassInterview.crpo_interviewer_login import InterviewLogin
from Scripts.MassInterview.crpo_select_candidate import SelectCandidate
from Scripts.MassInterview.crpo_invite_candidate import InviteCandidate
from Scripts.MassInterview.crpo_provide_feedback import ProvideFeedback
from Scripts.MassInterview.crpo_enable_auto_assign import EnableAutoAssign
from Scripts.MassInterview.crpo_event_change_applicant_status import EventApplicant
from Scripts.MassInterview.crpo_event_slot_configuration import SlotConfiguration
from Scripts.MassInterview.crpo_candidate_login import CandidateLobbyLogin


class MassInterviewFlow:
    """
        Required class Objects are created
    """
    time = input('slot time (ex:- 10:10 AM) ::')
    environment = ''
    login_success = ''
    login_link = ''
    id = ''

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
        status = EventApplicant(driver=driver, index=index, version=version)
        slot = SlotConfiguration(driver=driver, index=index, time=time)
        allocation = EnableAutoAssign(driver=driver, index=index)
        room = Room(driver=driver, index=index, version=version)
        candidate = CandidateLobbyLogin(driver=driver, index=index, version=version)
        assign_room = AssignRoom(driver=driver, index=index, version=version)
        int_login = InterviewLogin(driver=driver, index=index, version=version)
        select = SelectCandidate(driver=driver, index=index, version=version)
        invite = InviteCandidate(driver=driver, index=index, version=version)
        feedback = ProvideFeedback(driver=driver, index=index, version=version)

        MASS_OUTPUT = MassInterviewReport.MassOutputReport(version=version, server=server, start_date_time=date_time)

    except Exception as error:
        ui_logger.error(error)
        environment.close()

    def crpo_login(self):
        try:
            self.login.crpo_login()
            self.login_success = True
        except Exception as error:
            ui_logger.error(error)

    def applicant_status_change(self):
        self.status.event()
        self.MASS_OUTPUT.event_report(0, 1, self.status.event_collection)

        self.status.event_applicant_grid()
        self.id = self.status.candidate_details.candidate_id
        self.MASS_OUTPUT.event_applicant_report(self.status.applicant_collection)

    def auto_allocation_configuration(self):
        self.status.event()
        self.MASS_OUTPUT.event_report(4, 5, self.status.event_collection)

        self.allocation.auto_allocation_user_chat()
        self.MASS_OUTPUT.auto_allocation_report(self.allocation.event_config_collection)

    def slot_configuration(self):
        self.slot.slot_configurations(self.id)
        self.login_link = self.slot.slot_config.candidate_login_link
        self.MASS_OUTPUT.slot_config_report(self.slot.event_slot_collection)

    def room_creation(self):
        self.room.create_room()
        self.MASS_OUTPUT.create_room_report(self.room.room_collection)

    def candidate_lobby(self):
        self.candidate.candidate_lobby_login(self.id, self.login_link)
        self.MASS_OUTPUT.candidate_login_report(self.candidate.candidate_lobby_collection)

    def room_tagging(self):
        self.assign_room.assign_room()
        self.MASS_OUTPUT.room_tag_report(self.assign_room.assign_room_collection)

    def interviewer_logins(self):
        self.int_login.interviewer_login()
        self.MASS_OUTPUT.interviewer_login_report(self.int_login.int_collection)

    def candidate_selection(self):
        self.select.select_candidate(self.id, self.login_link)
        self.MASS_OUTPUT.select_candidate_report(self.select.select_candidate_collection)

    def feedback_provide(self):
        self.feedback.provide_feedback()
        self.MASS_OUTPUT.feedback_report(self.feedback.pf_collection)

    def candidate_invitation(self):
        self.invite.invite_candidate(self.id, self.login_link)
        self.MASS_OUTPUT.invite_candidate_report(self.invite.invite_candidate_collection)


Object = MassInterviewFlow()
Object.crpo_login()

if Object.login_success:
    Object.applicant_status_change()
    Object.auto_allocation_configuration()
    Object.slot_configuration()
    Object.room_creation()
    Object.candidate_lobby()
    Object.room_tagging()
    Object.interviewer_logins()
    Object.candidate_selection()
    Object.feedback_provide()
    Object.candidate_invitation()
    Object.MASS_OUTPUT.overall_status()
    Object.environment.close()
