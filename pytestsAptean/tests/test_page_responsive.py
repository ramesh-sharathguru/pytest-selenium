"""
For any web-page with responsiveness : use this script.
This file will only test for website 'url' responsiveness on different screens with different region
can do to fetch url from command line, (like option) - for now URL is hard coded
"""

import math
import os
import pytest
import time
import base64
from datetime import datetime
from PIL import Image
from io import BytesIO

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from pytestsAptean.tests.test_page_accessibility import AUTHOR_PAGE

DISCRETE_SOLUTION_URL = "https://aptean-website-dev.azurewebsites.net/en-US/discrete-solution"
#development URL : https://aptean-website-dev.azurewebsites.net/en-US/cp/tms
#production URL : https://www.aptean.com/en-US/cp/tms
CAMPAIN_PAGE_URL = "https://aptean-website-dev.azurewebsites.net/en-US/cp/tms"

AUTHOR_PAGE = "https://aptean-website-dev.azurewebsites.net/en-US/author/jack"

APTEAN_REGION = ['en-US', 'fr-CA','es-US', 'nl-NL', 'de-DE']

DEVICE_TYPE = {
    "tablet":[1138, 712],
    "laptop":[1366,768],
    "mobile":[375,767],
}

# @pytest.mark.parametrize("selected_device", "selected_dimension",DEVICE_TYPE.items())
def test_multi_device_screens(all_tests_driver):
    driver = all_tests_driver
    screen_width, screen_height = (None, None)
    for device_type, selected_dimension in DEVICE_TYPE.items():
        if device_type == 'mobile':
            screen_width, screen_height = selected_dimension
            driver.set_window_size(screen_width, screen_height)
        elif device_type == 'tablet':
            screen_width, screen_height = selected_dimension
            driver.set_window_size(screen_width, screen_height)
        elif device_type == 'laptop':
            screen_width, screen_height = selected_dimension
            driver.set_window_size(screen_width, screen_height)

        for region in APTEAN_REGION:
            new_region = AUTHOR_PAGE.replace('en-US', region)
            driver.get(new_region)

            time.sleep(4)

            driver.execute_script("document.querySelector('header').style.display = 'none';")
            driver.execute_script("document.querySelector('footer').style.display = 'none'")  # footer is displayed
            driver.execute_script("document.getElementsByClassName('optimizely-container')[0].style.display = 'none'")

            # Find the WebElement you want to hide
            # (Replace 'element_id' and 'By.ID' with your element's locator)
            element_to_hide = driver.find_element(By.XPATH, "//app-callout-banner/div")

            print(element_to_hide)

            # Use JavascriptExecutor to set the 'display' style property to 'none'
            driver.execute_script("arguments[0].style.display = 'none';", element_to_hide)

            time.sleep(10)

            while True:
                driver.execute_script(f"window.scrollBy(0, {screen_height});")
                time.sleep(2)
                new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
                total_height = driver.execute_script("return document.body.scrollHeight;")
                if new_height >= total_height:
                    break

            try:
                # iframe_ele = driver.find_elements(By.XPATH, "//div[@id='sl-demo-root']")
                # for element in iframe_ele:
                #     driver.execute_script("arguments[0].scrollIntoView();", element)
                #     # Capture the full-page screenshot using CDP
                screenshot_data = driver.execute_cdp_cmd(
                    "Page.captureScreenshot",
                    {
                        "format": "png",
                        # "clip": clip,
                        "captureBeyondViewport": True  # Essential for full page capture
                    }
                )
                # Decode and save the screenshot
                output_path = f"{device_type}-{selected_dimension}-{region}-{datetime.now().strftime('%Y-%m-%d')}.png"
                with open(output_path, "wb") as f:
                    f.write(base64.b64decode(screenshot_data['data']))
                print(f"Full page screenshot saved as {output_path}")
            except WebDriverException as e:
                print(e)

            # capture_full_page_screenshot(driver, f"{device_type}-{selected_dimension}-{region}-{datetime.now().strftime('%H-%M-%S')}.png")

