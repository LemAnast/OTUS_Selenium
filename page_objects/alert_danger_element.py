import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertDangerElement:
    ALERT_DANGER = By.CSS_SELECTOR, ".alert-danger"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.ALERT_DANGER))
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Проверить текст в danger alert")
    def check_alert_danger_text(self):
        self.logger.info("Check text in danger alert")
        assert self.alert.text == "No match for Username and/or Password.", \
            "Текст оповещения некорректный"
