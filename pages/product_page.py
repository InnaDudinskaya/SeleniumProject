from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):

    def __init__(self, driver, product_id='furn-9999-office-design-software-7', category='9'):
        super().__init__(driver)
        self.page_url = f'/shop/{product_id}?category={category}'

    @staticmethod
    def get_success_message_loc():
        return loc.success_message_loc

    def check_product_title_is_not_empty(self):
        title = self.find(loc.product_title_loc)
        assert len(title.text.strip()) > 0, "Product title is empty"

    def check_price_is_displayed(self):
        self.check_element_displayed(loc.product_price_loc)

    def check_product_image_exists(self):
        self.check_element_displayed(loc.product_image_loc)

    def check_add_to_cart_button_exists(self):
        self.check_element_displayed(loc.add_to_cart_button_loc)

    def add_to_cart(self):
        self.click(loc.add_to_cart_button_loc)

    def wait_good_added_to_cart(self):
        self.find(loc.cart_item_added_loc)
