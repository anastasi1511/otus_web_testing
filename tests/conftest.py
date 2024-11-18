import datetime
import logging
import os.path
import json

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--yad", default="/Users/user/drivers/yandexdriver")
    parser.addoption("--base_url", default="http://192.168.0.106:8081/")
    parser.addoption("--drivers", default=os.path.expanduser("/Users/user/drivers/yandexdriver"))
    parser.addoption("--admin_login", default='user')
    parser.addoption("--admin_password", default='bitnami')
    parser.addoption("--log_level", action='store', default='INFO')


@pytest.fixture
def admin_login(request):
    return request.config.getoption("--admin_login")


@pytest.fixture
def admin_password(request):
    return request.config.getoption("--admin_password")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
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
    log_level = request.config.getoption("--log_level")
    yad = request.config.getoption("--yad")
    driver = None

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter('%(levelname)s:%(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test %s started at %s' % (request.node.name, datetime.datetime.now()))

    if browser_name in ["cr", "chrome"]:
        driver = webdriver.Chrome()
    elif browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()
    elif browser_name in ["ya", "yandex"]:
        options = ChromeOptions()
        options.binary_location = "/Applications/Yandex.app"
        driver = webdriver.Chrome(options=options, service=Service(executable_path=yad))

        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities, ensure_ascii=False),
            attachment_type=allure.attachment_type.JSON
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info('Browser %s started' % browser)

    def fin():
        driver.quit()
        logger.info('===> Test %s finished at %s' % (request.node.name, datetime.datetime.now()))

    yield driver
    request.addfinalizer(fin)

    if request.node.status == 'failed':
        allure.attach(
            name='failure_screenshot',
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG)
        allure.attach(
            name='page_source',
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML)











