from Config import inputFile
from pageObjects.Pages.EventPages.EventConfigurationTabPage import EventConfiguration
from utilities import excelRead


class EnableAutoAssign:
    def __init__(self, driver, index):
        self.driver = driver
        self.config = EventConfiguration(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_assign_config'], index=index)
        xl = status_excel.excel_dict
        self.xl_user_name = xl['user_name'][0]
        self.xl_on_off_button = xl['on_off'][0]
        self.xl_enable_disable_button = xl['enable_disable'][0]
        self.xl_save_button = xl['save'][0]
        self.xl_message = xl['message'][0]

        self.event_config_collection = []

    def auto_allocation_user_chat(self):

        self.event_config_collection = []
        __list = [self.config.configurations_tab(),
                  self.config.on_off_buttons(self.xl_on_off_button),
                  self.config.user_id_chat(),
                  self.config.search_user_chat(self.xl_user_name),
                  self.config.enable_disable_button(self.xl_enable_disable_button),
                  self.config.save_buttons(self.xl_save_button, self.xl_message)
                  ]
        for func in __list:
            if func:
                self.event_config_collection.append(func)
            else:
                self.event_config_collection.append(func)
