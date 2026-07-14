def test_cart_page_loads(cart_page):
    cart_page.open_page()
    cart_page.check_url_contains_cart()


def test_cart_page_has_order_overview_text(cart_page):
    cart_page.open_page()
    cart_page.check_order_overview_text()


def test_cart_page_has_title(cart_page):
    cart_page.open_page()
    cart_page.check_page_title_contains_cart()
