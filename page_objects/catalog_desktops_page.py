from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CatalogDesktopsPage(BasePage):
    PATH = "/en-gb/catalog/desktops"
    TITLE = By.CSS_SELECTOR, "head title"
    HEADER = By.CSS_SELECTOR, "#content h2"
    MENU_ITEM = By.CLASS_NAME, "list-group-item"
    PRODUCT_ITEM = By.CLASS_NAME, "product-thumb"
    BUTTON_LIST = By.ID, "button-list"
    LIST_VIEW = By.CLASS_NAME, "product-list"

    def open_catalog_desktops_page(self):
        self.open_page(self.PATH)
        return self

    def check_desktops_title(self):
        self.check_title_text("Desktops")
        return self

    def check_desktops_header(self):
        assert self.get_element(self.HEADER).text == "Desktops", \
            "Заголовок раздела Desktops не верен"
        return self

    def check_count_of_menu_items(self):
        menu_list = self.get_elements(self.MENU_ITEM)
        assert len(menu_list) == 10, \
            "Количество элементов в меню не верно"
        return self

    def click_menu_item(self, index):
        self.get_elements(self.MENU_ITEM)[index].click()
        return self

    def check_count_of_product_items(self):
        product_list = self.get_elements(self.PRODUCT_ITEM)
        assert len(product_list) == 1, \
            "Некорректное количество товаров в разделе"
        return self

    def activate_list_view(self):
        self.get_element(self.BUTTON_LIST).click()
        return self

    def check_list_view(self):
        assert self.get_element(self.LIST_VIEW), \
            "Представление в виде списка не работает"
        return self
