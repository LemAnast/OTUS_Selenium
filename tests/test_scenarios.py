import allure

from page_objects.add_product_page import AddProductPage
from page_objects.admin_page import AdminPage
from page_objects.admin_products_page import AdminProductsPage
from page_objects.alert_success_element import AlertSuccessElement
from page_objects.catalog_desktops_page import CatalogDesktopsPage
from page_objects.main_page import MainPage
from page_objects.register_page import RegisterPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.top_menu_element import TopMenu


@allure.feature("Admin page")
@allure.title("Проверка логина и разлогина в админ панель")
def test_login_and_logout_to_admin_page(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .login() \
        .wait_logged_in() \
        .logout() \
        .wait_logged_out()


@allure.feature("Main page")
@allure.title("Проверка добавления в корзину случайного товара с главной страницы")
def test_add_to_cart_random_product(browser):
    MainPage(browser).add_to_cart_random_product()
    AlertSuccessElement(browser) \
        .check_alert_success_text() \
        .close_alert()
    TopMenu(browser).click_shopping_cart_link()
    MainPage(browser).wait_url("/en-gb?route=checkout/cart")
    ShoppingCartPage(browser).check_product_in_cart()


@allure.feature("Main page")
@allure.title("Проверка, что при переключении валют цены на товары меняются на главной странице")
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


@allure.feature("Catalog page")
@allure.title("Проверка, что при переключении валют цены на товары меняются в каталоге")
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


@allure.feature("Admin page")
@allure.title("Проверка добавления нового товара в разделе администратора")
def test_add_new_product_admin_page(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .login() \
        .wait_logged_in()
    AdminProductsPage(browser) \
        .open_products_section() \
        .click_add_new_product()
    AddProductPage(browser) \
        .fill_product_name() \
        .fill_meta_tag_title() \
        .open_data_tab() \
        .fill_model() \
        .open_seo_tab() \
        .fill_seo_keyword() \
        .click_save_product()
    AlertSuccessElement(browser).check_alert_success_modified_product()


@allure.feature("Admin page")
@allure.title("Проверка удаления товара в разделе администратора")
def test_delete_product_admin_page(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .login() \
        .wait_logged_in()
    AdminProductsPage(browser) \
        .open_products_section() \
        .fill_filter_by_product_name() \
        .click_filter_button() \
        .click_checkbox_product() \
        .click_delete_button() \
        .submit_deleting_product()
    AlertSuccessElement(browser).check_alert_success_modified_product()


@allure.feature("Registration page")
@allure.title("Проверка регистрации нового пользователя")
def test_registration_user(browser):
    RegisterPage(browser) \
        .open_register_page() \
        .fill_your_personal_details_inputs() \
        .enter_valid_password() \
        .click_agreement_checkbox() \
        .click_submit_button() \
        .wait_success_registration()


@allure.feature("Main page")
@allure.title("Проверка переключения валют из верхнего меню")
def test_switching_currencies(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .select_euro_currency() \
        .click_currency_dropdown() \
        .select_pound_currency() \
        .click_currency_dropdown() \
        .select_dollar_currency()
