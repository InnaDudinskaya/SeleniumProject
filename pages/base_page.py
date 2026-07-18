from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.custom_conditions import UrlContains
from utils.custom_conditions import TitleContainsIgnoreCase
from utils.custom_conditions import ElementHasText
from utils.custom_conditions import ElementIsVisible
from utils.custom_conditions import ElementIsClickable


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple[str, str]):
        return self.wait.until(ec.presence_of_element_located(locator))

    def find_all(self, locator: tuple[str, str]):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]):
        element = self.wait.until(ElementIsClickable(locator))
        element.click()

    def check_url_contains(self, text: str):
        self.wait.until(UrlContains(text))
        assert text in self.driver.current_url

    def check_title_contains(self, text: str):
        self.wait.until(TitleContainsIgnoreCase(text))
        assert text.lower() in self.driver.title.lower()

    def check_element_displayed(self, locator: tuple[str, str]):
        element = self.wait.until(ElementIsVisible(locator))
        assert element.is_displayed()

    def check_element_text(self, expected_text: str, locator: tuple[str, str]):
        self.wait.until(ElementHasText(locator, expected_text))
        element = self.find(locator)
        assert element.text == expected_text
