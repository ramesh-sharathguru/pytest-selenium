"""
For any web-page with responsiveness : use this script.
This file will only test for website 'url' responsiveness on different screens with different region
can do to fetch url from command line, (like option) - for now URL is hard coded
"""
import os
import pytest
import time

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

DISCRETE_SOLUTION_URL = "https://aptean-website-dev.azurewebsites.net/en-US/discrete-solution"
CAMPAIN_PAGE_URL = "https://aptean-website-dev.azurewebsites.net/en-US/cp/tms"

APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']

DEVICE_TYPE = {
    "mobile":[375,767],
    "tablet":[1138, 712],
    "laptop":[1366,768],
}

# @pytest.mark.parametrize("selected_device", "selected_dimension",DEVICE_TYPE.items())
def test_multi_device_screens(all_tests_driver):
    driver = all_tests_driver

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
            new_region = DISCRETE_SOLUTION_URL.replace('en-US', region)
            time.sleep(1)
            driver.get(new_region)
            WebDriverWait(driver, 30).until(lambda d: d.execute_script(" return document.readyState") == "complete")

            scroll_amount = 200  # Number of pixels per scroll
            while True:
                time.sleep(1)
                user_in = input("Need a screen shot ? ")
                if user_in == "y":
                    driver.save_screenshot( f"{device_type}-{selected_dimension}-{region}-{datetime.now().strftime('%H-%M-%S')}.png")
                else:
                    print("Screen looks good.!!")
                time.sleep(1)
                driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
                total_height = driver.execute_script("return document.body.scrollHeight;")
                if new_height >= total_height:
                    break

            header = driver.find_element(By.TAG_NAME, "h1")
            assert header.is_displayed()

    # -------------------------------------------------------------------------------

    # assert driver.find_element(By.XPATH, "//app-contentful").is_displayed()
    # app_product_ele = driver.find_element(By.XPATH, "//app-contentful//div[contains(@class,'product-cards')]")
    # time.sleep(1)
    # driver.execute_script("arguments[0].scrollIntoView(true);", app_product_ele)
    # time.sleep(1)
    #
    # lead_generation_ele = driver.find_element(By.XPATH, "//app-contentful//div[contains(@class,'lead-generation__container')]")
    # time.sleep(1)
    # driver.execute_script("arguments[0].scrollIntoView(true);", lead_generation_ele)
    # time.sleep(1)
    # #driver.save_screenshot(f"{device_type}-lead-generation-{region}.png")



