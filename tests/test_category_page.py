def test_category_page_loads(category_page):
    category_page.open_page()
    category_page.check_url_contains_category('desks-1')


def test_category_page_displays_main_elements(category_page):
    category_page.open_page()
    category_page.check_products_exist()
    category_page.check_price_slider_exists()
    category_page.check_legs_checkbox_exists()
    category_page.check_categories_dropdown_exists()


def test_cart_icon_click(category_page):
    category_page.open_page()
    first_item_cart_number = 2
    category_page.get_cart_icon_click(first_item_cart_number)
    category_page.is_add_to_cart_dialog_opened()
