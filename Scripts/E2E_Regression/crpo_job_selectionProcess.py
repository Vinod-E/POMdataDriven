from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.JobPages.JobActionsPage import Actions


class CRPOJobSelectionProcess:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(self.driver)

        self.job_sp_collection = []

    def crpo_job_selection_process(self):
        self.job_sp_collection = []

        __list = [self.actions.job_actions_click(),
                  self.actions.tag_selection_process()
                  ]
        for func in __list:
            if func:
                self.job_sp_collection.append(func)
            else:
                self.job_sp_collection.append(func)
        print(self.job_sp_collection)
