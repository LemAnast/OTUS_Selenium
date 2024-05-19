from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage


def test_product_page_iphone_card_url(browser):
    MainPage(browser) \
        .click_featured_product(1) \
        .wait_url("/en-gb/product/iphone")


def test_product_page_iphone_header(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_header_iphone()


def test_product_page_iphone_price(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_price_iphone()


def test_product_page_iphone_rating(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_rating()


def test_product_page_iphone_related_products(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_related_product_header() \
        .check_related_product_items()
