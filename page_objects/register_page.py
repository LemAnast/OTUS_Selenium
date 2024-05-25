from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    RC_MENU_ITEM = By.CLASS_NAME, "list-group-item"
    TITLE_PD = By.CSS_SELECTOR, "#account legend"
    TITLE_PASS = By.CSS_SELECTOR, "fieldset:nth-child(2) legend"
    TITLE_NL = By.CSS_SELECTOR, "fieldset:nth-child(3) legend"
    CBOX_NL = By.ID, "input-newsletter"
    LABEL_LOGIN_LINK = By.CSS_SELECTOR, "#content p"
    LOGIN_LINK = By.CSS_SELECTOR, "#content p a"
    PASS_INPUT = By.ID, "input-password"
    SUBMIT_BTN = By.CSS_SELECTOR, "button[type='submit']"
    PASS_VALID = By.ID, "error-password"
    FIRST_NAME_INPUT = By.ID, "input-firstname"
    LAST_NAME_INPUT = By.ID, "input-lastname"
    EMAIL_INPUT = By.ID, "input-email"
    CBOX_AGREEMENT = By.CSS_SELECTOR, "input[name='agree']"
    H1_SUCCESS_REG = By.CSS_SELECTOR, "#content h1"

    def open_register_page(self):
        self.open_page(self.PATH)
        return self

    def check_right_column_menu_items(self):
        menu_items = self.get_elements(self.RC_MENU_ITEM)
        assert len(menu_items) == 13, \
            "Некорректное количество элементов в боковом меню"
        return self

    def check_fieldset_titles(self):
        assert self.get_element(self.TITLE_PD).text == "Your Personal Details", \
            "Заголовок блока персональной информации не верен"
        assert self.get_element(self.TITLE_PASS).text == "Your Password", \
            "Заголовок блока пароля не верен"
        assert self.get_element(self.TITLE_NL).text == "Newsletter", \
            "Заголовок блока рассылки не верен"
        return self

    def click_newsletter_checkbox(self):
        self.click(self.CBOX_NL)
        return self

    def check_active_newsletter_checkbox(self):
        assert self.get_element(self.CBOX_NL).is_selected(), \
            "Чекбокс не активировался после нажатия"
        return self

    def check_text_to_login_page(self):
        assert (self.get_element(self.LABEL_LOGIN_LINK).text ==
                "If you already have an account with us, please login at the login page."), \
            "Текст не верен"
        return self

    def click_link_to_login_page(self):
        self.click(self.LOGIN_LINK)
        return self

    def enter_invalid_password(self):
        self.input_value(self.PASS_INPUT, "123")
        return self

    def click_submit_button(self):
        self.click(self.SUBMIT_BTN)
        return self

    def check_password_validation(self):
        assert self.get_element(self.PASS_VALID).text == "Password must be between 4 and 20 characters!", \
            "Текст валидации пароля не верен"
        return self

    def fill_your_personal_details_inputs(self):
        self.input_value(self.FIRST_NAME_INPUT, "Will")
        self.input_value(self.LAST_NAME_INPUT, "Smith")
        self.input_value(self.EMAIL_INPUT, "Smith123@mail.com")
        return self

    def enter_valid_password(self):
        self.input_value(self.PASS_INPUT, "123Smith")
        return self

    def click_agreement_checkbox(self):
        self.click(self.CBOX_AGREEMENT)
        return self

    def wait_success_registration(self):
        self.wait_url("/en-gb?route=account/success&customer_token")
        self.check_title_text("Your Account Has Been Created!")
        assert self.get_element(self.H1_SUCCESS_REG).text == "Your Account Has Been Created!"
