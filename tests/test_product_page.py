def test_product_page_loads(product_page):
    product_page.open_page()
    product_page.check_url_contains_product('furn-9999')


def test_product_page_has_details(product_page):
    product_page.open_page()
    product_page.check_product_title_is_not_empty()
    product_page.check_price_is_displayed()
    product_page.check_product_image_exists()


def test_product_page_can_add_to_cart(product_page):
    product_page.open_page()
    product_page.check_add_to_cart_button_exists()
    product_page.add_to_cart()
    product_page.check_success_message_contains("Item(s) added to your cart")
