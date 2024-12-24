import pytest

from pages.authorization import AuthPage
from pages.main import MainPage
from pages.news import NewsListPage


@pytest.fixture(name="auth")
def authorization(auth_page):
    """single activity app"""
    auth_page.set_login("login2")
    auth_page.set_password("password2")
    return auth_page.click_sign_in_button()


@pytest.fixture(name="auth_page")
def init_auth_page(driver):
    # print(getattr(request.session, "driver"))
    return AuthPage(driver)


@pytest.fixture(name="main_page")
def init_main_page(driver):
    return MainPage(driver)

@pytest.fixture(name="news_lst_page")
def init_news_lst_page(driver):
    return NewsListPage(driver)