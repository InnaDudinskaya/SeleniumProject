def test_product_page_main_elements(product_page):
    product_page.open_page()
    product_page.check_url_contains('furn-9999')
    product_page.check_product_title_is_not_empty()
    product_page.check_price_is_displayed()
    product_page.check_product_image_exists()
    product_page.check_add_to_cart_button_exists()


def test_add_product_to_cart(product_page):
    product_page.open_page()
    product_page.add_to_cart()
    product_page.check_element_text("Item(s) added to your cart", product_page.get_success_message_loc())
