import pathlib

import pytest
from appium import webdriver as appium_webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from pages.authorization import AuthPage
from pages.main import MainPage
from pages.news import NewsListPage

# pytest_plugins = ["pages_fixtures_test"]

pytestmark = pytest.mark.usefixtures("setup")

@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(args=['--base-path', '/wd/hub'])
    # service.start(args=["--config-file", str(pathlib.Path(pathlib.Path.cwd(), ".appiumrc.json"))])
    yield
    service.stop()


def appium_driver():
    caps = {
        "platformName": "Android",
        "automationName": 'UiAutomator2',
        "platformVersion": "9",
        "allowTestPackages": "true",
        "app": str(pathlib.Path(pathlib.Path.cwd(), "apk", "app-debug.apk")),
        "autoLaunch": "false",
        "appPackage": "ru.iteco.fmhandroid",
        "appActivity": ".ui.AppActivity"
    }
    app_options = UiAutomator2Options().load_capabilities(caps=caps)
    app_options.timeouts = {"implicit": 1, "pageLoad": 2, "script": 0}
    return app_options


@pytest.fixture(scope="session", params=[appium_driver()], name="driver")
def appium_session(request, appium_service):
    driver = webdriver.Remote("http://127.0.0.1:4723/", options=request.param)
    yield driver
    driver.remove_app(app_id="ru.iteco.fmhandroid")
    driver.quit()


@pytest.fixture
def setup(driver):
    driver.activate_app(app_id="ru.iteco.fmhandroid")
    yield
    # driver.terminate_app(app_id="ru.iteco.fmhandroid")
    driver.execute_script("mobile: clearApp", {"appId": "ru.iteco.fmhandroid"})

