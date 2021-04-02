import configparser
from Config import CongfigFile


config = configparser.RawConfigParser()
config.read(CongfigFile.INI_FILE)


class ReadConfig:
    @staticmethod
    def get_qa_url():
        url = config.get('urls', 'QA')
        return url

    @staticmethod
    def get_beta_url():
        url = config.get('urls', 'BETA')
        return url

    @staticmethod
    def get_stage_url():
        url = config.get('urls', 'STAGE')
        return url

    @staticmethod
    def get_production_url():
        url = config.get('urls', 'PRODUCTION')
        return url

    @staticmethod
    def get_indiaams_url():
        url = config.get('urls', 'INDIAAMS')
        return url
