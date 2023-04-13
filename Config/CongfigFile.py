import os

# ----- Ubuntu -----
PATH = os.getenv("HOME")
COMMON_FOLDER_PATH = "%s/hirepro_automation/POMdataDriven/" % PATH
INPUT_FILE = "%s/hirepro_automation/POMdataDriven/testData/" % PATH
MICROSITE_INPUT_FILE = "%s/hirepro_automation/POMdataDriven/testData/microsite/" % PATH
OUTPUT_FILE = "%s/hirepro_automation/POMdataDriven/Reports/" % PATH
HTML_OUTPUT_FILE = "%s/hirepro_automation/POMdataDriven/Reports/HTML_Reports/" % PATH
HISTORY_FILE = "%s/hirepro_automation/POMdataDriven/Reports/Graph_Sprint_Data/" % PATH
LOG_FILE = COMMON_FOLDER_PATH + 'Logs/ui_automation.log'
BATCH_FILE = COMMON_FOLDER_PATH + 'Logs/batch.log'
INI_FILE = COMMON_FOLDER_PATH + 'Config/config.ini'
IMAGE = COMMON_FOLDER_PATH + 'ScreenShots/{}.png'
SLASH = '/'

# ----- Windows -------
# PATH = os.path.join("C:\\Users\\user\\Desktop")
# COMMON_FOLDER_PATH = "%s\\hirepro_automation\\POMdataDriven\\" % PATH
# INPUT_FILE = "%s\\hirepro_automation\\POMdataDriven\\testData\\" % PATH
# MICROSITE_INPUT_FILE = "%s\\hirepro_automation\\POMdataDriven\\testData\\microsite\\" % PATH
# OUTPUT_FILE = "%s\\hirepro_automation\\POMdataDriven\\Reports\\" % PATH
# HTML_OUTPUT_FILE = "%s\\hirepro_automation\\POMdataDriven\\Reports\\HTML_Reports\\" % PATH
# HISTORY_FILE = "%s\\hirepro_automation\\POMdataDriven\\Reports\\Graph_Sprint_Data\\" % PATH
# LOG_FILE = COMMON_FOLDER_PATH + 'Logs\\ui_automation.log'
# BATCH_FILE = COMMON_FOLDER_PATH + 'Logs\\batch.log'
# INI_FILE = COMMON_FOLDER_PATH + 'Config\\config.ini'
# IMAGE = COMMON_FOLDER_PATH + 'ScreenShots\\{}.png'
# SLASH = '\\'
