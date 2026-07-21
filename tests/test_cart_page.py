def test_cart_page_main_elements(cart_with_product):
    cart_with_product.check_url_contains('cart')
    cart_with_product.check_title_contains('Cart')
    cart_with_product.check_element_text("Order overview", cart_with_product.get_order_overview_loc())
    cart_with_product.check_element_displayed(cart_with_product.get_checkout_button_loc())
    cart_with_product.check_element_displayed(cart_with_product.get_continue_shopping_link_loc())
    cart_with_product.check_element_displayed(cart_with_product.get_remove_button_loc())


def test_continue_shopping_link(cart_with_product):
    cart_with_product.click_continue_shopping()
    cart_with_product.check_url_contains('/shop')


def test_remove_product_from_cart(cart_with_product):
    cart_with_product.remove_product()

    assert cart_with_product.is_cart_empty(), "Empty cart message is not displayed"


def test_proceed_to_checkout(cart_with_product):
    cart_with_product.proceed_to_checkout()
    cart_with_product.check_url_contains('address')
