import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ch", "ya", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--yadriver", action="store_true",
        default="C:/Users/79515/Downloads/yandexdriver-24.1.0.2570-win64/yandexdriver.exe"
    )
    parser.addoption(
        "--yabinary", action="store_true",
        default="C:/Users/79515/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
    )
    parser.addoption("--url", action="store", default="http://192.168.0.106:8081")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    yabinary = request.config.getoption("--yabinary")
    url = request.config.getoption("--url")

    if browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService(), options=options)
    elif browser_name == "ya":
        options = Options()
        options.binary_location = yabinary
        if headless_mode:
            options.add_argument("headless=new")
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(options=options, service=service)

    browser.maximize_window()

    request.addfinalizer(browser.close)

    browser.get(url)
    browser.url = url

    return browser
