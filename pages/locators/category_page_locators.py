from selenium.webdriver.common.by import By

product_items_loc = (By.CSS_SELECTOR, 'img.position-absolute')
price_slider_wrapper_loc = (By.CSS_SELECTOR, ".multirange-wrapper")
first_legs_checkbox_loc = (By.XPATH, "(//b[text()='Legs']/following::input[@name='attrib'])[1]")
categories_dropdown_loc = (By.CSS_SELECTOR, "#top_menu a.nav-link.dropdown-toggle.active")
items_cart_icons = (By.CLASS_NAME, "fa-shopping-cart")
add_to_card_dialog_title = (By.CLASS_NAME, "modal-title")
