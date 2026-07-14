def test_category_page_loads(category_page):
    category_page.open_page()
    category_page.check_url_contains_category('desks-1')


def test_category_page_has_products(category_page):
    category_page.open_page()
    category_page.check_products_exist()


def test_price_slider_is_present(category_page):
    category_page.open_page()
    category_page.check_price_slider_exists()
