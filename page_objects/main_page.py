from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    CURRENCY_DD = By.ID, "form-currency"
    CURRENCY_ITEM = By.CSS_SELECTOR, "#form-currency li"
    CART_DD = By.ID, "header-cart"
    CART_DD_TEXT = By.CSS_SELECTOR, "#header-cart li"
    CAROUSEL = By.CLASS_NAME, "carousel.slide"
    CAROUSEL_ITEM = By.CLASS_NAME, "carousel-item"
    PRODUCT_ITEM = By.CLASS_NAME, "product-thumb"
    PRODUCT_BTN = By.CSS_SELECTOR, "button[type='submit']"
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, ".product-thumb h4 a"

    def click_currency_dropdown(self):
        self.get_element(self.CURRENCY_DD).click()
        return self

    def check_currency_list(self):
        currency_list = self.get_elements(self.CURRENCY_ITEM)
        assert len(currency_list) == 3, \
            "Количество валют в дропдауне не равно 3"
        return self

    def click_cart_dropdown(self):
        self.get_element(self.CART_DD).click()
        return self

    def check_empty_cart_dropdown_text(self):
        assert self.get_element(self.CART_DD_TEXT).text == "Your shopping cart is empty!", \
            "Некорректный текст при пустой корзине"
        return self

    def check_carousel_items(self, index):
        carousel_list = self.get_invisible_elements(self.CAROUSEL)
        if index == 0:
            carousel_items = carousel_list[0].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 2, "Количество элементов в carousel_0 не равно 2"
        elif index == 1:
            carousel_items = carousel_list[1].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 3, "Количество элементов в carousel_1 не равно 3"
        return self

    def check_product_buttons(self):
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            product_buttons = product_items[i].find_elements(*self.PRODUCT_BTN)
            assert len(product_buttons) == 3, f"Количество кнопок на {i} карточке продукта не равно 3"

    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()
        return  self
