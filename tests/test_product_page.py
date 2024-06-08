import allure

from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage


@allure.feature("Product page")
@allure.title("Проверка перехода на страницу товара iPhone")
def test_product_page_iphone_card_url(browser):
    MainPage(browser) \
        .click_featured_product(1) \
        .wait_url("/en-gb/product/iphone")


@allure.feature("Product page")
@allure.title("Проверка хэдера на странице товара iPhone")
def test_product_page_iphone_header(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_header_iphone()


@allure.feature("Product page")
@allure.title("Проверка цены на странице товара iPhone")
def test_product_page_iphone_price(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_price_iphone()


@allure.feature("Product page")
@allure.title("Проверка рейтинга на странице товара iPhone")
def test_product_page_iphone_rating(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_product_rating()


@allure.feature("Product page")
@allure.title("Проверка блока 'связанные продукты' на странице товара iPhone")
def test_product_page_iphone_related_products(browser):
    ProductPage(browser) \
        .open_product_page_iphone() \
        .check_related_product_header() \
        .check_related_product_items()
