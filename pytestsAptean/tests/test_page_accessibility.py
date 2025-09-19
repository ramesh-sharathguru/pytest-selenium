import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
from selenium.webdriver.common.by import By

CAMPAIN_PAGE_URL = "https://aptean-website-dev.azurewebsites.net/en-US/cp/tms"


APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']

# @pytest.mark.skip(reason="This test is currently under development.") # ignore the below test for now
def test_multi_screen_accessibility(all_tests_driver):
    driver = all_tests_driver

    driver.get(CAMPAIN_PAGE_URL)

    driver.implicitly_wait(10)

    body_ele = driver.find_element(By.TAG_NAME, "body")
    os.makedirs("screenshots", exist_ok=True)
    filename = os.path.join("screenshots", f"body_screenshot_{int(time.time())}.png")
    body_ele.screenshot(filename)

    axe = Axe(driver)
    # Inject axe-core script into the page
    axe.inject()

    #run accessibility scan and get the results
    results = axe.run()

    #check for violations
    if results['violations']:
        print(" Accessibilty violation found..!! ")
        for violation in results['violations']:
            print("-:-:"*10)
            print(f"violation : {violation['help']}")
            print(f"Impact : {violation['impact']}")
            print("Elements affected : ")
            for node in violation['nodes']:
                print(f" - {node['html']}")
    else:
        print("No violations found")

