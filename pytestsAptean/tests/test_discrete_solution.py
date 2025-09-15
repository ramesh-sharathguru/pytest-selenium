import pytest
import pytest_html
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']
NEW_TARGET_URL = "https://aptean-website-dev.azurewebsites.net/en-US/discrete-solution"

def test_page_alignment(general_driver):
    print("Page alignment test- SUCCESSFUL..!! ")
    driver = general_driver
    devices = ['mobile',] #'tablet', 'desktop','laptop'
    for device_type in devices:
        if device_type == 'mobile':
            driver.set_window_size(375, 867)
        elif device_type == 'tablet':
            driver.set_window_size(1138, 712)
        elif device_type == 'laptop':
            driver.set_window_size(1366, 768)
            print("laptop screen size : ", driver.get_window_size())

        elif device_type == 'desktop':
            driver.maximize_window()
            screen_size = driver.get_window_size()

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

            assert "Discrete Manufacturing Solution" in driver.title

            assert driver.find_element(By.XPATH, "//app-contentful").is_displayed()


            app_product_ele = driver.find_element(By.XPATH, "//app-contentful//div[contains(@class,'product-cards')]")
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", app_product_ele)
            # time.sleep(1)
            #driver.save_screenshot(f"{device_type}-product-card-{region}.png")

            lead_generation_ele = driver.find_element(By.XPATH, "//app-contentful//div[contains(@class,'lead-generation__container')]")
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", lead_generation_ele)
            # time.sleep(1)
            #driver.save_screenshot(f"{device_type}-lead-generation-{region}.png")
