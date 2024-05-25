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

    def fill_product_name(self):
        self.input_value(self.PRODUCT_NAME, "Test Product")
        return self

    def fill_meta_tag_title(self):
        self.input_value(self.META_TAG_TITLE, "Test Product Tag")
        return self

    def open_data_tab(self):
        self.click(self.DATA)
        return self

    def fill_model(self):
        self.input_value(self.MODEL, "Test Model")
        return self

    def open_seo_tab(self):
        self.click(self.SEO)
        return self

    def fill_seo_keyword(self):
        self.input_value(self.KEYWORD, "test-product")
        return self

    def click_save_product(self):
        self.click(self.SAVE_PRODUCT_BTN)
        return self
