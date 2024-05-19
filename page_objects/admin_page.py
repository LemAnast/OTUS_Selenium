from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/administration"
    CARD = By.CLASS_NAME, "card"
    HEADER = By.CLASS_NAME, "card-header"
    HEADER_ICON = By.CSS_SELECTOR, ".card-header i"
    INPUT = By.CSS_SELECTOR, ".mb-3 input"
    INPUT_LABEL = By.CSS_SELECTOR, ".mb-3 label"
    INPUT_ICON = By.CSS_SELECTOR, ".mb-3 i"
    LOGIN_BTN = By.CSS_SELECTOR, "button[type='submit']"
    LOGIN_INPUT = By.ID, "input-username"
    PASS_INPUT = By.ID, "input-password"
    LOGOUT_BTN = By.ID, "nav-logout"

    def open_admin_page(self):
        self.open_page(self.PATH)
        return self

    def wait_card(self):
        self.get_element(self.CARD)
        return self

    def check_header(self):
        self.get_element(self.HEADER_ICON)
        assert self.get_element(self.HEADER).text == "Please enter your login details.", \
            "Текст заголовка некорректный"

    def check_input_label(self, index=0):
        if index == 0:
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Username", \
                "Некорректная подпись поля Username"
        else:
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Password", \
                "Некорректная подпись поля Password"
        return self

    def check_input_icon(self, index=0):
        if index == 0:
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Отсутствует иконка поля Username"
        else:
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Отсутствует иконка поля Password"
        return self

    def check_input_placeholder(self, index=0):
        if index == 0:
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Username", \
                "Некорректный плейсхолдер поля Username"
        else:
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Password", \
                "Некорректный плейсхолдер поля Password"

    def check_login_button(self):
        assert self.get_element(self.LOGIN_BTN).text == "Login", \
            "Название кнопки Login некорректно"
        return self

    def submit_login_button(self):
        self.get_element(self.LOGIN_BTN).click()
        return self

    def login(self):
        self.input_value(self.LOGIN_INPUT, "user")
        self.input_value(self.PASS_INPUT, "bitnami")
        self.click(self.LOGIN_BTN)
        return self

    def wait_logged_in(self):
        self.wait_url("/administration/index.php?route=common/dashboard&user_token")
        self.check_title_text("Dashboard")
        return self

    def logout(self):
        self.click(self.LOGOUT_BTN)
        return self

    def wait_logged_out(self):
        self.wait_url("/administration/index.php?route=common/login")
        self.check_title_text("Administration")
        return self
