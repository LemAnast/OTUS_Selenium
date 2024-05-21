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

    def click_shopping_cart_link(self):
        cart_link = self.browser.find_element(*self.SHOPPING_CART)
        AC(self.browser).move_to_element(cart_link).click(cart_link).perform()
        return self

    def click_currency_dropdown(self):
        self.browser.find_element(*self.CURRENCY_DD).click()
        return self

    def check_currency_list(self):
        currency_list = self.browser.find_element(*self.CURRENCY_ITEM)
        assert len(currency_list) == 3, \
            "Количество валют в дропдауне не равно 3"
        return self

    def select_euro_currency(self):
        self.browser.find_element(*self.EURO).click()
        return self

    def select_pound_currency(self):
        self.browser.find_element(*self.POUND).click()
        return self

    def select_dollar_currency(self):
        self.browser.find_element(*self.DOLLAR).click()
        return self
