from Config import CongfigFile

GENERIC_OUTPUT_PATH = CongfigFile.OUTPUT_FILE
GENERIC_OUTPUT_PATH_HTML = CongfigFile.HTML_OUTPUT_FILE
GENERIC_OUTPUT_PATH_HISTORY = CongfigFile.HISTORY_FILE

OUTPUT_PATH = {
    'E2E_output': GENERIC_OUTPUT_PATH + 'UI_CRPO_E2E_REGRESSION.xls',
    'Mass_Interview_output': GENERIC_OUTPUT_PATH + 'UI_MASS_INTERVIEW.xls',
    'Live_Interview_output': GENERIC_OUTPUT_PATH + 'UI_LIVE_INTERVIEW.xls',
    'Quick_Interview_output': GENERIC_OUTPUT_PATH + 'UI_QUICK_INTERVIEW.xls',
    'New_Interview_output': GENERIC_OUTPUT_PATH + 'UI_NEW_INTERVIEW.xls',
    'Cancel_Interview_output': GENERIC_OUTPUT_PATH + 'UI_INTERVIEW_CANCELLATION.xls',
    'Unlock_update_output': GENERIC_OUTPUT_PATH + 'UI_UNLOCK_UPDATE_INTERVIEW.xls',
    'Help_desk_output': GENERIC_OUTPUT_PATH + 'UI_HELP_DESK_QUERY.xls',
    'Manage_output': GENERIC_OUTPUT_PATH + 'UI_MANAGE_INTERVIEWERS.xls',
    'Certi_output': GENERIC_OUTPUT_PATH + 'UI_CERTIFICATE_REGISTRATION.xls',

    'E2E_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_CRPO_E2E_REGRESSION.html',
    'Mass_Interview_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_MASS_INTERVIEW.html',
    'Live_Interview_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_LIVE_INTERVIEW.html',
    'Quick_Interview_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_QUICK_INTERVIEW.html',
    'New_Interview_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_NEW_INTERVIEW.html',
    'Cancel_Interview_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_INTERVIEW_CANCELLATION.html',
    'Unlock_update_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_UNLOCK_UPDATE_INTERVIEW.html',
    'Help_desk_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_HELP_DESK_QUERY.html',
    'Manage_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_MANAGE_INTERVIEWERS.html',
    'Certi_output_html': GENERIC_OUTPUT_PATH_HTML + 'UI_CERTIFICATE_REGISTRATION.html',

    'E2E_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'E2E_REGRESSION_HISTORY_DATA.xlsx',
    'Mass_Interview_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'MASS_INTERVIEW_HISTORY_DATA.xlsx',
    'Live_Interview_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'LIVE_INTERVIEW_HISTORY_DATA.xlsx',
    'Quick_Interview_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'QUICK_INTERVIEW_HISTORY_DATA.xlsx',
    'New_Interview_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'NEW_INTERVIEW_HISTORY_DATA.xlsx',
    'Cancel_Interview_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'INTERVIEW_CANCELLATION_HISTORY_DATA.xlsx',
    'Unlock_update_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'UNLOCK_UPDATE_INTERVIEW_HISTORY_DATA.xlsx',
    'Help_desk_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'HELP_DESK_QUERY_HISTORY_DATA.xlsx',
    'Manage_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'MANAGE_INTERVIEWERS_HISTORY_DATA.xlsx',
    'Certi_output_history': GENERIC_OUTPUT_PATH_HISTORY + 'UI_CERTIFICATE_REGISTRATION_HISTORY_DATA.xlsx',
}
