class UrlContains:

    def __init__(self, text: str):
        self.text = text

    def __call__(self, driver):
        return self.text in driver.current_url


class TitleContainsIgnoreCase:

    def __init__(self, text: str):
        self.text = text.lower()

    def __call__(self, driver):
        return self.text in driver.title.lower()


class ElementHasText:

    def __init__(self, locator: tuple, expected_text: str):
        self.locator = locator
        self.expected_text = expected_text

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.text == self.expected_text:
            return element
        return False


class ElementIsVisible:

    def __init__(self, locator: tuple):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.is_displayed():
            return element
        return False


class ElementIsClickable:

    def __init__(self, locator: tuple):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.is_displayed() and element.is_enabled():
            return element
        return False
