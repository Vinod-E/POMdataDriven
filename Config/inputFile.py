from Config import CongfigFile

GENERIC_INPUT_PATH = CongfigFile.INPUT_FILE
MICROSITE_GENERIC_INPUT_PATH = CongfigFile.MICROSITE_INPUT_FILE


INPUT_PATH = {
    'upload': GENERIC_INPUT_PATH + 'candidateUpload.xls',
    'job_attachment': GENERIC_INPUT_PATH + 'job-description.pdf',
    'OCR_candidate': MICROSITE_GENERIC_INPUT_PATH + 'OCR_Candidate.png',
    'OCR_PAN': MICROSITE_GENERIC_INPUT_PATH + 'OCR_PAN.jpg',
    'OCR_id_card': MICROSITE_GENERIC_INPUT_PATH + 'college_id_card.jpg',

    'login_excel': GENERIC_INPUT_PATH + 'Login_Details.xls',
    'job_excel': GENERIC_INPUT_PATH + 'Job_Details.xls',
    'job_config_excel': GENERIC_INPUT_PATH + 'Job_Configurations.xls',
    'job_automation': GENERIC_INPUT_PATH + 'Job_automations.xls',
    'job_feedback_form': GENERIC_INPUT_PATH + 'Job_Feedback_from_config.xls',
    'event_status_change': GENERIC_INPUT_PATH + 'Event_change_status.xls',
    'event_assign_config': GENERIC_INPUT_PATH + 'Event_assign_chat_config.xls',
    'event_slot_room': GENERIC_INPUT_PATH + 'Event_slot_room_creation.xls',
    'candidate_lobby': GENERIC_INPUT_PATH + 'Lobby_Candidate.xls',
    'interview_lobby': GENERIC_INPUT_PATH + 'Lobby_Interviewer.xls',
    'feedback': GENERIC_INPUT_PATH + 'feedback.xls',
    'cancel_interview': GENERIC_INPUT_PATH + 'CancelInterviews.xls',
    'requirement_excel': GENERIC_INPUT_PATH + 'requirement.xls',
    'assessment_excel': GENERIC_INPUT_PATH + 'assessment_details.xls',
    'event_excel': GENERIC_INPUT_PATH + 'event_details.xls',
    'manage_task': GENERIC_INPUT_PATH + 'manage_task_details.xls',
    'embrace': GENERIC_INPUT_PATH + 'embrace.xls',
    'help_desk': GENERIC_INPUT_PATH + 'Help_desk_config.xls',
    'candidate_queries': GENERIC_INPUT_PATH + 'candidate_query.xls',
    'manage_interviewers': GENERIC_INPUT_PATH + 'Manage_interviewers.xls',
    'microsite_common': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeCommon.xls',
    'microsite_certificate': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeCertificate.xls',
    'microsite_education': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeEducation.xls',
    'microsite_OCR': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeOCR.xls',
    'microsite_razorpay': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeRazorPay.xls',
    'microsite_Aadhar': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeAadhar.xls',
    'microsite_WorkProfile': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeWorkProfile.xls',
    'microsite_CP': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeCP.xls',
    'microsite_ACP': MICROSITE_GENERIC_INPUT_PATH + 'MicrositeACP.xls'
}
