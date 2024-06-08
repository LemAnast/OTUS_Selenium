import datetime
import allure
import logging
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
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    yabinary = request.config.getoption("--yabinary")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

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

    browser.logger = logger
    browser.get(url)
    browser.url = url

    logger.info("Browser %s started" % browser)

    yield browser

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    def fin():
        browser.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
