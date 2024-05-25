from page_objects.catalog_desktops_page import CatalogDesktopsPage


def test_catalog_page_desktops_header(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_header()


def test_catalog_page_desktops_title(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_desktops_title()


def test_catalog_page_desktops_menu_elements(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .check_count_of_menu_items()


def test_catalog_page_desktops_mac_quantity(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .click_menu_item(2) \
        .check_count_of_product_items()


def test_catalog_page_desktops_select_list_view(browser):
    CatalogDesktopsPage(browser) \
        .open_catalog_desktops_page() \
        .activate_list_view() \
        .check_list_view()
