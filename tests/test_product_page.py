from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_iphone_card_url(browser):
    browser.find_element(By.CSS_SELECTOR, "img[title='iPhone']").click()
    WebDriverWait(browser, 2).until(EC.url_to_be(
        browser.url + "/en-gb/product/iphone"), message="URL не верен")


def test_product_page_iphone_header(browser):
    browser.get(browser.url + "/en-gb/product/iphone")
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "h1"), "iPhone"),
        message="Заголовок карточки iPhone не верен"
    )


def test_product_page_iphone_price(browser):
    browser.get(browser.url + "/en-gb/product/iphone")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "price-new")),
        message="Цена iPhone не отображается"
    )


def test_product_page_iphone_rating(browser):
    browser.get(browser.url + "/en-gb/product/iphone")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "rating")),
        message="Рейтинг iPhone не отображается"
    )
    star_qty = WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "fa-stack")))
    assert len(star_qty) == 5, "Количество звезд рейтинга не равно 5"


def test_product_page_iphone_related_products(browser):
    browser.get(browser.url + "/en-gb/product/iphone")
    WebDriverWait(browser, 2).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "h3"), "Related Products"),
        message="Заголовок блока связанных продуктов не верен"
    )
    WebDriverWait(browser, 2).until(EC.visibility_of_any_elements_located(
        (By.CSS_SELECTOR, "div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 .product-thumb")),
        message="В блоке связанных продуктов пусто"
    )
