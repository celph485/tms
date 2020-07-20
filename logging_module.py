import logging
from logging.handlers import RotatingFileHandler
from datetime import date
from pathlib import Path

LOG_DIR = '/tmp/logs/tms/'
DATE_FORMAT = '%Y-%m-%d'
LOG_FILE_SIZE = 20_000_000
LOG_FILE_BACKUP_COUNT = 2_000

FILE_LOG_FORMAT =    '%(asctime)s :: %(threadName)-9s :: %(filename)-10s:%(lineno)3d :: %(message)s'
CONSOLE_LOG_FORMAT = '%(asctime)s :: %(threadName)-9s :: %(filename)-10s:%(lineno)3d :: %(message)s'


def get_file_handler():
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    curr_date_str = date.today().strftime(DATE_FORMAT)    
    file_path = f'{LOG_DIR}tms_{curr_date_str}.log'
    handler = RotatingFileHandler(file_path,
                                    maxBytes=LOG_FILE_SIZE,
                                    backupCount=LOG_FILE_BACKUP_COUNT,
                                    delay=True)
    handler.setFormatter(logging.Formatter(FILE_LOG_FORMAT))
    return handler


def get_console_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(CONSOLE_LOG_FORMAT))
    return handler


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    log.addHandler(get_file_handler())
    log.addHandler(get_console_handler())
    return log