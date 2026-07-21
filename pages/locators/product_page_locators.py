from selenium.webdriver.common.by import By

product_title_loc = (By.CSS_SELECTOR, 'h1[itemprop="name"]')
product_price_loc = (By.CSS_SELECTOR, '.oe_price .oe_currency_value')
product_image_loc = (By.CSS_SELECTOR, 'img.product_detail_img')
add_to_cart_button_loc = (By.ID, "add_to_cart")
success_message_loc = (By.XPATH, "//strong[contains(text(), 'Item(s) added to your cart')]")
cart_item_added_loc = (By.XPATH, "//*[contains(@class, 'my_cart_quantity')][contains(text(), '1')]")
