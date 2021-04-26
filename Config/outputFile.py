from Config import CongfigFile

GENERIC_OUTPUT_PATH = CongfigFile.OUTPUT_FILE

OUTPUT_PATH = {
    'E2E_output': GENERIC_OUTPUT_PATH + 'UI_CRPO_E2E_REGRESSION.xls',
    'Mass_Interview_output': GENERIC_OUTPUT_PATH + 'UI_MASS_INTERVIEW.xls',
    'Live_Interview_output': GENERIC_OUTPUT_PATH + 'UI_LIVE_INTERVIEW.xls',
    'Quick_Interview_output': GENERIC_OUTPUT_PATH + 'UI_QUICK_INTERVIEW.xls'
}
