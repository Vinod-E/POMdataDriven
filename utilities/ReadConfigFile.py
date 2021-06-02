import configparser
from Config import CongfigFile


config = configparser.RawConfigParser()
config.read(CongfigFile.INI_FILE)


class ReadConfig:
    @staticmethod
    def get_qa_url():
        url = config.get('crpoUrls', 'QA')
        return url

    @staticmethod
    def get_beta_url():
        url = config.get('crpoUrls', 'BETA')
        return url

    @staticmethod
    def get_stage_url():
        url = config.get('crpoUrls', 'STAGE')
        return url

    @staticmethod
    def get_production_url():
        url = config.get('crpoUrls', 'PRODUCTION')
        return url

    @staticmethod
    def get_indiaams_url():
        url = config.get('crpoUrls', 'INDIAAMS')
        return url

    @staticmethod
    def get_qa_candidate_url():
        url = config.get('candidateLoginUrls', 'QA')
        return url

    @staticmethod
    def get_beta_candidate_url():
        url = config.get('candidateLoginUrls', 'BETA')
        return url

    @staticmethod
    def get_stage_candidate_url():
        url = config.get('candidateLoginUrls', 'STAGE')
        return url

    @staticmethod
    def get_production_candidate_url():
        url = config.get('candidateLoginUrls', 'PRODUCTION')
        return url

    @staticmethod
    def get_indiaams_candidate_url():
        url = config.get('candidateLoginUrls', 'INDIAAMS')
        return url

    @staticmethod
    def get_qa_embrace_url():
        url = config.get('embraceLoginUrls', 'QA')
        return url

    @staticmethod
    def get_beta_embrace_url():
        url = config.get('embraceLoginUrls', 'BETA')
        return url

    @staticmethod
    def get_stage_embrace_url():
        url = config.get('embraceLoginUrls', 'STAGE')
        return url

    @staticmethod
    def get_production_embrace_url():
        url = config.get('embraceLoginUrls', 'PRODUCTION')
        return url

    @staticmethod
    def get_indiaams_embrace_url():
        url = config.get('embraceLoginUrls', 'INDIAAMS')
        return url
