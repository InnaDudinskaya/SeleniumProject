import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from selenium import webdriver
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def cart_with_product(driver, category_page, product_page):
    category_page.open_page()
    category_page.open_product(2)
    product_page.add_to_cart()
    product_page.wait_good_added_to_cart()
    cart_page = CartPage(driver)
    cart_page.open_page()
    return cart_page
