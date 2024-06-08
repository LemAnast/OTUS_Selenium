import allure
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

    @allure.step("Открыть страницу админки")
    def open_admin_page(self):
        self.logger.info("Open admin page")
        self.open_page(self.PATH)
        return self

    @allure.step("Подождать элемент карточки логина в админку")
    def wait_card(self):
        self.logger.info("Wait for the login card element in the admin page")
        self.get_element(self.CARD)
        return self

    @allure.step("Проверить отображение хэдера")
    def check_header(self):
        self.logger.info("Check header display")
        self.get_element(self.HEADER_ICON)
        assert self.get_element(self.HEADER).text == "Please enter your login details.", \
            "Текст заголовка некорректный"

    @allure.step("Проверить лейбл инпута")
    def check_input_label(self, index=0):
        if index == 0:
            self.logger.info("Check label of Username input")
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Username", \
                "Некорректная подпись поля Username"
        else:
            self.logger.info("Check label of Password input")
            assert self.get_elements(self.INPUT_LABEL)[index].text == "Password", \
                "Некорректная подпись поля Password"
        return self

    @allure.step("Проверить иконку инпута")
    def check_input_icon(self, index=0):
        if index == 0:
            self.logger.info("Check icon of Username input")
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Отсутствует иконка поля Username"
        else:
            self.logger.info("Check icon of Password input")
            assert self.get_elements(self.INPUT_ICON)[index], \
                "Отсутствует иконка поля Password"
        return self

    @allure.step("Проверить плейсхолдер инпута")
    def check_input_placeholder(self, index=0):
        if index == 0:
            self.logger.info("Check placeholder of Username input")
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Username", \
                "Некорректный плейсхолдер поля Username"
        else:
            self.logger.info("Check placeholder of Password input")
            assert self.get_elements(self.INPUT)[index].get_attribute("placeholder") == "Password", \
                "Некорректный плейсхолдер поля Password"

    @allure.step("Проверить отображение кнопки Login")
    def check_login_button(self):
        self.logger.info("Check the display of the Login button")
        assert self.get_element(self.LOGIN_BTN).text == "Login", \
            "Название кнопки Login некорректно"
        return self

    @allure.step("Кликнуть по кнопке Login")
    def submit_login_button(self):
        self.logger.info("Click on the Login button")
        self.click(self.LOGIN_BTN)
        return self

    @allure.step("Залогиниться в админ панель")
    def login(self):
        self.logger.info("Login to the admin panel")
        self.input_value(self.LOGIN_INPUT, "user")
        self.input_value(self.PASS_INPUT, "bitnami")
        self.click(self.LOGIN_BTN)
        return self

    @allure.step("Проверить успешность логина")
    def wait_logged_in(self):
        self.logger.info("Check login success")
        self.wait_url("/administration/index.php?route=common/dashboard&user_token")
        self.check_title_text("Dashboard")
        return self

    @allure.step("Разлогиниться в админ панели")
    def logout(self):
        self.logger.info("Logout from the admin panel")
        self.click(self.LOGOUT_BTN)
        return self

    @allure.step("Проверить успешность разлогина")
    def wait_logged_out(self):
        self.logger.info("Check logout success")
        self.wait_url("/administration/index.php?route=common/login")
        self.check_title_text("Administration")
        return self
