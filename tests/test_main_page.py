import allure

from page_objects.main_page import MainPage
from page_objects.top_menu_element import TopMenu


@allure.feature("Main page")
@allure.title("Проверка валют в выпадающем списке на главной странице")
def test_main_page_currency(browser):
    TopMenu(browser) \
        .click_currency_dropdown() \
        .check_currency_list()


@allure.feature("Main page")
@allure.title("Проверка уведомления в пустой корзине на главной странице")
def test_main_page_empty_cart_text(browser):
    MainPage(browser) \
        .click_cart_dropdown() \
        .check_empty_cart_dropdown_text()


@allure.feature("Main page")
@allure.title("Проверка количества баннеров в верхней карусели на главной странице")
def test_main_page_carousel_0(browser):
    MainPage(browser) \
        .check_carousel_items(0)


@allure.feature("Main page")
@allure.title("Проверка отображения кнопок в карточке продуктов на главной странице")
def test_main_page_product_buttons(browser):
    MainPage(browser) \
        .check_product_buttons()


@allure.feature("Main page")
@allure.title("Проверка количества баннеров в нижней карусели на главной странице")
def test_main_page_carousel_1(browser):
    MainPage(browser) \
        .check_carousel_items(1)
