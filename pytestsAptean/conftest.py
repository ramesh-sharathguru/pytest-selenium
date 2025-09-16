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

driver, selected_browser, selected_device_type = (None, None, None)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser choice : chrome or firefox")
    parser.addoption( "--device_type", action="store", default="desktop", help="Device type available : mobile, tablet, laptop, desktop" )

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def device_type(request):
    return request.config.getoption("--device_type")

# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def all_tests_driver(browser, device_type):
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    global driver, selected_browser, selected_device_type
    selected_browser = browser
    selected_device_type = device_type

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=GeckoDriverManager().install())
    else:
        raise Exception("please choose between chrome or firefox")

    # devices = ['mobile','desktop',] #'tablet', 'laptop'
    # for device_type in devices:
    if device_type == 'mobile':
        driver.set_window_size(375, 867)
    elif device_type == 'tablet':
        driver.set_window_size(1138, 712)
    elif device_type == 'laptop':
        driver.set_window_size(1366, 768)
    elif device_type == 'desktop':
        driver.maximize_window()
        # screen_size = driver.get_window_size()

    driver.implicitly_wait(6)
    yield driver
    driver.quit()

# Use this hook to add environment info to the HTML report
def pytest_html_report_title(report):
    report.title = "QA Automation Test Report"

def pytest_html_results_table_header(cells):
    cells.insert(2, " Device ")
    cells.insert(3, " Browser ")
    cells.insert(2, selected_device_type)
    cells.insert(3, selected_browser)

# def pytest_html_results_table_row(report, cells):
#     # device = report.extra_device if hasattr(report, "extra_device") else "N/A"
#     # browser = report.extra_browser if hasattr(report, "extra_browser") else "N/A"
#     cells.insert(2, selected_device_type)
#     cells.insert(3, selected_browser)

# # Attach device/browser info to each test report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     global driver
#     outcome = yield
#     report = outcome.get_result()
#     report.extra_device = item.config.getoption("device")
#     report.extra_browser = item.config.getoption("browser")
#
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             screenshot_path = f"reports/screenshots/{item.name}.png"
#             driver.save_screenshot(screenshot_path)



