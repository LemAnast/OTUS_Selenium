from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    ALERT_SUCCESS = By.CSS_SELECTOR, ".alert-success"
    CLOSE_BTN = By.CSS_SELECTOR, "#alert .btn-close"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.ALERT_SUCCESS))

    def check_alert_success_text(self):
        assert "Success: You have added" in self.alert.text, \
            "Текст оповещения некорректный"
        return self

    def close_alert(self):
        self.browser.find_element(*self.CLOSE_BTN).click()
        return self

    def check_alert_success_modified_product(self):
        assert "Success: You have modified products!" in self.alert.text, \
            "Текст оповещения некорректный"
        return self
