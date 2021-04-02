import os

# ----- Ubuntu -----
PATH = os.getenv("HOME")
COMMON_FOLDER_PATH = "%s/PythonFrameWorkNew/Pytest_UI/" % PATH
LOG_FILE = COMMON_FOLDER_PATH + 'Logs/ui_automation.log'
BATCH_FILE = COMMON_FOLDER_PATH + 'Logs/batch.log'
INI_FILE = COMMON_FOLDER_PATH + 'Config/config.ini'
IMAGE = COMMON_FOLDER_PATH + 'ScreenShots/{}.png'
SLASH = '/'

# ----- Windows -------
# PATH = os.path.join("D:\\")
# COMMON_FOLDER_PATH = "%s\\hirepro_automation\\UI-Automation\\" % PATH
# LOG_FILE = COMMON_FOLDER_PATH + 'logs\\ui_automation.log'
# BATCH_FILE = COMMON_FOLDER_PATH + 'logs\\batch.log'

# SLASH = '\\'
