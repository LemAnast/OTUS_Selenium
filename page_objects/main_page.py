import random
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

from page_objects.base_page import BasePage


class MainPage(BasePage):
    CART_DD = By.ID, "header-cart"
    CART_DD_TEXT = By.CSS_SELECTOR, "#header-cart li"
    CAROUSEL = By.CLASS_NAME, "carousel.slide"
    CAROUSEL_ITEM = By.CLASS_NAME, "carousel-item"
    PRODUCT_ITEM = By.CLASS_NAME, "product-thumb"
    PRODUCT_BTN = By.CSS_SELECTOR, "button[type='submit']"
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, ".product-thumb h4 a"
    ADD_TO_CART_BTN = By.CSS_SELECTOR, "button[type='submit']:nth-of-type(1)"
    PRODUCT_PRICE_NEW = By.CLASS_NAME, "price-new"
    PRODUCT_PRICE_TAX = By.CLASS_NAME, "price-tax"

    @allure.step("Кликнуть по дропдауну корзины")
    def click_cart_dropdown(self):
        self.logger.info("Click on Cart dropdown")
        self.click(self.CART_DD)
        return self

    @allure.step("Проверить текст в дропдауне пустой корзины")
    def check_empty_cart_dropdown_text(self):
        self.logger.info("Check the text in the dropdown of an empty cart")
        assert self.get_element(self.CART_DD_TEXT).text == "Your shopping cart is empty!", \
            "Некорректный текст при пустой корзине"
        return self

    @allure.step("Проверить количество баннеров в карусели")
    def check_carousel_items(self, index):
        self.logger.info("Check the number of banners in the carousel")
        carousel_list = self.get_invisible_elements(self.CAROUSEL)
        if index == 0:
            carousel_items = carousel_list[0].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 2, "Количество элементов в carousel_0 не равно 2"
        elif index == 1:
            carousel_items = carousel_list[1].find_elements(*self.CAROUSEL_ITEM)
            assert len(carousel_items) == 3, "Количество элементов в carousel_1 не равно 3"
        return self

    @allure.step("Проверить количество кнопок на карточках продуктов")
    def check_product_buttons(self):
        self.logger.info("Check the number of buttons on product cards")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            product_buttons = product_items[i].find_elements(*self.PRODUCT_BTN)
            assert len(product_buttons) == 3, f"Количество кнопок на {i} карточке продукта не равно 3"

    @allure.step("Кликнуть по карточке рекомендуемого продукта")
    def click_featured_product(self, index=0):
        self.logger.info("Click on the recommended product card")
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()
        return self

    @allure.step("Добавить в корзину рандомный продукт")
    def add_to_cart_random_product(self):
        self.logger.info("Add a random product to cart")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        i = random.randint(1, len(product_items))
        target_btn = self.get_element((By.CSS_SELECTOR,
                                       f"div.col.mb-3:nth-child({i}) button[type='submit']:nth-child(1)"))
        AC(self.browser).move_to_element(target_btn).click(target_btn).perform()
        return self

    @allure.step("Проверить отображение цены и налога в Евро")
    def check_prices_in_euro(self):
        self.logger.info("Check display of price and tax in Euro")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "€" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "Цена в евро отображается некорректно"
            assert "€" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "Налог цены в евро отображается некорректно"
        return self

    @allure.step("Проверить отображение цены и налога в Фунтах")
    def check_prices_in_pound(self):
        self.logger.info("Check display of price and tax in Pound")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "£" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "Цена в фунтах отображается некорректно"
            assert "£" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "Налог цены в фунтах отображается некорректно"
        return self

    @allure.step("Проверить отображение цены и налога в Долларах")
    def check_prices_in_dollar(self):
        self.logger.info("Check display of price and tax in Dollar")
        product_items = self.get_elements(self.PRODUCT_ITEM)
        for i in range(0, len(product_items)):
            assert "$" in product_items[i].find_element(*self.PRODUCT_PRICE_NEW).text, \
                "Цена в долларах отображается некорректно"
            assert "$" in product_items[i].find_element(*self.PRODUCT_PRICE_TAX).text, \
                "Налог цены в долларах отображается некорректно"
        return self
