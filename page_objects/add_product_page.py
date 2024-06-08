import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AddProductPage(BasePage):
    PRODUCT_NAME = By.CSS_SELECTOR, "input[name='product_description[1][name]']"
    META_TAG_TITLE = By.CSS_SELECTOR, "input[name='product_description[1][meta_title]']"
    DATA = By.LINK_TEXT, "Data"
    MODEL = By.CSS_SELECTOR, "input[name='model']"
    SEO = By.LINK_TEXT, "SEO"
    KEYWORD = By.CSS_SELECTOR, "input[name='product_seo_url[0][1]']"
    SAVE_PRODUCT_BTN = By.CSS_SELECTOR, "i[class='fa-solid fa-floppy-disk']"

    @allure.step("Ввести 'Test Product' в поле Product Name")
    def fill_product_name(self):
        self.logger.info("Input 'Test Product' in the Product Name field")
        self.input_value(self.PRODUCT_NAME, "Test Product")
        return self

    @allure.step("Ввести 'Test Product Tag' в поле Meta Tag Title")
    def fill_meta_tag_title(self):
        self.logger.info("Input 'Test Product Tag' in the Meta Tag Title field")
        self.input_value(self.META_TAG_TITLE, "Test Product Tag")
        return self

    @allure.step("Кликнуть по вкладке Data")
    def open_data_tab(self):
        self.logger.info("Click on the Data tab")
        self.click(self.DATA)
        return self

    @allure.step("Ввести 'Test Model' в поле Model")
    def fill_model(self):
        self.logger.info("Input 'Test Model' in the Model field")
        self.input_value(self.MODEL, "Test Model")
        return self

    @allure.step("Кликнуть по вкладке SEO")
    def open_seo_tab(self):
        self.logger.info("Click on the SEO tab")
        self.click(self.SEO)
        return self

    @allure.step("Ввести 'test-product' в поле Keyword")
    def fill_seo_keyword(self):
        self.logger.info("Input 'test-product' in the Keyword field")
        self.input_value(self.KEYWORD, "test-product")
        return self

    @allure.step("Кликнуть по кнопке Save")
    def click_save_product(self):
        self.logger.info("Click on the Save button")
        self.click(self.SAVE_PRODUCT_BTN)
        return self
