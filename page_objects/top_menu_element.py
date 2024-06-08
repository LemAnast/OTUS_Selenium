import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC


class TopMenu:
    CURRENCY_DD = By.ID, "form-currency"
    CURRENCY_ITEM = By.CSS_SELECTOR, "#form-currency li"
    EURO = By.CSS_SELECTOR, "a[href='EUR']"
    POUND = By.CSS_SELECTOR, "a[href='GBP']"
    DOLLAR = By.CSS_SELECTOR, "a[href='USD']"
    SHOPPING_CART = By.CSS_SELECTOR, "a[title='Shopping Cart']"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Кликнуть по ссылке Shopping cart")
    def click_shopping_cart_link(self):
        self.logger.info("Click on the Shopping cart link")
        cart_link = self.browser.find_element(*self.SHOPPING_CART)
        AC(self.browser).move_to_element(cart_link).click(cart_link).perform()
        return self

    @allure.step("Кликнуть по дропдауну Currency")
    def click_currency_dropdown(self):
        self.logger.info("Click on Currency dropdown")
        self.browser.find_element(*self.CURRENCY_DD).click()
        return self

    @allure.step("Проверить количество валют в дропдауне Currency")
    def check_currency_list(self):
        self.logger.info("Check the number of currencies in the Currency dropdown")
        currency_list = self.browser.find_elements(*self.CURRENCY_ITEM)
        assert len(currency_list) == 3, \
            "Количество валют в дропдауне не равно 3"
        return self

    @allure.step("Кликнуть по валюте Евро")
    def select_euro_currency(self):
        self.logger.info("Click on Euro currency")
        self.browser.find_element(*self.EURO).click()
        return self

    @allure.step("Кликнуть по валюте Фунт")
    def select_pound_currency(self):
        self.logger.info("Click on Pound currency")
        self.browser.find_element(*self.POUND).click()
        return self

    @allure.step("Кликнуть по валюте Доллар")
    def select_dollar_currency(self):
        self.logger.info("Click on Dollar currency")
        self.browser.find_element(*self.DOLLAR).click()
        return self
