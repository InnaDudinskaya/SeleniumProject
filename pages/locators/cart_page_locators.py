from selenium.webdriver.common.by import By

checkout_button_loc = (By.NAME, "website_sale_main_button")
order_overview_loc = (By.XPATH, "//h3[text()='Order overview']")
continue_shopping_link_loc = (By.CSS_SELECTOR, "a[href='/shop']")
remove_button_loc = (By.XPATH, "//a[contains(text(), 'Remove')]")
empty_cart_message_loc = (By.CSS_SELECTOR, ".alert-info")
