from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    def check_page_title_contains_cart(self):
        self.check_title_contains('cart')

    def check_url_contains_cart(self):
        self.check_url_contains('cart')

    def check_order_overview_text(self):
        self.check_element_text("Order overview", loc.order_overview_loc)
