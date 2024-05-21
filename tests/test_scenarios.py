from page_objects.admin_page import AdminPage
from page_objects.alert_success_element import AlertSuccessElement
from page_objects.catalog_desktops_page import CatalogDesktopsPage
from page_objects.main_page import MainPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.top_menu_element import TopMenu


def test_login_and_logout_to_admin_page(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .login() \
        .wait_logged_in() \
        .logout() \
        .wait_logged_out()


def test_add_to_cart_random_product(browser):
    MainPage(browser).add_to_cart_random_product()
    AlertSuccessElement(browser) \
        .check_alert_success_text() \
        .close_alert()
    TopMenu(browser).click_shopping_cart_link()
    MainPage(browser).wait_url("/en-gb?route=checkout/cart")
    ShoppingCartPage(browser).check_product_in_cart()


def test_main_page_switch_currencies(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_euro_currency()
    MainPage(browser) \
        .check_prices_in_euro()
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_pound_currency()
    MainPage(browser) \
        .check_prices_in_pound()
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_dollar_currency()
    MainPage(browser) \
        .check_prices_in_dollar()


def test_catalog_page_switch_currencies(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page()
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_euro_currency()
    CatalogDesktopsPage(browser) \
        .check_prices_in_euro()
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_pound_currency()
    CatalogDesktopsPage(browser) \
        .check_prices_in_pound()
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_dollar_currency()
    CatalogDesktopsPage(browser) \
        .check_prices_in_dollar()


def test_add_new_product_admin_page(browser):
    AdminPage(browser).open_admin_page()
    pass


#def test_delete_product_admin_page():
    pass


#def test_registration_user():
    pass


def test_switching_currencies(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_euro_currency() \
        .click_currency_dropdown() \
        .select_pound_currency() \
        .click_currency_dropdown() \
        .select_dollar_currency()
