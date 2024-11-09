import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
import mysql.connector


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--yad", default="/Users/user/drivers/yandexdriver")
    parser.addoption("--base_url", default="http://192.168.0.110:8081/")
    parser.addoption("--drivers", default=os.path.expanduser("/Users/user/drivers/yandexdriver"))
    parser.addoption("--admin_login", default='user')
    parser.addoption("--admin_password", default='bitnami')


@pytest.fixture
def admin_login(request):
    return request.config.getoption("--admin_login")


@pytest.fixture
def admin_password(request):
    return request.config.getoption("--admin_password")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    yad = pytestconfig.getoption("yad")
    driver = None

    if browser_name in ["cr", "chrome"]:
        driver = webdriver.Chrome()
    elif browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()
    elif browser_name in ["ya", "yandex"]:
        options = ChromeOptions()
        options.binary_location = "/Applications/Yandex.app"
        driver = webdriver.Chrome(options=options, service=Service(executable_path=yad))
    yield driver
    driver.quit()










