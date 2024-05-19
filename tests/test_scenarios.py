from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.admin_page import AdminPage
from page_objects.alert_success_element import AlertSuccessElement
from page_objects.main_page import MainPage
from page_objects.shopping_cart_page import ShoppingCartPage


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
    MainPage(browser) \
        .click_shopping_cart_link() \
        .wait_url("/en-gb?route=checkout/cart")
    ShoppingCartPage(browser).check_product_in_cart()


def test_main_page_switch_currencies(browser):
    product_items = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "product-thumb"))
    )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(1)").click()
    for i in range(1, len(product_items)+1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "€"),
            message="Некорректная цена в евро"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(2)").click()
    for i in range(1, len(product_items)+1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "£"),
            message="Некорректная цена в фунтах"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(3)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "$"),
            message="Некорректная цена в долларах"
        )


def test_catalog_page_switch_currencies(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    product_items = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "product-thumb")))
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(1)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "€"),
            message="Некорректная цена в евро"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(2)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "£"),
            message="Некорректная цена в фунтах"
        )
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.CSS_SELECTOR, f"ul.dropdown-menu.show > li:nth-child(3)").click()
    for i in range(1, len(product_items) + 1):
        WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) .price-new"), "$"),
            message="Некорректная цена в долларах"
        )
