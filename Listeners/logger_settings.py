import sys
import logging
from Config import CongfigFile
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s.%(msecs)03d %(process)d ] %(levelname)s "
                       "[%(name)s:%(filename)s:%(funcName)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'ui-logger': {'class': 'logging.handlers.RotatingFileHandler',
                      'formatter': 'verbose',
                      'level': logging.DEBUG,
                      'filename': CongfigFile.LOG_FILE,
                      'maxBytes': 52428800,
                      'backupCount': 7},
        'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
                                 'formatter': 'verbose',
                                 'level': logging.DEBUG,
                                 'filename': CongfigFile.BATCH_FILE,
                                 'maxBytes': 52428800,
                                 'backupCount': 7},
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
    },
    loggers={
        'ui_logger': {
            'handlers': ['ui-logger', 'console'],
            'level': logging.DEBUG
        },
        'batch_process_logger': {
            'handlers': ['batch-process-logger', 'console'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)

ui_logger = logging.getLogger('ui_logger')
batch_process_logger = logging.getLogger('batch_process_logger')
