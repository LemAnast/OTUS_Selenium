import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ShoppingCartPage(BasePage):
    PRODUCT_TABLE = By.CSS_SELECTOR, "#shopping-cart"

    @allure.step("Проверить отсутствие продуктов в корзине")
    def check_product_in_cart(self):
        self.logger.info("Check if there are no products in the cart")
        assert self.get_element(self.PRODUCT_TABLE), "Корзина пустая"
        return self
