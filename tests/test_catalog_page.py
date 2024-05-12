from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page_desktops_header(browser):
    browser.find_element(By.CSS_SELECTOR, "#narbar-menu li.nav-item:nth-child(1)").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".dropdown-menu.show .see-all"))
    ).click()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#content h2"), "Desktops"),
        message="Заголовок раздела Desktops не верен"
    )


def test_catalog_page_desktops_title(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    WebDriverWait(browser, 1).until(EC.title_is("Desktops"), message="Тайтл раздела Desktops не верен")


def test_catalog_page_desktops_menu_elements(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    menu_list = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".list-group.mb-3 a"))
    )
    assert len(menu_list) == 10, "Количество элементов в меню не верно"


def test_catalog_page_desktops_mac_quantity(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left a:nth-child(3)"))
    ).click()
    mac_list = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "#product-list .product-thumb"))
    )
    assert len(mac_list) == 1, "Некорректное количество товаров в разделе Mac"


def test_catalog_page_desktops_select_list_view(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.ID, "button-list"))
    ).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "product-list")), message="Представление в виде списка не работает"
    )
