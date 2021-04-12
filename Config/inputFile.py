from Config import CongfigFile

GENERIC_INPUT_PATH = CongfigFile.INPUT_FILE

INPUT_PATH = {
    'login_excel': GENERIC_INPUT_PATH + 'Login_Details.xls',
    'job_excel': GENERIC_INPUT_PATH + 'Job_Details.xls',
    'job_attachment': GENERIC_INPUT_PATH + 'job-description.pdf',
    'job_config_excel': GENERIC_INPUT_PATH + 'Job_Configurations.xls',
    'job_automation': GENERIC_INPUT_PATH + 'Job_automations.xls',
    'job_feedback_form': GENERIC_INPUT_PATH + 'Job_Feedback_from_config.xls',
    'event_status_change': GENERIC_INPUT_PATH + 'Event_change_status.xls',
    'event_slot_config': GENERIC_INPUT_PATH + 'Event_slot_config.xls',
    'event_assign_config': GENERIC_INPUT_PATH + 'Event_assign_chat_config.xls',
    'event_room': GENERIC_INPUT_PATH + 'Event_room_creation.xls',
    'candidate_lobby': GENERIC_INPUT_PATH + 'Lobby_Candidate.xls',
    'interview_lobby': GENERIC_INPUT_PATH + 'Lobby_Interviewer.xls',
    'feedback': GENERIC_INPUT_PATH + 'feedback.xls',
    'requirement_excel': GENERIC_INPUT_PATH + 'requirement.xls',
}
