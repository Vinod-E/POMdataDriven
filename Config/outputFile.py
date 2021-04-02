import os

PATH = os.getenv("HOME")
GENERIC_INPUT_PATH = "%s/PythonFrameWorkNew/Pytest_UI/Reports/" % PATH

OUTPUT_PATH = {
    'E2E_output': GENERIC_INPUT_PATH + 'UI_CRPO_E2E_REGRESSION.xls',
    'Mass_Interview_output': GENERIC_INPUT_PATH + 'UI_MASS_INTERVIEW.xls'
}
