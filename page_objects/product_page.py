import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PATH = "/en-gb/product/iphone"
    HEADER = By.CSS_SELECTOR, "h1"
    PRICE = By.CSS_SELECTOR, "#content .price-new"
    RATING_STAR = By.CLASS_NAME, "fa-stack"
    RP_HEADER = By.CSS_SELECTOR, "h3"
    RP_PRODUCT = By.CLASS_NAME, "product-thumb"

    @allure.step("Открыть страницу продукта iPhone")
    def open_product_page_iphone(self):
        self.logger.info("Open iPhone product page")
        self.open_page(self.PATH)
        return self

    @allure.step("Проверить отображение хэдера на странице продукта iPhone")
    def check_product_header_iphone(self):
        self.logger.info("Check the display of the header in the iPhone product page")
        assert self.get_element(self.HEADER).text == "iPhone", \
            "Заголовок карточки iPhone не верен"
        return self

    @allure.step("Проверить цену на странице продукта iPhone")
    def check_product_price_iphone(self):
        self.logger.info("Check price in iPhone product page")
        assert self.get_element(self.PRICE).text == "$123.20", \
            "Цена iPhone некорректна"
        return self

    @allure.step("Проверить рейтинг на странице продукта iPhone")
    def check_product_rating(self):
        self.logger.info("Check rating in iPhone product page")
        star_list = self.get_elements(self.RATING_STAR)
        assert len(star_list) == 5, \
            "Количество звезд рейтинга не равно 5"
        return self

    @allure.step("Проверить заголовок блока похожих продуктов на странице продукта iPhone")
    def check_related_product_header(self):
        self.logger.info("Check the title of related products on the iPhone product page")
        assert self.get_element(self.RP_HEADER).text == "Related Products", \
            "Заголовок блока связанных продуктов не верен"
        return self

    @allure.step("Проверить наличие похожих продуктов на странице продукта iPhone")
    def check_related_product_items(self):
        self.logger.info("Check for related products on the iPhone product page")
        self.get_any_element(self.RP_PRODUCT)
        return self
