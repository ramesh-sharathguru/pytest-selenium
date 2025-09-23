# my conftest
import sys
import time
import pytest
import pytest_html
from selenium import webdriver
from selenium.common import WebDriverException
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

driver, selected_browser, selected_device_type,wait_time = (None, None, None,None)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser choice : chrome or firefox")
    parser.addoption( "--device_type", action="store", default="desktop", help="Device type available : mobile, tablet, laptop, desktop" )
    parser.addoption("--wait_time", action="store", default="5", help="Time to wait for browser to open")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

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

@pytest.fixture(scope="session")
def wait_time(request):
    global wait_time
    wait_time = int(request.config.getoption("--wait_time"))
    return wait_time

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

    try:
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

    except WebDriverException as e:
        print("WebDriver Exception occurred ")
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        sys.exit(1)

    except Exception as e:
        print("Exception occurred ")
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        sys.exit(1)


#HTML report modifications ------------

def pytest_html_report_title(report):
    """Customize the HTML report title"""
    report.title = "QA Automation Test Report"

def pytest_html_results_table_header(cells):
    """Customize table headers"""
    cells.append(html.th("Custom Info"))
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
#
# def pytest_html_results_table_row(report, cells):
#     info = "✅" if report.passed else "❌"
#     cells.append(html.td(info))

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Custom summary line added here.")])

# HTML modification's --------------------------
