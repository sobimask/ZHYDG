# -*- coding:utf-8 -*-
import re
import pytest
from tools.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage
from tools.times import datatime_strftime

class TestLogin:

    @pytest.fixture(scope='function', autouse=True)
    def open_web(self,drivers):
        """打开登录页"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        #log("打开登录页")

    def test_001(self,drivers):
        """输入账号"""
        login = LoginPage(drivers)
        login.input_username('zkzc')
        #log("输入账号zkzc")

    def test_002(self,drivers):
        """输入密码"""
        login = LoginPage(drivers)
        login.input_password('zkzc123')
        #log("输入密码")

    def test_003(self,drivers):
        """点击登录"""
        login = LoginPage(drivers)
        login.click_loginbutton()
        #log("点击登录按钮")

if __name__ == '__main__':
    pytest.main(['-s','TestCase/test_login.py','--pytest_report',datatime_strftime()+'report.html'])
