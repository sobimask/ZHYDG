from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.logger import log
"""selenium基类的封装方法"""

class WebPage(object):
    """selenium基类"""
    """初始化定义"""
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver,self.timeout)

    def get_url(self,url):
        #self.driver.set_page_load_time(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(90)
            log("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException('打开网页超时检查网络' % url)

    @staticmethod
    def element_locator(func,locator):
        """元素定位器"""
        name,value = locator
        return func(LOCATE_MODE[name],value)

    def find_element(self,loactor):
        """选择单个元素"""

        return WebPage.element_locator(lambda *args: self.wait.until(
             EC.presence_of_element_located(args)),loactor)


    def find_elements(self,loactor):
        """选择多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), loactor)

    def elements_num(self,loactor):
        """获取相同元素个数"""
        number = len(self.find_elements(loactor))
        log("相同元素：{}".format((loactor,number)))
        return number

    def input_text(self,loactor,txt):
        """清空+输入"""
        sleep(1)
        ele = self.find_element(loactor)
        ele.clear()
        ele.send_keys(txt)
        log("输入文本: {}" .format(txt))

    def click(self,loactor):
        """点击"""
        self.find_element(loactor).click()
        sleep(1)
        log("点击元素: {}".format(loactor))

    def element_text(self,locator):
        """获取当前元素文本"""
        _text = self.find_element(locator).text
        log("获取文本: {}" .format(_text))
        return _text

    @property
    def get_source(self):
        """获取当前页面源码"""
        return self.driver.page.source

    def refresh(self):
        self.driver.refresh()
        self.driver.imlicitly_wait(30)

if __name__ == "__main__":
    pass
