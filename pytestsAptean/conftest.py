import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options  import Options

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser choice : chrome or firefox")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def general_driver(browser):
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    global driver
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=GeckoDriverManager().install())
    else:
        raise Exception("please choose between chrome or firefox")

    time.sleep(6)
    yield driver

    driver.quit()




