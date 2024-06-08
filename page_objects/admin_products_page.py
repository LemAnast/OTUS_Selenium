import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminProductsPage(BasePage):
    MENU_CATALOG = By.ID, "menu-catalog"
    MENU_PRODUCTS = By.CSS_SELECTOR, "#collapse-1 li:nth-child(2)"
    ADD_NEW_PRODUCT = By.CSS_SELECTOR, "i[class='fa-solid fa-plus']"
    FILTER_PRODUCT_NAME = By.CSS_SELECTOR, "input[name='filter_name']"
    FILTER_BTN = By.ID, "button-filter"
    CHECKBOX_PRODUCT = By.CSS_SELECTOR, "table > tbody > tr > td:nth-child(1) > input"
    DELETE_BTN = By.CSS_SELECTOR, "i[class='fa-regular fa-trash-can']"

    @allure.step("Открыть раздел меню Продукты")
    def open_products_section(self):
        self.logger.info("Open Products section of menu")
        self.click(self.MENU_CATALOG)
        self.click(self.MENU_PRODUCTS)
        return self

    @allure.step("Кликнуть по кнопке добавления нового продукта")
    def click_add_new_product(self):
        self.logger.info("Click on the add new product button")
        self.click(self.ADD_NEW_PRODUCT)
        return self

    @allure.step("Ввести 'Test Product' в поле фильтра Product Name")
    def fill_filter_by_product_name(self):
        self.logger.info("Input 'Test Product' in the Product Name filter field")
        self.input_value(self.FILTER_PRODUCT_NAME, "Test Product")
        return self

    @allure.step("Кликнуть по кнопке Filter")
    def click_filter_button(self):
        self.logger.info("Click on the Filter button")
        self.click(self.FILTER_BTN)
        return self

    @allure.step("Кликнуть по чекбоксу выбора продукта")
    def click_checkbox_product(self):
        self.logger.info("Click on the product selection checkbox")
        self.click(self.CHECKBOX_PRODUCT)
        return self

    @allure.step("Кликнуть по кнопке Delete")
    def click_delete_button(self):
        self.logger.info("Click on the Delete button")
        self.click(self.DELETE_BTN)
        return self

    @allure.step("Кликнуть по кнопке подтверждения удаления продукта")
    def submit_deleting_product(self):
        self.logger.info("Click on the product removal confirmation button")
        alert_obj = self.browser.switch_to.alert
        alert_obj.accept()
        return self
