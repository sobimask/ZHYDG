import time
import datetime

def timestamp():
    '''时间戳'''
    return time.time()

def datatime_strftime(fmt = '%Y%m%d-%H%M'):
    '''datatime格式化时间'''
    return datetime.datetime.now().strftime(fmt)

def sleep(seconds = 1.0):
    """睡眠时间"""
    time.sleep(seconds)

if __name__ == '__main__':
    print(datatime_strftime())