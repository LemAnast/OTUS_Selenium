from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"

    def open_register_page(self):
        self.open_page(self.PATH)
        return self
