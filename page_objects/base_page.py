from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self, page_url):
        self.browser.get(self.browser.url + page_url)

    def check_title_text(self, title: str, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.title_is(title))

    def wait_url(self, page_url: str, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.url_contains(self.browser.url + page_url))

    def get_element(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def get_invisible_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def get_any_element(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_any_elements_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)
