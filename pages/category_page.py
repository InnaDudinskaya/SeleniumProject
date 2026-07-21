from pages.base_page import BasePage
from pages.locators import category_page_locators as loc


class CategoryPage(BasePage):

    def __init__(self, driver, category='desks-1'):
        super().__init__(driver)
        self.page_url = f'/shop/category/{category}'

    def check_url_contains_category(self, category):
        self.check_url_contains(category)

    def check_products_exist(self):
        products = self.find_all(loc.product_items_loc)
        assert len(products) > 0, "Products are not found"

    def check_price_slider_exists(self):
        self.check_element_displayed(loc.price_slider_wrapper_loc)

    def check_legs_checkbox_exists(self):
        self.check_element_displayed(loc.first_legs_checkbox_loc)

    def check_categories_dropdown_exists(self):
        self.check_element_displayed(loc.categories_dropdown_loc)

    def open_product(self, product_number):
        products = self.find_all(loc.product_items_loc)
        if products:
            products[product_number].click()
            return True
        return False

    def get_cart_icon_click(self, cart_icon_number):
        cart_icons = self.find_all(loc.items_cart_icons)
        cart_icons[cart_icon_number].click()

    def is_add_to_cart_dialog_opened(self):
        assert self.find(loc.add_to_card_dialog_title).is_displayed()
