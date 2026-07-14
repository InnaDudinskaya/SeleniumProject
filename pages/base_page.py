from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def check_url_contains(self, text: str):
        self.wait.until(lambda driver: text in driver.current_url)
        assert text in self.driver.current_url

    def check_title_contains(self, text: str):
        self.wait.until(lambda driver: text.lower() in driver.title.lower())
        assert text.lower() in self.driver.title.lower()

    def check_element_displayed(self, locator: tuple[str, str]):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        assert element.is_displayed()

    def check_element_text(self, expected_text: str, locator: tuple[str, str]):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        assert element.text == expected_text
