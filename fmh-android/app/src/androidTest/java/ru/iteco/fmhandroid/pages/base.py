from typing import List, Union

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement as MobileWebElement
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 15, 0.5, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException))

    def find_element(self, locator) -> MobileWebElement:
        return self.wait.until(lambda x: x.find_element(*locator),
                               f"Cant find element by locator {locator}")

    def find_elements(self, locator) -> Union[List[MobileWebElement], List]:
        return self.wait.until(lambda x: x.find_elements(*locator),
                               f"Cant find elements by locator {locator}")
