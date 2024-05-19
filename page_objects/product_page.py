import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PATH = "/en-gb/product/iphone"
    HEADER = By.CSS_SELECTOR, "h1"
    PRICE = By.CSS_SELECTOR, "#content .price-new"
    RATING_STAR = By.CLASS_NAME, "fa-stack"
    RP_HEADER = By.CSS_SELECTOR, "h3"
    RP_PRODUCT = By.CLASS_NAME, "product-thumb"

    def open_product_page_iphone(self):
        self.open_page(self.PATH)
        return self

    def check_product_header_iphone(self):
        assert self.get_element(self.HEADER).text == "iPhone", \
            "Заголовок карточки iPhone не верен"
        return self

    def check_product_price_iphone(self):
        assert self.get_element(self.PRICE).text == "$123.20", \
            "Цена iPhone некорректна"
        return self

    def check_product_rating(self):
        star_list = self.get_elements(self.RATING_STAR)
        assert len(star_list) == 5, \
            "Количество звезд рейтинга не равно 5"
        return self

    def check_related_product_header(self):
        assert self.get_element(self.RP_HEADER).text == "Related Products", \
            "Заголовок блока связанных продуктов не верен"
        return self

    def check_related_product_items(self):
        self.get_any_element(self.RP_PRODUCT)
        return self
