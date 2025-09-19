# run cmd : pytest -vs pytestsAptean/tests/test_discrete_solution.py  --html=reports/html-report[mobile].html --self-contained-html
import pytest
import time
import pytest_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest_assume

ALL_APTEAN_REGIONS = [{"url":"https://aptean-website-dev.azurewebsites.net/en-US/discrete-solution", "title": "en-US"},
                     {"url":"https://aptean-website-dev.azurewebsites.net/fr-CA/discrete-solution", "title": "fr-CA"},
                     {"url":"https://aptean-website-dev.azurewebsites.net/es-US/discrete-solution", "title": "es-US"},
                     {"url":"https://aptean-website-dev.azurewebsites.net/nl-NL/discrete-solution", "title": "nl-NL"},
                     {"url":"https://aptean-website-dev.azurewebsites.net/de-DE/discrete-solution", "title": "de-DE"},]

@pytest.mark.parametrize("region", ALL_APTEAN_REGIONS)
def test_page_title(all_tests_driver, region, request):
    all_tests_driver.get(region["url"])
    assert "Discrete Manufacturing Solution" in all_tests_driver.title
    description = "<p>Page title is : 'Discrete Manufacturing Solution' - Verified..!!  </p>"
    request.node.add_report_section("cell", "description", description)


@pytest.mark.skip(reason="This test is currently under development.") # ignore the below test for now
@pytest.mark.parametrize("region", ALL_APTEAN_REGIONS)
def test_header_visibility(all_tests_driver, region):
    driver = all_tests_driver
    # new_region = NEW_TARGET_URL.replace('en-US', region)
    time.sleep(2)
    driver.get(region["url"])

    WebDriverWait(driver, 30).until(lambda d: d.execute_script(" return document.readyState") == "complete")

    scroll_amount = 600  # Number of pixels per scroll
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(2)
        new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
        total_height = driver.execute_script("return document.body.scrollHeight;")
        if new_height >= total_height:
            break
    #1. Title Check
    pytest.assume(driver.title == "Discrete Manufacturing Solution", f"Title mismatch for region {region['url']}")
    # Header visibility
    try:
        header = driver.find_element(By.TAG_NAME, "h1")
        pytest.assume(header.is_displayed(), f"Header not visible for region {region['url']}")
    except Exception:
        pytest.assume(False, f"Header not visible for region {region['url']}")



