from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_currency(browser):
    browser.find_element(By.ID, "form-currency").click()
    currency_list = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "ul.dropdown-menu.show > li"))
    )
    assert len(currency_list) == 3, "Количество валют в дропдауне не равно 3"


def test_main_page_empty_cart_text(browser):
    browser.find_element(By.ID, "header-cart").click()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#header-cart li.text-center"), "Your shopping cart is empty!"),
        message="Некорректный текст при пустой корзине"
    )


def test_main_page_carousel_0(browser):
    carousel_0 = browser.find_elements(By.CSS_SELECTOR, "#carousel-banner-0 .carousel-item")
    assert len(carousel_0) == 2, "Количество элементов в карусели не равно 2"


def test_main_page_product_buttons(browser):
    product_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    for i in range(1, len(product_items)+1):
        product_buttons = browser.find_elements(By.CSS_SELECTOR, f"div.col.mb-3:nth-child({i}) button")
        assert len(product_buttons) == 3, f"Количество кнопок на {i} карточке продукта не равно 3"


def test_main_page_carousel_1(browser):
    carousel_1 = browser.find_elements(By.CSS_SELECTOR, "#carousel-banner-1 .carousel-item")
    assert len(carousel_1) == 3, "Количество элементов в карусели не равно 3"
