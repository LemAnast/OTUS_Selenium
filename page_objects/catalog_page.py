from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/en-gb/catalog/desktops"

    def open_catalog_page(self):
        self.open_page(self.PATH)
        return self
