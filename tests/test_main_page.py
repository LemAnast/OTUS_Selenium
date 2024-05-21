from page_objects.main_page import MainPage
from page_objects.top_menu_element import TopMenu


def test_main_page_currency(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .check_currency_list()


def test_main_page_empty_cart_text(browser):
    MainPage(browser) \
        .click_cart_dropdown() \
        .check_empty_cart_dropdown_text()


def test_main_page_carousel_0(browser):
    MainPage(browser) \
        .check_carousel_items(0)


def test_main_page_product_buttons(browser):
    MainPage(browser) \
        .check_product_buttons()


def test_main_page_carousel_1(browser):
    MainPage(browser) \
        .check_carousel_items(1)
