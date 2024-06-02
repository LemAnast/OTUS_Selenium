import allure

from page_objects.admin_page import AdminPage
from page_objects.alert_danger_element import AlertDangerElement


@allure.feature("Admin page")
@allure.title("Проверка хэдера в карточке авторизации админ панели")
def test_admin_page_header(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_header()


@allure.feature("Admin page")
@allure.title("Проверка поля имени пользователя в карточке авторизации админ панели")
def test_admin_page_username_input(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_input_label(0) \
        .check_input_icon(0) \
        .check_input_placeholder(0)


@allure.feature("Admin page")
@allure.title("Проверка поля пароля пользователя в карточке авторизации админ панели")
def test_admin_page_password_input(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_input_label(1) \
        .check_input_icon(1) \
        .check_input_placeholder(1)


@allure.feature("Admin page")
@allure.title("Проверка кнопки логина в карточке авторизации админ панели")
def test_admin_page_login_button(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .check_login_button()


@allure.feature("Admin page")
@allure.title("Проверка алерта при незаполненных полях в карточке авторизации админ панели")
def test_admin_page_alert(browser):
    AdminPage(browser) \
        .open_admin_page() \
        .wait_card() \
        .submit_login_button()
    AlertDangerElement(browser).check_alert_danger_text()
