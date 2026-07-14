from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):

    def __init__(self, driver, product_id='furn-9999-office-design-software-7', category='9'):
        super().__init__(driver)
        self.page_url = f'/shop/{product_id}?category={category}'

    def check_url_contains_product(self, product_id):
        self.check_url_contains(product_id)

    def check_product_title_is_not_empty(self):
        title = self.find(loc.product_title_loc)
        assert len(title.text.strip()) > 0, "Product title is empty"

    def check_price_is_displayed(self):
        self.check_element_displayed(loc.product_price_loc)

    def check_product_image_exists(self):
        image = self.find(loc.product_image_loc)
        self.wait.until(lambda driver: image.is_displayed())
        assert image.is_displayed(), "Product image is not visible"

    def check_add_to_cart_button_exists(self):
        element = self.find(loc.add_to_cart_button_loc)
        assert element.is_displayed(), "Button 'Add to cart' is not displayed"

    def add_to_cart(self):
        self.click(loc.add_to_cart_button_loc)

    def check_success_message_contains(self, expected_text):
        message = self.find(loc.success_message_loc)
        self.wait.until(lambda driver: message.is_displayed())
        actual_text = message.text.strip()
        assert expected_text in actual_text, \
            f"Expected '{expected_text}', got '{actual_text}'"
