import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

NEW_TARGET_URL = "https://aptean-website-dev.azurewebsites.net/en-US/discrete-solution"
APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']


def test_multi_device_screens(all_tests_driver):
    driver = all_tests_driver

    for region in APTEAN_REGION:
        new_region = NEW_TARGET_URL.replace('en-US', region)
        time.sleep(2)
        driver.get(new_region)
        WebDriverWait(driver, 30).until(lambda d: d.execute_script(" return document.readyState") == "complete")

        scroll_amount = 1000  # Number of pixels per scroll
        while True:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(2)
            new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
            total_height = driver.execute_script("return document.body.scrollHeight;")
            if new_height >= total_height:
                break

        header = driver.find_element(By.TAG_NAME, "h1")
        assert header.is_displayed()
