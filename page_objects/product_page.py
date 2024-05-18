from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    PATH = "/en-gb/product/iphone"

    def open_product_page(self):
        self.open_page(self.PATH)
        return self
