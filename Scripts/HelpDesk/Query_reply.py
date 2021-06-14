from Config import inputFile
from utilities import excelRead
from pageObjects.Pages.EmbraceCandidatePages.ReplyQueryPage import CandidateQueryReplyPage


class CandidateQueryReply:

    def __init__(self, driver, index, version):
        self.driver = driver
        self.query_reply = CandidateQueryReplyPage(self.driver)

        """
        ----------------- EXCEL READ AND TO ASSIGN VALUES TO RESPECTIVE INIT VARIABLES ------>>>>
        """
        query_excel = excelRead.ExcelRead()
        query_excel.read(inputFile.INPUT_PATH['candidate_queries'], index=index)
        xl = query_excel.excel_dict
        self.xl_candidate = xl['candidate'][0].format(version)
        self.xl_subject = xl['subject'][0]
        self.xl_message = xl['message'][0]

        self.reply_1_collection = []
        self.reply_2_collection = []
        self.reply_3_collection = []

    def user_reply_1(self):
        self.reply_1_collection = []
        __list = [self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.reply_to_query(),
                  self.query_reply.in_progress_tab(),
                  self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.mark_as_closed(),
                  self.query_reply.confirm_button()
                  ]
        for func in __list:
            if func:
                self.reply_1_collection.append(func)
            else:
                self.reply_1_collection.append(func)

    def user_reply_2(self):
        self.reply_2_collection = []
        __list = [self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.reply_to_query(),
                  self.query_reply.in_progress_tab(),
                  self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.mark_as_closed(),
                  self.query_reply.confirm_button()
                  ]
        for func in __list:
            if func:
                self.reply_2_collection.append(func)
            else:
                self.reply_2_collection.append(func)

    def user_reply_3(self):
        self.reply_3_collection = []
        __list = [self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.reply_to_query(),
                  self.query_reply.in_progress_tab(),
                  self.query_reply.search_candidate_query(self.xl_candidate),
                  self.query_reply.select_proper_query_based_on_subject(self.xl_subject),
                  self.query_reply.reply_message_entry(self.xl_message),
                  self.query_reply.mark_as_closed(),
                  self.query_reply.confirm_button()
                  ]
        for func in __list:
            if func:
                self.reply_3_collection.append(func)
            else:
                self.reply_3_collection.append(func)
