# my conftest
import sys
import os
import time
import pytest
import datetime
import platform
import requests

# html report generate library
from py.xml import html
import pytest_html

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pytestsAptean.pages.base import step_tracker

driver, selected_browser, selected_device_type, wait_time = (None, None, None,None)

def pytest_addoption(parser):
    parser.addoption("--browser_pytest", action="store", default="chrome", help="Browser choice : chrome or firefox")
    parser.addoption( "--device_type", action="store", default="desktop", help="Device type available : mobile, tablet, laptop, desktop" )
    parser.addoption("--wait_time", action="store", default="5", help="Time to wait for browser to open")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

@pytest.fixture(scope="session")
def browser(request):
    global selected_browser
    step_tracker.step_number = 0
    step_tracker.all_steps = []
    selected_browser = request.config.getoption("--browser_pytest")
    step_tracker.add_step("Starting browser", f"Setting up {selected_browser}")

    return selected_browser

@pytest.fixture(scope="session")
def device_type(request):
    global selected_device_type
    selected_device_type = request.config.getoption("--device_type")
    step_tracker.add_step("Selected device", f"Setting up '{selected_device_type}' screen ")
    return selected_device_type

@pytest.fixture(scope="session")
def browser_wait_time(request):
    global wait_time
    wait_time = int(request.config.getoption("--wait_time"))
    step_tracker.add_step("Selected sleep time", f"Wait time between step {selected_device_type} sec")
    return wait_time

# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def all_tests_driver(browser, device_type):
    global driver, selected_browser, selected_device_type
    selected_browser = browser
    selected_device_type = device_type


    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions

    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()
    try:
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        else:
            raise Exception("please choose between only available browser's : chrome or firefox")
        driver.maximize_window()
        driver.implicitly_wait(6)

        step_tracker.add_step("Browser ready", f"{selected_browser} is open and ready")
        yield driver

        # driver.quit()

    except WebDriverException as e:
        print("WebDriver Exception occurred ")
        sys.exit(1)

    except Exception as e:
        print("Exception occurred ")
        sys.exit(1)

    finally:
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        driver.quit()

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


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Custom summary line added here.")])

# HTML modification's --------------------------
