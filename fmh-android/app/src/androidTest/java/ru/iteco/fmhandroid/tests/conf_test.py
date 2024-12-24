import pathlib

import pytest
import io.github.bonigarcia.wdm.WebDriverManager
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.chrome.ChromeOptions
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

pytest_plugins = ["pages_fixtures_test"]


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start()
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


@pytest.fixture(scope="session", params=appium_driver(), name="driver")
def appium_session(request, appium_service):
    driver = webdriver.Remote("http://127.0.0.1:4723/", options=request.params)
    yield driver
    driver.remove_app(app_id="ru.iteco.fmhandroid")
    driver.quit()


@pytest.fixture
def setup(driver):
    driver.activate_app(app_id="ru.iteco.fmhandroid")
    yield
    # driver.terminate_app(app_id="ru.iteco.fmhandroid")
    driver.execute_script("mobile: clearApp", {"appId": "ru.iteco.fmhandroid"})