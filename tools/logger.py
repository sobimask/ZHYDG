from nb_log import LogManager
from config.conf import LOG_PATH
from tools.times import datatime_strftime
import os

def log(text):
    logger = LogManager('INFO').get_logger_and_add_handlers(is_add_stream_handler=True,
                                                log_filename=LOG_PATH+datatime_strftime()+'.log')
    logger.info(text)

if __name__ == '__main__':
    log('日志开始')
