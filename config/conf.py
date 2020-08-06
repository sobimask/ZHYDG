import os
from selenium.webdriver.common.by import By

#项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件
INI_PATH = os.path.join(BASE_DIR,'config','config.ini')

#页面元素文件
ELEMENT_PATH = os.path.join(BASE_DIR,'page_element')

#日志目录
LOG_PATH = os.path.join(BASE_DIR,'logs\\')

#报告目录
REPORT_PATH = os.path.join(BASE_DIR,'report')

#元素定位类型
LOCATE_MODE = {
    'css1': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}
