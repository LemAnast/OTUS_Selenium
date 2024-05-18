from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_page_menu_items(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    menu_items = WebDriverWait(browser, 1).until(EC.visibility_of_all_elements_located(
        (By.CLASS_NAME, "list-group-item"))
    )
    assert len(menu_items) == 13, "Некорректное количество элементов в боковом меню"


def test_register_page_fieldset_titles(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#account legend"), "Your Personal Details"),
        message="Заголовок блока персональной информации не верен"
    )
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "fieldset:nth-child(2) legend"), "Your Password"),
        message="Заголовок блока пароля не верен"
    )
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "fieldset:nth-child(3) legend"), "Newsletter"),
        message="Заголовок блока рассылки не верен"
    )


def test_register_page_subscribe_checkbox(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    assert not browser.find_element(By.ID, "input-newsletter").is_selected(), \
        "Чекбокс по умолчанию должен быть не активен"
    browser.find_element(By.ID, "input-newsletter").click()
    assert browser.find_element(By.ID, "input-newsletter").is_selected(), \
        "Чекбокс не активировался после нажатия"


def test_register_page_go_to_login_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#content p"),
        "If you already have an account with us, please login at the "),
        message="Текст не верен")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content p a"))).click()
    WebDriverWait(browser, 2).until(EC.url_to_be(
        browser.url + "/en-gb?route=account/login"), message="URL не верен")


def test_register_page_fill_invalid_password(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.ID, "input-password").send_keys("1")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.ID, "error-password")),
        message="Валидация пароля отсутствует"
    )
    WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element(
        (By.ID, "error-password"),
        "Password must be between 4 and 20 characters!"),
        message="Текст валидации пароля не верен"
    )
