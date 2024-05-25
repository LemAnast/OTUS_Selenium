from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ShoppingCartPage(BasePage):
    PRODUCT_TABLE = By.CSS_SELECTOR, "#shopping-cart"

    def check_product_in_cart(self):
        assert self.get_element(self.PRODUCT_TABLE), "Корзина пустая"
        return self
