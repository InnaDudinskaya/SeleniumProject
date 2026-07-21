from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    @staticmethod
    def get_checkout_button_loc():
        return loc.checkout_button_loc

    @staticmethod
    def get_order_overview_loc():
        return loc.order_overview_loc

    @staticmethod
    def get_continue_shopping_link_loc():
        return loc.continue_shopping_link_loc

    @staticmethod
    def get_remove_button_loc():
        return loc.remove_button_loc

    def proceed_to_checkout(self):
        self.click(loc.checkout_button_loc)

    def remove_product(self):
        self.click(loc.remove_button_loc)

    def click_continue_shopping(self):
        self.click(loc.continue_shopping_link_loc)

    def is_cart_empty(self) -> bool:
        return self.is_element_visible(loc.empty_cart_message_loc)

    def is_element_visible(self, locator: tuple[str, str]) -> bool:
        try:
            element = self.find(locator)
            return element.is_displayed()
        except:
            return False
