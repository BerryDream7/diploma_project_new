from selenium.common import TimeoutException

from pages.base import BasePage
from pages.header import Header
from pages.main import MainPage


class AuthPage(BasePage):
    _title = ("xpath", "//android.widget.TextView[@text='Authorization']")
    _login = ("xpath", "//android.widget.EditText[@text='Login']")
    _password = ("xpath", "//android.widget.EditText[@text='Password']")
    _sign_in_button = ("id", "ru.iteco.fmhandroid:id/enter_button")

    def __init__(self, driver):
        super().__init__(driver)
        self.toast_msg = ""

    def set_login(self, value):
        self.find_element(AuthPage._login).clear().send_keys(value)

    def set_password(self, value):
        self.find_element(AuthPage._password).clear().send_keys(value)

    def click_sign_in_button(self):
        self.find_element(AuthPage._sign_in_button).click()
        self.driver.implicitly_wait(1)
        self._toast_msg = self.driver.page_source

        # src = self.driver.page_source
        # with open("page-source.txt", "w") as f:
        #     f.write(src)

        try:
            header = Header(self.driver)
            assert header.user_icon.is_displayed()
            return MainPage(self.driver), header
        except TimeoutException:
            return

    @property
    def title(self):
        return self.find_element(AuthPage._title)

    @property
    def _toast_msg(self):
        return self.toast_msg

    @_toast_msg.setter
    def _toast_msg(self, page_src):
        lst = [s.split("\"") for s in page_src.split("\n") if s.find("Toast") != -1]
        if len(lst) == 0:
            return
        self.toast_msg = lst[0][7]
