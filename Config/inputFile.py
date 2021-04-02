import os

PATH = os.getenv("HOME")
GENERIC_INPUT_PATH = "%s/PythonFrameWorkNew/Pytest_UI/testData/" % PATH

INPUT_PATH = {
    'login_excel': GENERIC_INPUT_PATH + 'Login_Details.xls',
    'job_excel': GENERIC_INPUT_PATH + 'Job_Details.xls',
    'job_attachment': GENERIC_INPUT_PATH + 'job-description.pdf',
    'job_config_excel': GENERIC_INPUT_PATH + 'Job_Configurations.xls',
    'event_status_change': GENERIC_INPUT_PATH + 'Event_change_status.xls',
    'event_slot_config': GENERIC_INPUT_PATH + 'Event_slot_config.xls',
    'event_assign_config': GENERIC_INPUT_PATH + 'Event_assign_chat_config.xls',
    'event_room': GENERIC_INPUT_PATH + 'Event_room_creation.xls',
    'candidate_lobby': GENERIC_INPUT_PATH + 'Lobby_Candidate.xls',
    'interview_lobby': GENERIC_INPUT_PATH + 'Lobby_Interviewer.xls',
    'feedback': GENERIC_INPUT_PATH + 'feedback.xls'
}
