from page_base.webpage import WebPage,sleep
from common.readelement import Element

login_page = Element('login_page')

class LoginPage(WebPage):
    """登录类"""

    def input_username(self,username):
        """输入账号"""
        self.input_text(login_page['username'],txt = username)
        sleep(1)

    def input_password(self, password):
        """输入密码"""
        self.input_text(login_page['password'], txt=password)
        sleep(1)

    def click_loginbutton(self):
        """点击登录按钮"""
        self.click(login_page['loginbutton'])
        sleep(5)

if __name__ == '__main__':
    print(login_page['loginbutton'][1])
