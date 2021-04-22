from Config import inputFile
from pageObjects.Pages.EventPages import EventGetByNamePage
from pageObjects.Pages.MenuPages.eventSubTabPages import EventSubTabs
from pageObjects.Pages.EventPages.EventConfigurationTabPage import EventConfiguration
from pageObjects.Pages.MenuPages.menuPage import Menu
from pageObjects.Pages.SearchPages import AdvanceSearchPage
from utilities import excelRead


class EnableAutoAssign:
    def __init__(self, driver, index, version):
        self.driver = driver
        self.menu = Menu(self.driver)
        self.search = AdvanceSearchPage.Search(self.driver)
        self.getby = EventGetByNamePage.EventGetByName(self.driver)
        self.config = EventConfiguration(self.driver)
        self.event_sub_tab = EventSubTabs(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        status_excel = excelRead.ExcelRead()
        status_excel.read(inputFile.INPUT_PATH['event_assign_config'], index=index)
        xl = status_excel.excel_dict
        self.xl_menu_name = xl['menu'][0]
        self.xl_tab_title = xl['tab_title'][0]
        self.xl_event_name = xl['name'][0].format(version)
        self.xl_user_name = xl['user_name'][0]
        self.xl_on_off_button = xl['on_off'][0]
        self.xl_enable_disable_button = xl['enable_disable'][0]
        self.xl_save_button = xl['save'][0]
        self.xl_message = xl['message'][0]

        self.event_config_collection = []

    def auto_allocation_user_chat(self):

        self.event_config_collection = []
        __list = [self.menu.event_tab(self.xl_menu_name, self.xl_tab_title),
                  self.search.advance_search(),
                  self.search.name_field(self.xl_event_name),
                  self.search.search_button(),
                  self.getby.event_name_click(),
                  self.getby.event_name_validation(self.xl_event_name),
                  self.event_sub_tab.event_configurations(),
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
