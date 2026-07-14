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
        slider_wrapper = self.find(loc.price_slider_wrapper_loc)
        assert slider_wrapper.is_displayed(), "Price slider is not visible"
