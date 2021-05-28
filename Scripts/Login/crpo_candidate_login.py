from Config import inputFile
from utilities import excelRead, appTitle, ReadConfigFile
from utilities.OpenNewTab import NewTab
from pageObjects.Pages.LoginPages.CandidateLoginPage import CandidateLogin


class CRPOCandidateLogin:
    def __init__(self, driver, index, version, server):
        self.driver = driver
        self.server = server

        self.LoginPage = CandidateLogin(self.driver)
        self.title = appTitle.Title(self.driver)
        self.new_tab = NewTab(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        login_excel = excelRead.ExcelRead()
        login_excel.read(inputFile.INPUT_PATH['login_excel'], index=index)
        xl = login_excel.excel_dict
        self.xl_title = xl['c_p_title'][0]
        self.xl_user = xl['c_p_user'][0].format(version)

    def candidate_login(self, candidate_email, password):
        if self.server == 'amsin':
            self.new_tab.open_new_tab(1, ReadConfigFile.ReadConfig.get_qa_candidate_url())
        elif self.server == 'ams':
            self.new_tab.open_new_tab(1, ReadConfigFile.ReadConfig.get_production_candidate_url())
        elif self.server == 'beta':
            self.new_tab.open_new_tab(1, ReadConfigFile.ReadConfig.get_beta_candidate_url())
        elif self.server == 'stage':
            self.new_tab.open_new_tab(1, ReadConfigFile.ReadConfig.get_stage_candidate_url())
        elif self.server == 'india':
            self.new_tab.open_new_tab(1, ReadConfigFile.ReadConfig.get_indiaams_candidate_url())

        assert self.title.tab_title(self.xl_title) == self.xl_title
        self.LoginPage.login_name(candidate_email)
        self.LoginPage.password(password)
        self.LoginPage.login_button()

        self.LoginPage.login_account_name_verification(self.xl_user)
        print(f'{self.xl_user} logged in successfully')
        self.title.tab_title(self.xl_title)
