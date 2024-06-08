import allure

from page_objects.catalog_desktops_page import CatalogDesktopsPage


@allure.feature("Catalog page")
@allure.title("Проверка хэдера в каталоге десктопов")
def test_catalog_page_desktops_header(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_header()


@allure.feature("Catalog page")
@allure.title("Проверка заголовка в каталоге десктопов")
def test_catalog_page_desktops_title(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_title()


@allure.feature("Catalog page")
@allure.title("Проверка количества элементов меню в каталоге десктопов")
def test_catalog_page_desktops_menu_elements(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_count_of_menu_items()


@allure.feature("Catalog page")
@allure.title("Проверка количества товаров Mac в каталоге десктопов")
def test_catalog_page_desktops_mac_quantity(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .click_menu_item(2) \
        .check_count_of_product_items()


@allure.feature("Catalog page")
@allure.title("Проверка переключения представления на список в каталоге десктопов")
def test_catalog_page_desktops_select_list_view(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .activate_list_view() \
        .check_list_view()
