import datetime
import allure
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--launch_mode", default="remote", choices=["remote", "local"]
    )
    parser.addoption(
        "--browser_local", default="ch", choices=["ch", "ya", "ff"]
    )
    parser.addoption(
        "--browser_remote", default="chrome", choices=["chrome", "firefox", "safari"]
    )
    parser.addoption("--bv_remote", action="store", default="125.0")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--executor", action="store", default="127.0.0.1")
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
    parser.addoption("--url", action="store", default="http://192.168.0.102:8081")
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
    launch_mode = request.config.getoption("--launch_mode")
    browser_local = request.config.getoption("--browser_local")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    yabinary = request.config.getoption("--yabinary")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    browser_remote = request.config.getoption("--browser_remote")
    bv_remote = request.config.getoption("--bv_remote")
    vnc = request.config.getoption("--vnc")
    executor = request.config.getoption("--executor")
    executor_url = f"http://{executor}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_remote == "chrome":
        options_remote = ChromeOptions()
    elif browser_remote == "firefox":
        options_remote = FFOptions()
    elif browser_remote == "saf":
        options_remote = ChromeOptions()

    caps = {
        "browserName": browser_remote,
        "browserVersion": bv_remote,
        "selenoid:options": {
             "enableVNC": vnc
        }
    }

    for k, v in caps.items():
        options_remote.set_capability(k, v)

    if launch_mode == "local":
        if browser_local == "ch":
            options = ChromeOptions()
            if headless_mode:
                options.add_argument("headless=new")
            browser = webdriver.Chrome(service=ChromeService(), options=options)
        elif browser_local == "ff":
            options = FFOptions()
            if headless_mode:
                options.add_argument("--headless")
            browser = webdriver.Firefox(service=FFService(), options=options)
        elif browser_local == "ya":
            options = ChromeOptions()
            options.binary_location = yabinary
            if headless_mode:
                options.add_argument("headless=new")
            service = ChromeService(executable_path=yadriver)
            browser = webdriver.Chrome(options=options, service=service)
    elif launch_mode == "remote":
        browser = webdriver.Remote(
            command_executor=executor_url,
            options=options_remote
        )

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
