from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page_header(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".card-header i")), message="Отсутствует иконка заголовка")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "card-header"), "Please enter your login details."),
        message="Заголовок некорректный")


def test_admin_page_username_input(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "label[for='input-username']"), "Username"),
        message="Некорректная подпись Username")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".mb-3:nth-child(1) .input-group-text i")), message="Отсутствует иконка Username")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.ID, "input-username")), message="Отсутствует инпут Username")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element_attribute(
        (By.ID, "input-username"), "placeholder", "Username"),
        message="Некорректный плейсхолдер Username")


def test_admin_page_password_input(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "label[for='input-password']"), "Password"),
        message="Некорректная подпись Password")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".mb-3:nth-child(2) .input-group-text i")), message="Отсутствует иконка Password")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.ID, "input-password")), message="Отсутствует инпут Password")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element_attribute(
        (By.ID, "input-password"), "placeholder", "Password"),
        message="Некорректный плейсхолдер Password")


def test_admin_page_login_button(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")), message="Отсутствует кнопка Login")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "button[type='submit']"), "Login"),
        message="Название кнопки Login некорректно")


def test_admin_page_alert(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "alert-dismissible"), "No match for Username and/or Password."),
        message="Текст оповещения некорректный")
