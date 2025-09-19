# my conftest
import time
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options  import Options

# html report generate library

import datetime
import platform
import os
from py.xml import html

driver, selected_browser, selected_device_type = (None, None, None)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser choice : chrome or firefox")
    parser.addoption( "--device_type", action="store", default="desktop", help="Device type available : mobile, tablet, laptop, desktop" )

@pytest.fixture(scope="session")
def browser(request):
    global selected_browser
    selected_browser = request.config.getoption("--browser")
    return selected_browser

@pytest.fixture(scope="session")
def device_type(request):
    global selected_device_type
    selected_device_type = request.config.getoption("--device_type")
    return selected_device_type

# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def all_tests_driver(browser, device_type):
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--remote-debugging-port=9222")
    # chrome_options.add_argument("--headless")  # optional: run headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    global driver, selected_browser, selected_device_type

    selected_browser = browser
    selected_device_type = device_type

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=GeckoDriverManager().install())
    else:
        raise Exception("please choose between only available browser's : chrome or firefox")

    driver.maximize_window()
    driver.implicitly_wait(6)
    yield driver
    driver.quit()

#HTML report modifications ------------

def pytest_html_report_title(report):
    """Customize the HTML report title"""
    report.title = "QA Automation Test Report"

def pytest_html_results_table_header(cells):
    """Customize table headers"""
    metadata_block = html.div(
        html.ul([
            html.li(html.b('Project: QA Testing - Campaign Page \'s ')) ,
            html.p(html.i("'UI/UX Validatation' and 'Responsive Design Testing'")),
            html.li(html.b('Tester : aptean QA ')) ,
            html.li(html.b('Environment: dev ')),
            html.li(html.b(f'Browser: {selected_browser}')),
            html.li(html.b(f'Device Type : {selected_device_type}')),
            html.li(html.b(f'Platform : {platform.platform()}')),
            html.li(html.b(f'Python Version : {platform.python_version()}')),
            html.li(html.b(f'Execution Time : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')),
        ]) )
    cells.insert(2, metadata_block)


# end of HTML report modifications ------------

